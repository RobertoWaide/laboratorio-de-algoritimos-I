a = 0
b = 0
c = 0

for code in range(1,21):
    print(f"Pessoa {code}")
    gazeta = input("Qual jonal você mais compra?(A,B ou C)").upper()

    if gazeta == "A":
        a += 1
    elif gazeta == "B":
        b += 1
    elif gazeta == "C":
        c += 1

porA = (a / 20) * 100
porB = (b / 20) * 100
porC = (c / 20) * 100
 
if porA <= porB and porA <= porC:
    print ("A porcentagem do A é de:", porA,"%,")
    if porB <= porC:
        print(" a do B é:", porB,"%" " e a do C é:", porC,"%")
    else:
        print(" a do C é:", porC,"%" " e a do B é:", porB,"%")
        
elif porB < porA and porB <= porC:
    print ("A porcentagem do B é de:", porB,"%,")
    if porA <= porC:
        print(" a do A é:", porA,"%" " e a do C é:", porC,"%")
    else:
        print(" a do C é:", porC,"%" " e a do A é:", porA,"%")

elif porC < porA and porC < porB:
    print ("A porcentagem do A é de:", porA,"%,")
    if porA <= porB:
        print(" a do A é:", porA,"%" " e a do B é:", porB,"%")
    else:
        print(" a do B é:", porB,"%" " e a do A é:", porA,"%")
