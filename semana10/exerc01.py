def soma(n1,n2):
    print("O resultado a da soma é:",(n1+n2))

def numero():
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    return n1,n2

def code():
    n1,n2 = numero()
    soma(n1,n2)
    
code()
