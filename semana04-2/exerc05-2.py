p1 = input("Telefonou para a vítima?(Y/N) ").upper()
p2 = input("Esteve no local do crime?(Y/N) ").upper()
p3 = input("Mora perto da vítima?(Y/N) ").upper()
p4 = input("Devia para a vítima?(Y/N) ").upper()
p5 = input("Já trabalhou com a vítima?(Y/N) ").upper()

Y = (+1)

if Y == 5:
    print("De fato você é o assassino, e será condenado por seus crimes")
elif Y == 4: 
    print("Tudo me leva a crer que você foi cumplice do real assassino e ficara sobre custodia até que provas digam o contrario")
elif Y == 3:
    print("A testemunha provavelmente é cumplice do assassinato")
elif Y == 2:
    print("A testemunha é suspeita, mas nada que prove algo")
elif Y == 1:
    print("A testemunha foi classificada como inocente")
elif Y == 0:
    print("Você é inocente, está liberado")
