def result(maior,menor):
    print("O menor é:",menor)
    print("O maior é:",maior)

def idade(lista):
    maior = 0
    menor = 999
    for i in range(5):
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
    return maior,menor

def numero():
    lista = []
    for n in range(5):
        numb = float(input("Digite um numero: "))
        lista.append(numb)
    return lista
    

def code():
    lista = numero()
    maior,menor = idade(lista)
    result(maior,menor)
    
code()
