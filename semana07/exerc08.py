dentro = 0
fora = 0

for code in range(10):
    numero = float(input("Digite um número: "))
    if numero >= 10 and numero <= 20:
        dentro += 1
    else:
        fora += 1

print(dentro,"estão dentro, e",fora,"estão fora do intervalo")
