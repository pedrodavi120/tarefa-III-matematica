# **Tarefa III: Algoritmo de Integração Numérica (Regra de Simpson)**

Este repositório contém a resolução da **Tarefa III** da disciplina de **Matemática Aplicada II**, focada na implementação de algoritmos numéricos para resolução de integrais definidas.

## **📋 Informações do Aluno**

* **Nome:** Pedro Davi Hipolito Silva de Lucena  
* **Disciplina:** Matemática Aplicada II  
* **Professora:** Tásia Moura Cardoso do Vale  
* **Tema:** Integração Numérica (Regra 1/3 de Simpson)

## **🎯 Objetivo da Tarefa**

**"Busque um algoritmo que realize integrais, busque uma aplicação e explique com suas palavras."**

O objetivo principal é demonstrar como métodos computacionais podem resolver integrais que são difíceis ou impossíveis de serem calculadas analiticamente (no papel), aplicando o algoritmo em cenários reais de Estatística e Física.

## **🧮 O Algoritmo: Regra de Simpson (1/3)**

A **Regra de Simpson** é um método numérico que aproxima a integral definida de uma função $f(x)$ utilizando polinômios de segundo grau (parábolas).

Ao contrário da *Regra dos Trapézios* (que usa linhas retas), a Regra de Simpson conecta cada três pontos da função com uma curva suave. Isso resulta em uma precisão significativamente maior com o mesmo número de passos.

### **Fórmula Matemática**

$$I \\approx \\frac{h}{3} \[f(x\_0) \+ 4f(x\_1) \+ 2f(x\_2) \+ 4f(x\_3) \+ \\dots \+ f(x\_n)\]$$  
Onde:

* $h$ é a largura do passo.  
* Os coeficientes seguem o padrão 1, 4, 2, 4, ..., 1\.

## **🚀 Aplicações Práticas**

### **1\. Estatística: A Curva de Gauss**

A função de distribuição normal ($f(x) \= e^{-x^2}$) é fundamental para calcular probabilidades. No entanto, ela **não possui primitiva elementar**.

* **Resultado:** O algoritmo calculou a área sob a curva com precisão de 8 casas decimais, permitindo obter probabilidades exatas sem uso de tabelas manuais.

### **2\. Física: Cinemática (Deslocamento)**

Para calcular a distância percorrida por um objeto com velocidade variável $v(t) \= 3t^2 \+ 2t$, utilizamos a integral da velocidade.

* **Resultado:** Como a função velocidade é um polinômio, a Regra de Simpson conseguiu obter o valor **exato** do deslocamento (80 metros), validando a implementação.

## **💻 Como Executar o Código**

### **Pré-requisitos**

* Python 3.x instalado.

### **Passo a Passo**

1. Clone este repositório:  
   git clone \[https://github.com/pedrodavi120/tarefa-III-matematica.git\](https://github.com/pedrodavi120/tarefa-III-matematica.git)

2. Entre na pasta do projeto:  
   cd tarefa-III-matematica

3. Execute o script:  
   python integracao\_simpson.py

## **📊 Resultados Obtidos**

| Aplicação | Intervalo | Valor Algoritmo | Valor Real | Erro |
| :---- | :---- | :---- | :---- | :---- |
| **Gaussiana** | $$0, 1$$ | 0.74682413 | 0.74682413 | \~0.00 |
| **Física** | $$0, 4$$ | 80.00000000 | 80.00000000 | 0.00 |

Desenvolvido por **Pedro Davi Hipolito Silva de Lucena** para a disciplina de Matemática Aplicada II.