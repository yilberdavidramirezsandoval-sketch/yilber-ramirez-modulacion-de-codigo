# Control de Inventario con Reposición

stock_inicial = 50
punto_reposicion = 10
stock_actual = stock_inicial

print(f"Stock inicial: {stock_actual} unidades")
print(f"Punto de reposición: {punto_reposicion} unidades\n")

while True:
    try:
        cantidad_vendida = int(input("Ingrese cantidad vendida hoy (o 0 para salir): "))
        
        if cantidad_vendida == 0:
            print("Proceso finalizado.")
            break
        
        if cantidad_vendida > stock_actual:
            print(f"Error: No hay suficiente stock. Stock disponible: {stock_actual}\n")
            continue
        
        stock_actual -= cantidad_vendida
        print(f"Venta registrada: {cantidad_vendida} unidades")
        print(f"Stock actual: {stock_actual} unidades\n")
        
        if stock_actual <= punto_reposicion:
            print("  AVISO DE REPOSICIÓN URGENTE ")
            print(f"El stock ({stock_actual} unidades) está en o por debajo del punto de reposición ({punto_reposicion} unidades)")
            print("Se detiene el proceso de ventas.")
            break
        
    except ValueError:
        print("Por favor, ingrese un número válido.\n")