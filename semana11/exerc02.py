def inserir(caixa):
    item = input("Digite o item: ")
    caixa.append(item)

def retirar(caixa):
    item = input("Digite o item: ")
    if item in caixa:
        caixa.remove(item)
    else:
        print("Nenhum item está em caixa.")

def listar(caixa):
    print(caixa)

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
        print("4 - Sair")
        opc = int(input("Digite uma opção: "))
    
        if opc == 1:
            inserir(caixa)
        elif opc == 2:
            retirar(caixa)
        elif opc == 3:
            listar(caixa)
        elif opc == 4:
            off()
            break
        else:
            invalida()

code()
