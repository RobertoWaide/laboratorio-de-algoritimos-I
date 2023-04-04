l1 = float(input("Informe o primeiro lado: "))
l2 = float(input("Informe o segundo lado: "))
l3 = float(input("Informe o terceiro lado: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l2 == l3:
        print("É um Triângulo Equilátero")
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print("É um Triângulo Isósceles")
    else:
        print("É um Triângulo Escaleno")
else:
    print("Não forma um Triângulo")
