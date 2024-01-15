import random

flip_remaining = 100
points=0 
while True:
    which = random.randint(1,2)
    Cara= 0
    Coroa = 0
    count = 0
    while True:
        count += 1
        if flip_remaining >=0:
            print(f'''
            Você tem {flip_remaining} tentativas:
            ''')
            

            if count == 1:
                    escolha =1
            if count == 2:
                if Cara-Coroa>4:
                    escolha = 4
                elif Cara-Coroa<=-1:
                    escolha = 3
                else:
                    escolha = 1
            if count == 3:
                if Cara-Coroa>=4:
                    escolha = 4
                elif Cara-Coroa<=0:
                    escolha = 3
                else: 
                    escolha = 1
            if count == 4:
                if Cara-Coroa>=5:
                    escolha = 4
                else:
                    escolha = 3
            print("Escolha", escolha)
            g = input()
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
