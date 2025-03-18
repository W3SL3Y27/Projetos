import random
quer_continuar = True
contador = 1
acertos = 0
erros = 0
while(quer_continuar):
    n1 = random.randint(1,1000)
    n2 = random.randint(1,1000)
    print(f"Q{contador}: {n1}+{n2}")
    resp = int(input("R:"))
    if(resp == n1+n2):
        print("resposta correta")
    else:
        print("resposta incorreta")
    contador = contador+1
    continuar = input("Quer continuar? [1]sim [2nao]")
    if(continuar ==2):
        quer_continuar = False

print("FIM")
