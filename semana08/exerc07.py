def ponteiros(hora):
    hora = hora.replace(".", ":")
    print(f"{hora:.2f}")

def ajuste(hora):
    hora -= 12
    return hora

def relogio():
    hora = input("Digite o horario: ")
    hora = hora.replace(",", ".").replace(":", ".").replace(";", ".")
    return float(hora)

def code():
    hora = relogio()
    if hora > 12.59:
        hora = ajuste(hora)
    ponteiros(hora)

code()
