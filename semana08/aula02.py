def espaco():
    print()
    
def maiorD18(maior):
    print("Maiores de idade:", maior)
    espaco()

def idad():
    media = 0
    maior = 0
    faixa = 0
    for i in range(7):
        idade = int(input("Digite sua idade:"))
        media += idade
        if idade >= 18:
            maior += 1
        if idade >= 10 and idade <=30:
            faixa += 1
    return media, maior, faixa
    
def calc(media):
    mediaIda = media / 7
    print("Media de idade:", mediaIda)
    espaco()
    
def porcent(faixa):
    faixa = (faixa / 7) * 100
    print("Porcentagem de pessoas entre 10 e 30 anos é de",faixa,"%")



def code():
    media, maior, faixa = idad()
    calc(media)
    maiorD18(maior)
    porcent(faixa)
  
  
code()
