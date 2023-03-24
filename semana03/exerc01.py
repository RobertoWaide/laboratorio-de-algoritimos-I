horas = int(input("Informe as horas trabalhadas:"))

### R$35/Hora
### <R$1000 - aumento de R$300

salario = horas * 35

if salario >= 1000:
    print("Seu salário é de R$",salario)
else:
    aumento = salario + 300
    print("Seu salário é de R$",salario,"mais aumento de R$300")
    print("Somando um total de R$",aumento)
