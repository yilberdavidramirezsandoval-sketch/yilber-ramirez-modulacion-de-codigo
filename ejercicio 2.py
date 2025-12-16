def definir_codigo():
    codigo = input("ingrese el codigo de identificacion:")
    return codigo
def rectificar_codigo(codigo, codigo_especial):
    if codigo == codigo_especial:
        return True
    else:
        return False
def procesar_accesos():
    codigo_especial = "2020"
    permitidos = 0
    denegados = 0
    while True:
        codigo = definir_codigo()
        if codigo == "salir":
            break
        if rectificar_codigo(codigo,codigo_especial):
            print("acceso permitido")
            permitidos = permitidos + 1
        else:
            print("acceso denegado")
            denegados = denegados + 1
    return permitidos, denegados
def mostrar_resultados(permitidos,denegados):
    print("accesso permitido",permitidos)
    print("acceso denegado",denegados)
permitidos , denegados= procesar_accesos()
mostrar_resultados(permitidos,denegados)