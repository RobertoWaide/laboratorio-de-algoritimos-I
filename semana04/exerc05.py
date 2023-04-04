categ = input("Qual a categoria de sua carteira de habilitação? ").upper()

if categ == "A":
    oria = "motos e triciclos"
elif categ == "B":
    oria = "carros de passeio"
elif categ == "C":
    oria = "veículos de carga acima de 3,5 ton."
elif categ == "D":
    oria = "veículos com mais de 8 passageiros"
elif categ == "E":
    oria = "veículos com unidade acoplada acima de 6 ton."
else:
    oria = "[NENHUMA CATEGORIA FOI SELECIONADA]"

print("Você está autorizado a dirigir",oria)
