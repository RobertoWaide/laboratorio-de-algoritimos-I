def menu():
    print("1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostrar saldo")
    print("4 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc
    
def sacar(saldo):
    saque = float(input("Quanto deseja sacar: "))
    if saque <= saldo:
        saldo = saldo - saque

    else:
        print("Saldo insuficiente!")
    mostrar(saldo)
    return saldo
    
def depositar(saldo):
    deposito = float(input("Quanto deseja depositar:"))
    saldo += deposito
    mostrar(saldo)
    return saldo
    
def mostrar(saldo):
    print("Saldo atual:", saldo)
    print()
    
def code():
    saldo = 0
    opc = 0
    while opc != 4:
        opc = menu()
        if opc == 1:
            saldo = sacar(saldo)
        elif opc == 2:
            saldo = depositar(saldo)
        elif opc == 3:
            mostrar(saldo)
        elif opc == 4:
            print("Deslisgando sistema...")
        else:
            print("Opção inavlida!")
        
code()
