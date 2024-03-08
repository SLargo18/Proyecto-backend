

import random

victorias=0
derrotas=0

while True:
    print('Bienvenidos a mi casino')
    jugador = random.randint(2, 26)
    dealer = random.randint(2,26)
    

    while True:
        print('jugador:',jugador, 'dealer:',dealer)
        quiere_mas_cartas = input ('quiere mas cartas? S/N')
        if quiere_mas_cartas =='S':
            nueva_carta=random.randint(1,13)
            jugador += nueva_carta
            print("nueva carta para el jugador:", nueva_carta)
        else:
            if jugador == 21 or (jugador > dealer and jugador > 21):
                print ("Ganaste!")
                victorias += 1
                break
            elif jugador == dealer:
                print('Perdiste')
                derrotas +=1
                break
            else:
                print('Perdiste')
                derrotas +=1
                break
    preguntar_si_salir= input('desea continuar el juego? S/N')
    if preguntar_si_salir == 'S':
            print('gracias por jugar')
            print('total de victorias:', victorias)
            print('Total de derrotas', derrotas)
            break
    else: 
            print('\n'*20)
    #juego.append
                
         

