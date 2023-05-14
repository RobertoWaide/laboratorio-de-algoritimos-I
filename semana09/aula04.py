def porcent(a,b,c):
    porA = (a / 10) * 100
    porB = (b / 10) * 100
    porC = (c / 10) * 100
    return porA , porB , porC
    
def resusut(a,porA,b,porB,c,porC):
    print(a,"usam o elevador A com",porA,"%, ",b,"usam o elevador B com",porB,"% e ",c,"usam o elevador c com",porC,"%") 

    
def elev():
    a = 0
    b = 0
    c = 0
    for i in range(1,11):
        print(f"Pessoa {i}")
        elev = input("Qual elevador mais usa, A,B ou C?").upper()

        if elev == "A":
            a += 1
        elif elev == "B":
            b += 1
        elif elev == "C":
            c += 1
    print()
    return a,b,c


def code():
    a,b,c = elev()
    porA , porB , porC = porcent(a,b,c)
    resusut(a,porA,b,porB,c,porC)
    
code()
