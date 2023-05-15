def recibo(laranj):
    print(f"Total: R${laranj:.2f}")

def compra(laranj):
    if laranj > 12:
        laranj *= 0.25
    else:
        laranj *= 0.4
    return laranj

def quantidade():
    laranj = int(input("Quantas laranjas deseja comprar?" ))
    return laranj

def code():
    laranj = quantidade()
    compra(laranj)
    recibo(laranj)
    
code()
