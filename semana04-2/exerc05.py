p1 = input("Telefonou para a vítima?(Y/N) ").upper()
p2 = input("Esteve no local do crime?(Y/N) ").upper()
p3 = input("Mora perto da vítima?(Y/N) ").upper()
p4 = input("Devia para a vítima?(Y/N) ").upper()
p5 = input("Já trabalhou com a vítima?(Y/N) ").upper()


if p1 =="Y"and p2=="Y"and p3=="Y"and p4=="Y"and p5=="Y":
    print("De fato você é o assassino, e será condenado por seus crimes")
elif (p1=="Y"and p2=="Y"and p3=="Y"and p4=="Y")or(p1=="Y"and p2=="Y"and p3=="Y"and p5=="Y")or(p1=="Y"and p2=="Y"and p5=="Y"and p4=="Y")or(p1=="Y"and p5=="Y"and p3=="Y"and p4=="Y")or(p5=="Y"and p2=="Y"and p3=="Y"and p4=="Y"):
    print("Tudo me leva a crer que você foi cumplice do real assassino e ficara sobre custodia até que provas digam o contrario")
elif (p3=="Y"and p4=="Y"and p5=="Y")or(p2=="Y"and p4=="Y"and p5=="Y")or(p2=="Y"and p3=="Y"and p5=="Y")or(p4=="Y"and p2=="Y"and p3=="Y")or(p1=="Y"and p4=="Y"and p5=="Y")or(p1=="Y"and p5=="Y"and p3=="Y")or(p1=="Y"and p4=="Y"and p3=="Y")or(p1=="Y"and p2=="Y"and p5=="Y")or(p1=="Y"and p2=="Y"and p4=="Y")or(p1=="Y"and p2=="Y"and p3=="Y"):
    print("A testemunha provavelmente é cumplice do assassinato")
elif (p4=="Y"and p5=="Y")or(p3=="Y"and p5=="Y")or(p3=="Y"and p4=="Y")or(p5=="Y"and p2=="Y")or(p4=="Y"and p2=="Y")or(p3=="Y"and p2=="Y")or(p1=="Y"and p5=="Y")or(p1=="Y"and p4=="Y")or(p1=="Y"and p3=="Y")or(p1=="Y"and p2=="Y"):
    print("A testemunha é suspeita, mas nada que prove algo")
elif (p1=="Y")or(p2=="Y")or(p3=="Y")or(p4=="Y")or(p5=="Y"):
    print("A testemunha foi classificada como inocente")
else:
    print("Você é inocente, está liberado")
