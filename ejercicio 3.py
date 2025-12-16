def definir():
     t = input("Tipo D deposito R retiro o FIN: ")
     return t
def monto():
    m = float(input("monto"))
    return m
def procesar():
    saldo = 1000
    transacciones = 0
    tipo = definir()
    while tipo != "FIN":
        if tipo == "D":
            m = monto()
            saldo = saldo + m
            transacciones = transacciones + 1
        else:
            if tipo == "R":
                m = monto()
                if saldo - m >= 0:
                    saldo = saldo - m
                    transacciones = transacciones + 1
                else:
                    print("no se puede retirar, saldo insuficiente")
            else:
                print("tipo no valido")

        tipo = definir()
    return saldo, transacciones
def mostrar(saldo, transacciones):
    print("saldo final:", saldo)
    print("transacciones validas:", transacciones)
saldo, transacciones = procesar()
mostrar(saldo, transacciones)