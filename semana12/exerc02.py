def result(resultado):
    print("A soma é:",resultado)
    print("A media é:",resultado/5)

def soma(lista):
    resultado = 0
    for i in range(5):
        resultado += lista[i]
    return resultado 

def numero():
    lista = []
    for n in range(5):
        numb = float(input("Digite um numero: "))
        lista.append(numb)
    return lista

def code():
    lista = numero()
    resultado = soma(lista)
    result(resultado)
    
code()
