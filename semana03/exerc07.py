genero = input("Você é homem ou mulher?")
alt = float(input("Qual sua altura?"))

if genero == "homem":
    calcH = ( 72.7 * alt ) - 58
    print("Seu peso ideal é:",calcH,"Kg")
elif genero == "mulher":
    calcM = ( 62.1 * alt ) - 44.7
    print("Seu peso ideal é:",calcM,"Kg")
else:
    print("Nenhum gênero foi selecionado")
