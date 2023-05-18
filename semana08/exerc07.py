def ponteiros(hora,minuto):
    print(hora,":",minuto)

def ajuste(hora):
    hora -= 12
    return hora

def relogio():
    hora = input("Digite o horario: ")
    hora = hora.replace(",", ".").replace(":", ".").replace(";", ".")
    partes = hora.split(".")
    hora = int(partes[0])
    minuto = int(partes[1])
    return hora,minuto

def code():
    hora,minuto = relogio()
    if hora > 12:
        hora = ajuste(hora)
    ponteiros(hora,minuto)

code()
