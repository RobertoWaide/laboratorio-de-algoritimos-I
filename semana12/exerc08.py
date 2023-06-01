def espaco():
    print()

def erro():
    print("Apenas números pares são validos")
    
def inserir(caixa):
    item = int(input("Digite o item: "))
    if item % 2 == 0:
        caixa.append(item)
    else:
        erro()

def retirar(caixa):
    item = int(input("Digite o item: "))
    if item % 2 == 0:
        if item in caixa:
            caixa.remove(item)
        else:
            print("Este item não está em caixa.")
    else:
        erro()

def listar(caixa):
    print(caixa)
    
def limpar(caixa):
    caixa.clear()

def off():
    print("Encerrando sistema...")

def invalida():
    print("Opção inválida!")

def code():
    caixa = []

    while True:
        print("1 - Inserir item")
        print("2 - Retirar item")
        print("3 - Listar itens")
        print("4 - Limpar caixa")
        print("5 - Sair")
        opc = int(input("Digite uma opção: "))
    
        if opc == 1:
            inserir(caixa)
            espaco()
        elif opc == 2:
            retirar(caixa)
            espaco()
        elif opc == 3:
            listar(caixa)
            espaco()
        elif opc == 4:
            Limpar(caixa)
            espaco()
        elif opc == 5:
            off()
            break
        else:
            invalida()
            espaco()

code()
