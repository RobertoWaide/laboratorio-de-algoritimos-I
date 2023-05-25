def soma(s, n):
    print("Total de pessoas que responderam sim:",s)
    print("Total de pessoas que responderam não:",n)
    
def pesquisa():
    s = 0
    n = 0
    for i in range(5):
        opn = input("Você gostou do produto? [S/N]: ").upper()
        if opn == "S":
            s += 1
        elif opn == "N":
            n += 1
        else:
            print("Opção invalida!")
    return s,n

def code():
    s, n = pesquisa()
    soma(s, n)

code()
