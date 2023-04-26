media = 0
for numero in range(1,11):
    numb = float(input(f"Digite o numero {numero}: "))
    media += numb
    
media /= 10
print("A media de todos os números é:",media)
