def inverte(lista):
    lista.reverse()
    print(lista)

def numero():
    lista = []
    for n in range(1,11):
        lista.append(n)
    return lista


def main():
    lista = numero()
    inverte(lista)
    
main()
