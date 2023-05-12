def calc(metro):
    print(metro*10,"decimetros")
    print(metro*100,"centimetros")
    print(metro*1000,"milimetros")

def code():
    metro = input("Digite o valor em metros: ")
    metro = float(metro.replace(",","."))
    calc(metro)
    
code()
