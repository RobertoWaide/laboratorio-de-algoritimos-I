def recibo(laranj):
    print(f"Total: R${laranj:.2f}")

def compra(laranj):
    if laranj > 12:
        laranj *= 0.25
    else:
        laranj *= 0.4
    recibo(laranj)

def code():
    laranj = int(input("Quantas laranjas deseja comprar?" ))
    compra(laranj)
    
code()
