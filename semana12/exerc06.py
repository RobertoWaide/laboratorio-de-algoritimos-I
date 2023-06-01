def result(lista):
    for i in range(6):
        num = int(input("Digite o número que procura: "))
        if num in lista:
           print("Está na lista")
        else:
            print("Não está na lista")

def number():
    lista = []
    import random
    for n in range(5):
        numb = int(input("Digite um número: "))
        lista.append(numb)
    return lista
    

def code():
    lista = number()
    result(lista)
    
code()
