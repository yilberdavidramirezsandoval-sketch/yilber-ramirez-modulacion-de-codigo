def asignar():
    producto = int(input("que producto lleva:"))
    return producto
def cantidad_pedidos():
    cantidad = int(input("cuantos productos son:"))
    return cantidad 
def procesar(cantidad):
    total = 0
    cont = 0
    for n in range(cantidad):
        print("calificacion del pedido:")
        calificacion = int(input("del 1 al 5"))
        if calificacion > 5:
            calificacion = 5
        if calificacion < 1:
            calificacion = 1
        if calificacion == 5:
            print("excelente")
        total = total + calificacion
        cont = cont + 1
    return total,cont
def hacer_calculo(total, cont):
    if cont > 0:
        promedio = total / cont
    else:
        promedio = 0
def mostrar_resultado(promedio):
    print("el promedio es:"+ str(promedio))
    
#********************codigo principal*****************
producto = asignar()
cantidad = cantidad_pedidos()
total, cont = procesar(cantidad)
promedio = hacer_calculo(total,cont)
mostrar_resultado(promedio)