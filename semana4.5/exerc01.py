nome = input("Informe o nome do funcionario(a): ")
sala = float(input("Seu salário atual: "))
tempo = int(input("E anos de serviço: "))

if tempo >= 5 and sala < 2000:
    bnus = sala * 1.10
    porcento = "10%"
else:
    bnus = sala * 1.05
    porcento = "5%"

print("O funcionário(a)", nome ,"com salário de R$",sala, "que trabalha à ",tempo," anos na empresa;") 
print("teve um reajuste de" ,porcento, ", totalizando R$",bnus)
