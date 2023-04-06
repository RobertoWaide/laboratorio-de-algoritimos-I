compra = int(input("Você quer comprar morango(0), maçã(1) ou os dois(2)? "))

if compra == 0:
    morango = float(input("Quantos Kg você quer? "))
    if morango > 5:
        calMg = morango * 2.20
    else:
        calMg = morango * 2.50
    fruta = calMg
    peso = morango
elif compra == 1:
    maca = float(input("Quantos Kg você quer? "))
    if maca > 5:
        calMc = maca * 1.50
    else:
        calMc = maca * 1.80
    fruta = calMc
    peso = maca
elif compra == 2:
    morango = float(input("Quantos Kg de morango você quer? "))
    maca = float(input("E quantos Kg de maçã? "))
    if morango > 5:
        calMg = morango * 2.20
    else:
        calMg = morango * 2.50
    if maca > 5:
        calMc = maca * 1.50
    else:
        calMc = maca * 1.80
    fruta = calMc + calMg
    peso = maca + morango

if peso > 8 or fruta > 25:
    result = fruta * 0.90
else:
    result = fruta

print("O valor da compra deu: R$",result)
