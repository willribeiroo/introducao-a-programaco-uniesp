# 1)Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

print("**********************************************************************************")
print("******ALGORITMO PARA LER 20 NÚMEROS E ARMAZENAR EM UM VETOR - ORDEM INVERSA*******")
print("**********************************************************************************")

VET = []
for i in range (20):
   VET.append(int(input("Digite um número inteiro: ")))
print("=-" *50)
print(f"Os 20 números digitados e que foram armazenados no vetor VET são: {VET}")
print("=-" *50)
print("--- ESCREVENDO NÚMEROS LIDOS NA ORDEM INVERSA ---")
VET.reverse()
print("=-" *50)
print(f"A ordem invertida do vetor VET é {VET}")
print("=-" *50)
print("--- FIM ---")
