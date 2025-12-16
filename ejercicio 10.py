def definir_horas():
    horas = int(input("digite las horas extra trabajadas: "))
    return horas
def proceso():
    total = 0
    empleado = 0
    horas = definir_horas()
    while horas >= 0:
        if horas > 5:
            bonificacion = horas * 15
            total = total + bonificacion
            empleado = empleado + 1
        else:
            if horas > 0:
                bonificacion = horas * 10
                total = total + bonificacion
                empleado = empleado + 1
        horas = definir_horas()
    return total, empleado
def mostrar(total, empleado):
    print("Bonificacion total:", total)
    print("Empleados con bonificacion:", empleado)
    
    total, empleado = proceso()