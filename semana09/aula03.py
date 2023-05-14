def dados(maiorIda,menorIda,mulher):
    print("A maior idade é",maiorIda,"e a menor é",menorIda)
    print("A quantidade de mulheres que rebem salário até R$100 é de:",mulher)
    
def calc(salario):
    media = salario / 10
    print("A media salarial é de R$",media)

def question():
    maiorIda = 0
    menorIda = 999999
    mulher = 0
    salario = 0
    for i in range(3):
        print(i,"Pessoa")
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o gênero (H/M): ").upper()
        sal = float(input("Digite o salario: "))
        if sexo == "M" and salario <= 100:
            mulher += 1
        if idade > maiorIda:
            maiorIda = idade
        if idade < menorIda:
            menorIda = idade
        salario += sal
        print()
    return mulher,maiorIda,menorIda,salario


def code():
    mulher,maiorIda,menorIda,salario = question()
    calc(salario)
    dados(maiorIda,menorIda,mulher)
    
code()
    
