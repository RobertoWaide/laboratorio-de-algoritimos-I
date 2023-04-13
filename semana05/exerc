saldo = float(input("Quanto é o saldo atual? "))
code = 0

while code != 4:
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    code = int(input("Selecionar: "))
    if code == 1:
        saque = float(input("Quanto você quer sacar? "))
        if saque > saldo:
            print("Operação negada, o saldo é insuficiente.")
            print()
        else:
            saldo = saldo - saque
            print("Saque efetuado!")
            print()
    elif code == 2:
        depos = float(input("Quanto você quer depositar? "))
        saldo = saldo + depos
        print("Deposito efetuado!")
        print()
    elif code == 3:
        print("seu saldo atual é de:",saldo)
        print()
    elif code == 4:
        print("Encerrando sistema, tenha um bom dia!")
    else:
        print("Operação invalida, selecione uma opção valida.")
        print()
