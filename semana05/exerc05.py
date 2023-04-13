numbPess = 0
maior18 = 0
ento = 0
while numbPess != 3:
    numbPess = numbPess + 1
    print("Cadastro - Pessoa",numbPess)
    idade = int(input("Digite a idade: "))
    if idade > 17:
        maior18 = maior18 + 1
    if idade >= 10 and idade <= 30:
        ento = ento + 1 
        porc = (ento / 7) * 100 
    peso = float(input("Digite o peso: "))
    print()

media = idade / 7
    
print("A media de idade é:",media, ",com um total de",maior18,"pessoas maior(es) de idade.")
print("Com uma porcentagem de",porc,"% de pessoas entre 10 a 30 anos.")

#### print("E o peso você enfia no seu...")####
