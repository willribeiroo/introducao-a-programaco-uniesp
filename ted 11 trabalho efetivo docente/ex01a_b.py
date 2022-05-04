#1. Consutra uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
# a. Imprima o resultado da soma de todos os valores da matriz no terminal;
# b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

print("**********************************************************************************")
print("******ALGORITMO PARA LER MATRIZ 10 X 10 - SOMA E MULTIPLICAÇÃO DE MATRIZES *******")
print("**********************************************************************************")

import random
m_a = []

for x in range(1, 11):

    m_aux = []

    for y in range(1, 11):
        m_aux.append(random.randint(0, 100))

    print("--- Adicionando na Matriz ---")
    print(m_aux)
    m_a.append(m_aux)

print("--- Nossa matriz a ---")
print(m_a)

print("--- Somando os valores da matriz a ---")

soma = 0

for i in m_a:
    
    for j in i:
        
        soma += j

print(f'O Resultado da Soma é igual a {soma}')

print("--- Multiplicando os valores da matriz a por 3 ---")
m_b = []

for i in range(0, len(m_a)):
    
    m_auxiliar = []
    
    for j in range(0, len(m_a[i])):
        
        multiplicacao = m_a[i][j] * 3
        m_auxiliar.append(multiplicacao)
        
    m_b.append(m_auxiliar)
        
print(m_b)