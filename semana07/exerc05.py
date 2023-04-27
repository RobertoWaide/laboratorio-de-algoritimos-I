maiorIda = 0
mulhier = 0
olhoAzul = 0
olhoVerde = 0
olhoCas = 0
cabLoiro = 0
cabCas = 0
CabPreto = 0
mulher = 0
homem = 0

for code in range(1, 16):
    print(f"Pessoa {code}")
    sexo = input("Sexo (M/F): ").upper()
    olho = input("Cor dos olhos (Azuis(A), Verdes(V), Castanho(Cm)):").upper()
    cabelo = input("Cor dos cabelos (Loiro(L), Castanho(C), Preto(P)):").upper()
    idade = int(input("Idade:"))

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "F" and idade >= 18 and idade <= 35 and olhos == "V" and cabelos == "L":
        mulhier += 1

    if olho == "A":
        olhoAzul += 1
    elif olho == "V":
        olhoVerde += 1
    elif olho == "C":
        olhoCas += 1

    if cabelos == "L":
        cabLoiro += 1
    elif cabelos == "C":
        cabCas += 1
    elif cabelos == "P":
        cabPreto += 1

    if sexo == "F":
        homem += 1
    elif sexo == "M":
        mulher += 1

porOlhoA = olhoAzul / 15 * 100
porOlhoV = olhoVerde / 15 * 100
porOlhoC = olhoCas / 15 * 100
porCabL = cabLoiro / 15 * 100
porCabC = cabCas / 15 * 100
porCabP = cabPreto / 15 * 100
porM = mulher / 15 * 100
porH = homem / 15 * 100

print("A maior idade é:", maiorIda)
print("A quantidade de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos loiros é de:", mulhier)
print("Porcentagem de pessoas com olhos azuis, verdes e castanhos respectivamente:", porOlhoA, porOlhoV, porOlhoCs)
print("Porcentagem de cabelos loiros, castanhos e pretos respectivamente:", porCabL, porCabC, porCabP)
print("Porcentagem de pessoas do sexo feminino e masculino respectivamente:", porM, porH)
