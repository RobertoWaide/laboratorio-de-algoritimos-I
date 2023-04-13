code = 0
conta = 0
while code != 10:
    code = code + 1
    print("Pessoa",code)
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        conta = conta + 1
    print()
    
print("Total de pessoas maiores de 18:",conta)
