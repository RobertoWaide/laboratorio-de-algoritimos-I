code = 0
conta = 0
a = 0
b = 0
c = 0

while code != 10:
    code = code + 1
    print("Pessoa",code)
    elev = input("Qual elevador mais usa, A,B ou C? ").upper()
    if elev == "A":
        a = a + 1
        porA = (a / 10) * 100
    elif elev == "B":
        b = b + 1
        porB = (b / 10) * 100
    elif elev == "C":
        c = c + 1
        porC = (c / 10) * 100
    
print(a,"usam o elevador A com",porA,"%, ",b,"usam o elevador B com",porB,"% e ",c,"usam o elevador c com",porC,"%")
