while True:
    count = 0
    while True:
        count+=1
    
        if count == 1:
            print('''
                  --------------
                  Começa com 5
                  ''')
        else:
            Cara = int(input("Cara"))
            Coroa = int(input("Cara"))
            if count == 2:
                if Cara-Coroa>4:
                    print("Cheater")
                    break
                    
                elif Cara-Coroa<=-1:
                    print("Fair")
                    break
                    
                else:
                    print("Continua com 5")
            if count == 3:
                if Cara-Coroa>=4:
                    print("Cheater")
                    break
                    
                elif Cara-Coroa<=0:
                    print("Fair")
                    break
                else: 
                    print("Continua com 5")
            if count == 4:
                if Cara-Coroa>=5:
                    print("Cheater")
                    break
                else:
                    print("Fair")
                    break
            
            
            