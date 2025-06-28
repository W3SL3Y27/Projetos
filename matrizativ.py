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

#Exercicio 6

matriz = [
    [10, 20, 30],
    [40, 50, 60]
]

print("Matriz (2x3):")
for linha in matriz:
    print(linha)

transposta = [[linha[n] for linha in matriz] for n in range(len(matriz[0]))]

print("Matriz transposta (3x2):")
for linha in transposta:
    print(linha)

#Exercicio 7

matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

diagonal = [matriz[n][2 - n] for n in range(3)]

soma = sum(diagonal)

print("diagonal:")
for n in diagonal:
    print(n)

print("Soma da diagonal:", soma)

#Exercicio 8

matriz = [
    [12, 45, 78, 33],
    [56, 23, 67, 89],
    [90, 11, 34, 66],
    [40, 99, 10, 25]
]

print("Matriz 4x4:")
for linha in matriz:
    print(linha)

maior = max(max(linha) for linha in matriz)
menor = min(min(linha) for linha in matriz)

print("Maior:", maior)
print("Menor:", menor)

#exercicio 9

matriz = [
    [4, 7, 1],
    [9, 3, 8],
    [6, 2, 5]
]

print("Matriz 3x3:")
for linha in matriz:
    print(linha)

numero = int(input("Digite um número para procurar na matriz: "))

encontrado = False
for l in range(3):
    for c in range(3):
        if matriz[l][c] == numero:
            print(f"Número encontrado na posição [{l}][{c}]")
            encontrado = True

if not encontrado:
    print("Número não encontrado na matriz.")
