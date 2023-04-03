n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

calc = int(input("Soma = 1, Subtrair = 2, Multiplicar = 3 ou Dividir = 4? "))

if calc == 1:
    ulad = "soma"
    ora = n1 + n2
elif calc == 2:
    ulad = "subtração"
    ora = n1 - n2
elif calc == 3:
    ulad = "multiplicação"
    ora = n1 * n2
elif calc == 4:
    ulad = "divisão"
    ora = n1 / n2

print("Resultado da", ulad,"é de:",ora )
