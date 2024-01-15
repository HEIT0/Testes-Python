import random
pontos = 0
max_pontos =0
min_pontos =1000000
media =0
for i in range(0,10000):
    flip_remaining = 100
    points=0 
    while True:
        which = random.randint(1,2)
        Cara= 0
        Coroa = 0
        count = 0
        while True:
            
            if flip_remaining >=0:
                count+=1
                ##print(f'''
            ## Você tem {flip_remaining} tentativas:
            ## 1- Girar 5 moedas
            ##  2- Girar 1 Moeda
            ##  3- Julgar Justo
            ##  4- Julgar Injusto
            ##   ''')
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
                
               
                
                
                if which ==1:
                    if escolha == 1:
                        flip_remaining-=5
                        for i in range(0,5):
                            
                            cheater = random.randint(1,4)
                            if cheater <= 3:
                                Cara+=1
                            else:
                                Coroa += 1
                        
                    if escolha == 2:
                        flip_remaining-=1
                        cheater = random.randint(1,4)
                        if cheater <= 3:
                            Cara+=1
                        else:
                            Coroa += 1
                            
                if which ==2:
                    if escolha == 1:
                        flip_remaining-=5
                        for i in range(0,5):
                            
                            cheater = random.randint(1,2)
                            if cheater == 2:
                                Cara+=1
                            else:
                                Coroa += 1
                        
                    if escolha == 2:
                        cheater = random.randint(1,2)
                        flip_remaining-=1
                        if cheater == 2:
                            Cara+=1
                        else:
                            Coroa += 1
                if escolha ==3:
                    if which == 2:
                        points += 1
                        flip_remaining+=15
                        break
                    else:
                        flip_remaining -= 30
                        break
                if escolha ==4:
                    if which == 1:
                        points += 1
                        flip_remaining+=15
                        break
                    else:
                        flip_remaining -= 30
                        break
            else:
                pontos += points
                break

        if flip_remaining<0:
                pontos += points
                break
    if points > max_pontos:
        max_pontos = points
    if points < min_pontos:
        min_pontos = points
    media += points-66
print(pontos/10000, max_pontos, min_pontos, media/10000)