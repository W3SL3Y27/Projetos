#Exercicio 1

a = int(input("digite um numero: "))
b = int(input("digite um numero: "))
c = int(input("digite um numero: "))
d = int(input("digite um numero: "))

matriz = [
    [a , b],
    [c , d],
]

for linha in matriz:
    print(linha)

#Exercicio 2

soma = 0

for linha in matriz:
    for coluna in linha:
        soma += coluna
print(soma)

#Exercicio 3

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7 ,8, 9],
]

for linha in range(3):
    print(matriz[linha][linha], end=", " if linha < 2 else "\n")

#Exercicio 4

pares = 0

for l in matriz:
    for c in l:
        if c%2 == 0:
            pares += 1

print(f"numeros pares:",(pares))

#Exercicio 5

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o número da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for i in range(3):
    soma = sum(matriz[i])
    print(f"Linha {i}: soma = {soma}")
