code = 0
conta = 0
while code != 10:
    code = code + 1
    print("Valor",code)
    valor = int(input("Digite um valor: "))
    if valor >= 30 and valor <= 90:
        conta = conta + 1

print()    
print("Há",conta," números entre 30 a 90")
