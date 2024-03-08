

import random

while True:
    print('Bienvenidos a mi casino')
    jugador = random.randint(2, 26)
    dealer = random.randint(2,26)
    

    while True:
        print(jugador,dealer)
        quiere_mas_cartas = input ('quiere mas cartas? S/N')
        if quiere_mas_cartas =='S':
            nueva_carta=random.randint(1,13)
            jugador = jugador + nueva_carta
            print(jugador,dealer)
        else:
            if jugador == 21 or (jugador > dealer and jugador > 21):
                print ("Ganaste!")
                break
            elif jugador == dealer:
                print('Perdiste')
                break
            else:
                print('Perdiste')
                break
    preguntar_si_salir= input('desea continuar el juego? S/N')
    if preguntar_si_salir == 'S':
            print('gracias por jugar')
            break
    else: 
            print('\n'*20)
                
         

