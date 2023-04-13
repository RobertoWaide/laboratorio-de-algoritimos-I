code = 1
conta = 0
while code != 0:
    code = int(input("Digite um número: "))
    if code == 10:
        conta = conta + 1
        
print()
print("Total de número 10 que foi digitado:",conta)
