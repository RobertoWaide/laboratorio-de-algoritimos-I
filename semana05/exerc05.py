code = 0
maiorIda = 0
menorIda = 200
mulher = 0
while code != 10:
    code = code + 1
    print(code,"Pessoa")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o gênero (H/M): ").upper()
    salario = float(input("Digite o salario: "))
    if sexo == "M" and salario <= 100:
        mulher = mulher + 1
    if idade > maiorIda:
        maiorIda = idade
    if idade < menorIda:
        menorIda = idade
    print()


media = salario / 10

print("A media salarial é de R$",media)
print("A maior idade é",maiorIda,"e a menor é",menorIda)
print("A quantidade de mulheres que rebem salário até R$100 é de:",mulher)
