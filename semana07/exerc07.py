code = 0
numb1 = int(input("Digite o primeiro número:"))
numb2 = int(input("Digite o segundo número:"))

if numb1 < numb2:
    for code in range (numb1, numb2):
        if code % 2 == 0:
            print("Os números pares são:", code)

elif numb1 > numb2:
    for code in range (numb1, numb2, -1):
        if code % 2 == 0:
            print("Os números pares são:", code)
