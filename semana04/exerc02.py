
valor = float(input("Digite o valor da peça: "))
forma = int(input("Selecione em quatas vezes quer pagar, de 1 à 3 parcelas: "))

if forma >= 1 and forma <= 3:
    if forma < 2:
        print("Valor á vista é: R$",valor)
        parcel = 0
    else:
        if forma == 2:
            parcel = valor / 2
        else:
            parcel = valor / 3
        print("O valor da parcela é de R$",parcel,"divido em",forma,"vezes")
else:
    print("Nenhuma forma foi selecionada!")
