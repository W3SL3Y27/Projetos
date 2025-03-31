prova1 = int(input("nota prova1: "))
prova2 = int(input("nota prova2: "))
nota = prova1+prova2

if(nota/2 >=5):
    print("aprovado")
else:
    print("reprovado")
    print("direito a uma prova de recuperaçao")
    prov3 = int(input("nota recuperaçao: "))
    nota+=prov3
if(nota/2 >=5):
    print("aprovado")
else:
    print("reprovado")
