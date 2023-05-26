def porA(a):
    print("A porcentagem do A é de:", a, "%")
    
def porB(b):
    print("A porcentagem do B é de:", b, "%")
    
def porC(c):
    print("A porcentagem do C é de:", c, "%")

def result(a, b, c):
    if a <= b and a <= c:
        porA(a)
        if b <= c:
            porB(b)
            porC(c)
        else:
            porC(c)
            porB(b)
    elif b < a and b <= c:
        porB(b)
        if a <= c:
            porA(a)
            porC(c)
        else:
            porC(c)
            porA(a)
    elif c < a and c < b:
        porC(c)
        if a <= b:
            porA(a)
            porB(b)
        else:
            porB(b)
            porA(a)

def porcent(a, b, c):
    a = (a / 20) * 100
    b = (b / 20) * 100
    c = (c / 20) * 100
    return a, b, c

def lista():
    a = 0
    b = 0
    c = 0

    for i in range(1, 21):
        print(f"Pessoa {i}")
        gazeta = input("Qual jornal você mais compra? (A, B ou C)").upper()

        if gazeta == "A":
            a += 1
        elif gazeta == "B":
            b += 1
        elif gazeta == "C":
            c += 1
    return a, b, c

def code():
    a, b, c = lista()
    a, b, c = porcent(a, b, c)
    result(a, b, c)

code()
