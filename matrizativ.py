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