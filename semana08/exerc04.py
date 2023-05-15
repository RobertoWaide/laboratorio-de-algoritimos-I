def result(media):
    if media >= 7:
        print("O aluno está aprovado!")
    elif media < 4:
        print("O aluno está reprovado!")
    else:
        print("O aluno está de recuperação!")

def calc(media):
    media /= 5
    return media

def meddia():
    media = 0
    for i in range(5):
        nota = float(input(f"Digite a {i+1}º nota: "))
        media += nota
    return media
    
def code():
    media = meddia()
    media = calc(media)
    result(media)
    print(media)
code()
