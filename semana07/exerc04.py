par = 0
impar = 0
zero = 0

for code in range(1,11):
    numb = int(input(f"Digite o {code}º número: "))
    if numb % 2 == 0:
        par += 1
    else:
        impar += 1
        
    if numb == 0:
        zero += 1
        
if par > 0:
    print("Foi digitado",par,"números pares")
else:
    print("Nenhum número par foi digitado")
if impar > 0:
    print("Foi digitado",impar,"números impares")
else:
    print("Nenhum número impar foi digitado")
if zero > 0:
    print("E",zero,"números zeros foram digitados")
else:
    print("Nenhum número zeo foi digitado")
