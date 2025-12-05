def pedir_producto():
    producto = int(input("que producto lleva:"))
    return producto
def cantidad_pedidos(producto):
    pedidos = int(input("digite la cantidad de pedidos:"))
    return pedidos
def prosesar_datos(pedidos):
    c=0
    for i in range (pedidos):
        calificacion = int (input("del 1 al 5 que calificacion le da el pedido"))
        if calificacion == 5:
            print ("exelente")
            c=c+calificacion
            sum = c
            return sum
def hacer_calculo(sum,pedidos):
    prom = sum/pedidos
    return prom
def mostrar_mensaje(prom):
    print("el promedio es" + str(prom))

#***************codigo principal***************+
producto = pedir_producto()
pedidos = cantidad_pedidos(producto)
sum = prosesar_datos(pedidos)
prom = hacer_calculo(producto, pedidos)
mostrar_mensaje(prom)


