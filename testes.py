import random



lista = ['❌', '❌', '❌', '❌', '❌', '🚢', '🚢', '🚢']
random.shuffle(lista)
print(lista)

ondas = ['🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊']

matriz = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4']

tentativas = 0
barco = '🚢'
acertos = 0



def mostrar_tabuleiro():
    print('    1    2   3    4')
    print('  ---------------------')
    print('A | {} | {} | {} | {} |'.format(ondas[0], ondas[1], ondas[2], ondas[3]))
    print('  ---------------------')
    print('B | {} | {} | {} | {} |'.format(ondas[4], ondas[5], ondas[6], ondas[7]))

for tentativas in range(0, 4, tentativas+1):
    if acertos == 3:
        print('VOCÊ GANHOU!!!\n')
        break
    chute = str(input('Qual posição? \n'))
    for c in range(0, 7):
        if chute == matriz[c]:
            ondas[c] = lista[c]
            if lista[c] == barco:
                print('Você acertou!\n')
                acertos = acertos + 1
                print(acertos)
            else:
                print("Você errou!\n")
    mostrar_tabuleiro()







