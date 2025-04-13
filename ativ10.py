conta_correta = "123"
senha_correta = "321"
saldo = 1500
outro_saque = True

conta = input("conta: ")
senha = input("senha: ")

while(outro_saque):
    if conta != conta_correta or senha != senha_correta:
        print ("conta ou senha incorretas,tente novamente")
    else:
        print ("login bem-sucedido")
        print (f"saldo disponivel:{saldo}")
        print ("notas: 100,50,20,10")
        saque = int(input("saque(multiplos de 10): "))
        if saque > saldo:
            print("saldo insuficiente")
        elif saque%10 != 0:
            print("saque invalido,somente multiplos de 10")
        else:
            notas = {}
            valor_sacado = 0
            for nota in [100, 50, 20, 10]:
                qtd = saque //nota
                notas[nota] = qtd
                saque%= nota
                valor_sacado += nota * qtd
            print("notas entregues: ")
            for nota, qtd in notas.items():
                if qtd > 0:
                    print(f"R$ {nota} x {qtd}")
            saldo -= valor_sacado
            print(f"saldo R$:{saldo}")
            continuar = input("realizar outro saque (1)sim (2)não")
            if continuar == 2:
                outro_saque == False