matriz = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
for linha in matriz:
    for i in linha:
        print(f'|{i}|', end='')
    print()
jogada_usuario1 = input('jogador1 Ex(02):')
jogada_usuario2 = input('jogador2 Ex(02):')
matriz[int(jogada_usuario1[0])][int(jogada_usuario1[1])] = 'X'
matriz[int(jogada_usuario2[0])][int(jogada_usuario2[1])] = 'O'
for linha in matriz:
    for i in linha:
        print(f'|{i}|', end='')
    print()