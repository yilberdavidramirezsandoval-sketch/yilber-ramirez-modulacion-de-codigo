def definir_cpu():
    cpu = float(input("uso de cpu :"))
    return cpu
def hacer_proceso_cpu():
    alertas = 0
    mediciones = 0
    uso = definir_cpu()
    while uso >= 0:
        mediciones = mediciones + 1
        if uso > 90:
            print("alerta uso critico")
            alertas = alertas + 1
        uso = definir_cpu()
    return alertas, mediciones

def mostrar_cpu(alertas, mediciones):
    print("total de medicione", mediciones)
    print("alerta critica", alertas)


#******************** codigo principal******************
alertas, mediciones = hacer_proceso_cpu()
mostrar_cpu(alertas, mediciones)