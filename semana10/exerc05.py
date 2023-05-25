def result(soma):
    print("O resultado é:", soma)

def numero():
    n = int(input("Digite um número: "))
    return n

def natual(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

def code():
    n = numero()
    soma = natual(n)
    result(soma)

code()
