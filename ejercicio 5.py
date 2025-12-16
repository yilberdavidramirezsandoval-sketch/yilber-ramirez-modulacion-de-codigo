def definir_precio():
    precio = float(input("digite el precio del producto: "))
    return precio
def definir_cantidad():
    cantidad = int(input("digite la cantidad: "))
    return cantidad
def procesar_compra():
    subtotal = 0
    seguir = input("agregar producto (si/no): ")
    while seguir != "no":
        precio = definir_precio()
        cantidad = definir_cantidad()
        subtotal = subtotal + (precio * cantidad)
        seguir = input("agregar otro producto (si/no): ")
    return subtotal
def hacer_calculo_descuento(subtotal):
    if subtotal > 1000:
        descuento = subtotal * 0.10
    else:
        if subtotal > 500:
            descuento = subtotal * 0.05
        else:
            descuento = 0
    total = subtotal - descuento
    return total, descuento
def mostrar_total(total, descuento):
    print("descuento aplicado:", descuento)
    print("monto final a pagar:", total)
subtotal = procesar_compra()
total, descuento = hacer_calculo_descuento(subtotal)
mostrar_total(total, descuento)