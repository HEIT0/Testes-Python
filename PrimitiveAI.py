import random

flip_remaining = 100
points=0 
while True:
    which = random.randint(1,2)
    Cara= 0
    Coroa = 0
    while True:
        if flip_remaining >=0:
            print(f'''
            Você tem {flip_remaining} tentativas:
            1- Girar 5 moedas
            2- Girar 1 Moeda
            3- Julgar Justo
            4- Julgar Injusto
            ''')
            escolha = int(input())
            if which ==1:
                if escolha == 1:
                    flip_remaining-=5
                    for i in range(0,5):
                        
                        cheater = random.randint(1,4)
                        if cheater <= 3:
                            Cara+=1
                        else:
                            Coroa += 1
                    print(f'Ele rodou {Cara} caras e {Coroa} coroas')
                if escolha == 2:
                    flip_remaining-=1
                    cheater = random.randint(1,4)
                    if cheater <= 3:
                        Cara+=1
                    else:
                        Coroa += 1
                    print(f'Ele rodou {Cara} caras e {Coroa} coroas')     
            if which ==2:
                if escolha == 1:
                    flip_remaining-=5
                    for i in range(0,5):
                        
                        cheater = random.randint(1,2)
                        if cheater == 2:
                            Cara+=1
                        else:
                            Coroa += 1
                    print(f'Ele rodou {Cara} caras e {Coroa} coroas')
                if escolha == 2:
                    cheater = random.randint(1,2)
                    flip_remaining-=1
                    if cheater == 2:
                        Cara+=1
                    else:
                        Coroa += 1
                    print(f'Ele rodou {Cara} caras e {Coroa} coroas')
            if escolha ==3:
                if which == 2:
                    print("Você Acertou: +15 tentativas")
                    points += 1
                    flip_remaining+=15
                    break
                else:
                    print("Você Errou: -30 tentativas")
                    flip_remaining -= 30
                    break
            if escolha ==4:
                if which == 1:
                    print("Você Acertou: +15 tentativas")
                    points += 1
                    flip_remaining+=15
                    break
                else:
                    print("Você Errou: -30 tentativas")
                    flip_remaining -= 30
                    break
        else:
            print(f"Perdeu com {points} pontos")
            break

    if flip_remaining<1:
            print(f"Perdeu com {points} pontos")
            break
