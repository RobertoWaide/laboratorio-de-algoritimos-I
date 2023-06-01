def result(gacha):
    print(gacha)

def genshin():
    gacha = []
    import random
    for n in range(10):
        gacha.append(random.randint(1,100))
    return gacha
    

def code():
    gacha = genshin()
    result(gacha)
    
code()
