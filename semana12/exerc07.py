def result(gacha,par,impar):
    print(gacha)
    print(par,"pares")
    print(impar,"impares")

def verific(gacha):
    par = 0
    impar  = 0
    for i in range(10):
        if gacha[i] % 2 == 0:
            par += 1
        else:
            impar += 1
    return par,impar

def genshin():
    gacha = []
    import random
    for n in range(10):
        gacha.append(random.randint(1,50))
    return gacha
    

def code():
    gacha = genshin()
    par,impar = verific(gacha)
    result(gacha,par,impar)
    
code()
