import random

contador = 0
sala = 1
escolha_caminho = 1
semProcesso = False

print ('''--- Bem-vindo(a) ---\n \nNesse jogo você é líder de uma guilda de aventureiros e,
tem como objetivo chegar ate a sala 9, MAS CUIDADO, 
no meio do caminho há alguns obstáculos e a aventura deve ser terminado em no máximo de 7 jogadas.\n-------------------------------------\n''')
while (sala != 9 and contador < 7 and (escolha_caminho == 1 or escolha_caminho == 2)):
    print('contador = ', contador)
    print('Você está na sala: {}'.format(sala))
    escolha_caminho = int(input('Escolha o seu caminho:\n[1] - Caminho vermelho \n[2] - Caminho preto\n'))
    mensagem = "Não existe essa opção" if sala == 6 and escolha_caminho == 1 else ""
    sala, semProcesso, contador = (random.randint(1,5), True, contador+1) if sala == 8 and escolha_caminho == 2 else (sala, False, contador)

    if semProcesso or len(mensagem) > 0:
        semProcesso = False
        print(mensagem)

    elif escolha_caminho == 1:
        sala += 1
        contador += 1

    else:
        sala += 2
        contador += 1

if escolha_caminho != 1 and escolha_caminho != 2:
    print('\nVocê escolheu um número invalido')

elif sala == 9:
    print('\n- Parabéns, você conseguiu liderar a sua guilda até a sala final! --')

elif contador >= 7:
    print('\nQue pena, você fez mais de 7 movimentos e infelizmente perdeu o jogo')