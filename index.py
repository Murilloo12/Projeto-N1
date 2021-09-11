import random

contador = 0
sala = 1
escolha_caminho = 1
semProcesso = False

while (sala != 9 and contador < 7 and (escolha_caminho == 1 or escolha_caminho == 2)):
    print('contador = ', contador)
    print('Você está na sala: {}'.format(sala))
    escolha_caminho = int(input('Escolha o seu caminho:\n[1] - Caminho vermelho \n[2] - Caminho preto\n'))
    
    while(sala == 6 and escolha_caminho == 1):
        print("Não existe essa opção")
        semProcesso = True
        break

    while(sala == 8 and escolha_caminho == 2):
        sala = random.randint(1,5)
        semProcesso = True
        contador += 1
        break

    if semProcesso:
        semProcesso = False
    elif escolha_caminho == 1:
        sala += 1
        contador += 1
    else:
        sala += 2
        contador += 1
        
if escolha_caminho != 1 and escolha_caminho != 2:
    print('Você escolheu um número invalido')
elif sala == 9:
    print('GANHOU')
elif contador >= 7:
    print('EXTRAPOLOU')