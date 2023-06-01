def result(lista3):
    print("lista3:",lista3)

def novamente(lista1,lista2):
    lista3 = []
    for i in range(5):
        lista3.append(lista1[i]+lista2[i])
    return lista3

def denovo():
    lista2 = []
    for n in range(5):
        numb = int(input("Digite númros da lista 2: "))
        lista2.append(numb)
    return lista2

def numero():
    lista1 = []
    for n in range(5):
        numb = int(input("Digite númros da lista 1: "))
        lista1.append(numb)
    return lista1
    

def code():
    lista1 = numero()
    lista2 = denovo()
    lista3 = novamente(lista1,lista2)
    result(lista3)
    
code()
