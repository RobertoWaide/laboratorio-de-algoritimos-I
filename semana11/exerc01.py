def acima(valors):
    for n in valors:
        if n > 100:
            print(n)
    
def numb():
    valors = []
    
    for n in range(10):
        valor = float(input("Digite um número: "))
        valors.append(valor)
    return valors

def code():
    valors = numb()
    acima(valors)

code()
