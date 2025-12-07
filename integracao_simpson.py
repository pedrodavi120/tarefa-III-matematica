import math

def explicacao_teorica():
    """
    Imprime a explicação do algoritmo e das aplicações.
    """
    texto = """
    ========================================================================
    RELATÓRIO: ALGORITMO DE INTEGRAÇÃO NUMÉRICA (Regra de Simpson)
    ========================================================================
    
    1. O ALGORITMO: Regra de Simpson (1/3)
    ------------------------------------------------------------------------
    A Regra de Simpson aproxima a área sob uma curva substituindo pequenos 
    segmentos da função original por arcos de parábola.
    Fórmula: I ≈ (h/3) * [y0 + 4y1 + 2y2 + 4y3 + ... + yn]
    
    2. APLICAÇÃO 1: ESTATÍSTICA (A Curva de Gauss)
    ------------------------------------------------------------------------
    Calculamos a área da distribuição normal (e^-x^2). Essencial para saber
    probabilidades em eventos naturais.

    3. APLICAÇÃO 2: FÍSICA (Cinemática / Deslocamento)
    ------------------------------------------------------------------------
    Problema: Um objeto se move com velocidade variável.
    Sabemos que a Distância é a Integral da Velocidade no tempo.
    
    Se v(t) = 3t^2 + 2t (metros/s), qual a distância percorrida entre
    t=0 e t=4 segundos?
    
    Solução Analítica (para comparação):
    A primitiva de (3t^2 + 2t) é (t^3 + t^2).
    Calculando de 0 a 4: (4^3 + 4^2) - 0 = 64 + 16 = 80 metros.
    
    Vamos ver se o algoritmo numérico acerta!
    ========================================================================
    """
    print(texto)

def regra_de_simpson(funcao, a, b, n):
    """
    Implementa a Regra de Simpson composta.
    Args:
        funcao: A função Python f(x) a ser integrada.
        a (float): Limite inferior.
        b (float): Limite superior.
        n (int): Número de subintervalos (deve ser par).
    """
    if n % 2 != 0:
        n += 1 
        
    h = (b - a) / n
    soma = funcao(a) + funcao(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            soma += 2 * funcao(x)
        else:
            soma += 4 * funcao(x)
            
    return soma * (h / 3)

# --- Funções para Teste ---

def funcao_gaussiana(x):
    # Aplicação 1: Estatística (sem solução analítica simples)
    return math.exp(-x**2)

def funcao_velocidade(t):
    # Aplicação 2: Física (v(t) = 3t^2 + 2t)
    return 3*(t**2) + 2*t

# --- Execução Principal ---

if __name__ == "__main__":
    explicacao_teorica()
    
    # --- CASO 1: ESTATÍSTICA ---
    print("\n--- TESTE 1: APLICAÇÃO ESTATÍSTICA (Curva de Gauss) ---")
    a1, b1, n1 = 0.0, 1.0, 100
    res_gauss = regra_de_simpson(funcao_gaussiana, a1, b1, n1)
    ref_gauss = 0.74682413
    print(f"Integral de e^(-x^2) de {a1} a {b1}: {res_gauss:.8f}")
    print(f"Erro absoluto: {abs(res_gauss - ref_gauss):.10f}")

    # --- CASO 2: FÍSICA ---
    print("\n--- TESTE 2: APLICAÇÃO FÍSICA (Distância Percorrida) ---")
    # Vamos calcular a distância de t=0 até t=4
    a2, b2, n2 = 0.0, 4.0, 10
    
    print(f"Função Velocidade: v(t) = 3t^2 + 2t")
    print(f"Intervalo de tempo: {a2}s a {b2}s")
    
    distancia = regra_de_simpson(funcao_velocidade, a2, b2, n2)
    distancia_exata = 80.0 # Como calculado na teoria (4^3 + 4^2)
    
    print(f"Distância Calculada (Simpson): {distancia:.8f} metros")
    print(f"Distância Exata (Analítica)  : {distancia_exata:.8f} metros")
    
    if abs(distancia - distancia_exata) < 1e-9:
        print("Resultado: O algoritmo foi PERFEITO (erro desprezível).")
    else:
        print("Resultado: Aproximação muito boa.")
