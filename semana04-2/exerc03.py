media = float(input("Digite a media final do aluno:"))
frequencia = float(input("Digite a frequencia do aluno (%):"))

if media >= 7 and frequencia >= 75:
    print("O aluno está aprovado")
elif media >= 4 and media < 7 and frequencia >= 75:
    print("O aluno terá que fazer o exame")
else:
    print("Reprovado")
