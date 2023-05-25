def f(graus):
    graus = graus * 1.8 + 32
    print(graus,"F")

def c():
    graus = float(input("Digite um graus Celsius: "))
    return graus

def code():
    graus = c()
    f(graus)
    

code()
