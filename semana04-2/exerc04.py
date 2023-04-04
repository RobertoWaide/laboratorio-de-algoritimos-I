n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2 ) / 2

if media >= 6 and media <= 10:
    if media >= 9 and media <= 10:
        conc = "A"
    elif media >= 7.5 and media < 9:
        conc = "B"
    else:
        conc = "C"
    print("O aluno está aprovado com nota", conc)
elif media >= 0 and media < 6:
    if media >= 4 and media < 6:
        conc = "D"
    else:
        conc = "E"
    print("O aluno está reprovado com nota", conc)
else:
    print("Você digitou alguma coisa errada, a media deu", media)

