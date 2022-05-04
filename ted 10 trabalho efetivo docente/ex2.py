# 2)Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

from typing import Counter
from unittest import result


print("******************************************************************************************")
print("******ALGORITMO PARA LER 50 NÚMEROS E ARMAZENAR EM UM VETOR - POSIÇÃO DOS REPETIDOS*******")
print("******************************************************************************************")

VET = []
i = 0
pos = []
for i in range (0,50):
   VET.append(int(input(f"Digite um valor para a posição {i}: ")))
print(f" O vetor VET é igual a: {VET}.")
print("=-" *50)
print("--- VERIFICANDO NÚMEROS REPETIDOS E SUAS POSIÇÕES ---")
cont = Counter(VET)
for i, repeticoes in cont.items():
    if repeticoes > 1:
        result = [pos for pos, item in enumerate(VET) if item == i]
        print(f"O número {i} se repete nas posições {result}.")
print("--- FIM ---")