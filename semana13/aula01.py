def reset():
    horas = [44] * 20
    falta = [0] * 20
    return horas, falta
    
def ver(horas, falta):
    funcionario = int(input("Digite o código do funcionário: "))
    while funcionario > 20 or funcionario < 1:
        print("Não há funcionários com esse número!")
        funcionario = int(input("Digite o código do funcionário: "))
    print("Horas trabalhadas:", horas[funcionario - 1])
    print("Horas ausentes:", falta[funcionario - 1])
    
def menu():
    print("1 - Verificar o total de horas trabalhadas e ausentes de um funcionário em questão")
    print("2 - Alterar o total de horas trabalhadas de um funcionário em questão")
    print("3 - Alterar o total de horas ausentes de um funcionário em questão")
    print("4 - Mostrar o salário do funcionário")
    print("5 - Mostrar o funcionário com seu total de horas")
    print("6 - Resetar")
    print("7 - Sair")
    
    opc = int(input("Digite sua opção: "))
    
    return opc 

def ver_salario(horas, funcionario):
    salario = horas[funcionario - 1] * 50
    print(f"Salário do funcionário {funcionario}: R${salario:.2f}")

def total_horas(horas, falta):
    for i in range(20):
        print(f"Código {i + 1} - Horas trabalhadas: {horas[i]}, faltas: {falta[i]}")

def mudar(horas, falta):
    funcionario = int(input("Digite o código do funcionário: "))
    while funcionario > 20 or funcionario < 1:
        print("Não há funcionários com esse número!")
        funcionario = int(input("Digite o código do funcionário: "))
    h = int(input("Digite a alteração de horas trabalhadas: "))
    while h > 44:
        h = int(input("Horario maximo ultrapassado, digite novamente: "))
    horas[funcionario - 1] = h
    falta[funcionario - 1] = 44 - h
    return horas, falta

def faltou(horas, falta):
    funcionario = int(input("Digite o código do funcionário: "))
    while funcionario > 20:
        print("Não há funcionários com esse número!")
        funcionario = int(input("Digite o código do funcionário: "))
    h = int(input("Digite a alteração de horas ausentes: "))
    while h > 44:
        h = int(input("Horario maximo ultrapassado, digite novamente: "))
    falta[funcionario - 1] = h
    horas[funcionario - 1] = 44 - h
    return horas, falta

def main():
    horas, falta = reset()
    opc = menu()
    while True:
        if opc == 1:
            ver(horas, falta)
            print()
        elif opc == 2:
            horas, falta = mudar(horas, falta)
            print()
        elif opc == 3:
            horas, falta = faltou(horas, falta)
            print()
        elif opc == 4:
            funcionario = int(input("Digite o código do funcionário: "))
            ver_salario(horas, funcionario)
            print()
        elif opc == 5:
            total_horas(horas, falta)
            print()
        elif opc == 6:
            horas, falta = reset()
            print()
        elif opc == 7:
            print("Obrigado por me usar!")
            break
        else:
            print("Digite uma opção válida!")
            print()    
        opc = menu()
        
main()
