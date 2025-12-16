def definir_unidades():
    unidades = int(input("digite la cantidad de unidades del lote: "))
    return unidades
def definir_estado():
    estado = input("estado (D defectuosa / O ok) :")
    return estado
def hacer_proceso():
    defectuosas = 0
    ok = 0
    seguir = input("digite stop para terminar o enter para continuar: ")

    while seguir != "stop":
        unidades = definir_unidades()

        contador = 0
        while contador < unidades:
            estado = definir_estado()

            if estado == "D":
                defectuosas = defectuosas + 1
            else:
                if estado == "O":
                    ok = ok + 1
                else:
                    print("Estado inválido")
                    contador = contador - 1

            contador = contador + 1

        seguir = input("digite stop para terminar o ente para continuar: ")

    return defectuosas, ok

def mostrar(defectuosas, ok):
    total = defectuosas + ok

    if total > 0:
        porcentaje = (defectuosas * 100) / total
    else:
        porcentaje = 0

    print("defectuosa", defectuosas)
    print("ok:", ok)
    print("porcentaje defectuosa ", porcentaje)
d, o = hacer_proceso()
mostrar(d, o)