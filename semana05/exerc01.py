code = 0
conta = 0
medA = 0
medI = 0


while code != 3:
    print("1 - Cadastrar pessoa")
    print("2 - Mostar média parcial")
    print("3 - Sair")
    code = int(input("Selecionar: "))
    
    if code == 1:
        alt = float(input("Digite a altura: "))
        ida = int(input("Digite a idade: "))
        print("Cadastro registrado!")
        medA = medA + alt
        medI = medI + ida
        conta = conta + 1
        print()
    elif code == 2:
        if conta == 0:
            print("Nenhum valor ainda foi cadastrado.")
            print()
        else:
            medAlt = medA / conta
            medIda = medI / conta
            print("A média de altura é",medAlt,"m e a média de idade é",medIda,"anos")
            print()
    elif code == 3:
        if conta > 0:
            medAlt = medA / conta
            medIda = medI / conta
            print("As medias totais são:",medAlt,"metros e",medIda,"anos!")
        else:
            print("Nenhuma mudança foi efetuada.")
        print("Encerrando sistema!")
    else:
        print("Nenhuma opção foi Selecionada.")
        print()
