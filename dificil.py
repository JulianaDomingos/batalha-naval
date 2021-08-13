import random

def jogar():

    lista = ['❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌',
             '❌', '❌', '🚢', '🚢', '🚢', '🚢', '🚢']
    random.shuffle(lista)
    print(lista)


    ondas = ['🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊',
             '🌊', '🌊', '🌊', '🌊', '🌊', '🌊', '🌊']

    print('    1    2   3    4    5')
    print('  ------------------------')
    print('A | {} | {} | {} | {} | {} |'.format(ondas[0], ondas[1], ondas[2], ondas[3], ondas[4]))
    print('  ------------------------')
    print('B | {} | {} | {} | {} | {} |'.format(ondas[5], ondas[6], ondas[7], ondas[8], ondas[9]))
    print('  ------------------------')
    print('C | {} | {} | {} | {} | {} |'.format(ondas[10], ondas[11], ondas[12], ondas[13], ondas[14]))
    print('  ------------------------')
    print('D | {} | {} | {} | {} | {} |'.format(ondas[15], ondas[16], ondas[17], ondas[18], ondas[19]))
    print('  ------------------------')
    print('E | {} | {} | {} | {} | {} |'.format(ondas[20], ondas[21], ondas[22], ondas[23], ondas[24]))
    print('  ------------------------')

    matriz = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5',
              'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']

    tentativas = 0
    barco = '🚢'
    acertos = 0


    def mostrar_tabuleiro():
        print('    1    2   3    4    5')
        print('  ------------------------')
        print('A | {} | {} | {} | {} | {} |'.format(ondas[0], ondas[1], ondas[2], ondas[3], ondas[4]))
        print('  ------------------------')
        print('B | {} | {} | {} | {} | {} |'.format(ondas[5], ondas[6], ondas[7], ondas[8], ondas[9]))
        print('  ------------------------')
        print('C | {} | {} | {} | {} | {} |'.format(ondas[10], ondas[11], ondas[12], ondas[13], ondas[14]))
        print('  ------------------------')
        print('D | {} | {} | {} | {} | {} |'.format(ondas[15], ondas[16], ondas[17], ondas[18], ondas[19]))
        print('  ------------------------')
        print('E | {} | {} | {} | {} | {} |'.format(ondas[20], ondas[21], ondas[22], ondas[23], ondas[24]))
        print('  ------------------------')




    for tentativas in range(0, 10, tentativas+1):
        if acertos == 5:
            print('VOCÊ GANHOU!!!\n')
            break
        chute = str(input('Qual posição? \n'))
        for c in range(0, 24):
            if chute.upper() == matriz[c]:
                ondas[c] = lista[c]
                if lista[c] == barco:
                    print('Você acertou!\n')
                    acertos = acertos + 1
                    print(acertos)
                else:
                    print("Você errou!\n")
        mostrar_tabuleiro()


if(__name__ == "__main__"):
    jogar()
