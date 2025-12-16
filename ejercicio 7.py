# Verificación de Cumplimiento de Metas de Ventas
meta_ventas = 5000
vendedores_con_meta = 0
total_vendedores = 0
felicitaciones = []

while True:
    venta = float(input("Ingrese el monto de ventas del vendedor (0 o negativo para salir): $"))
    
    if venta <= 0:
        break
    
    total_vendedores += 1
    
    if venta >= meta_ventas:
        vendedores_con_meta += 1
        felicitaciones.append(f"Vendedor {total_vendedores}: ¡Felicitaciones! Meta cumplida con ${venta}")
    else:
        felicitaciones.append(f"Vendedor {total_vendedores}: Falta ${meta_ventas - venta} para cumplir la meta")

print("\n--- REPORTE DE VENTAS ---")
print(f"Total de vendedores procesados: {total_vendedores}")
print(f"Vendedores con meta cumplida: {vendedores_con_meta}")
if total_vendedores > 0:
    porcentaje = (vendedores_con_meta / total_vendedores) * 100
    print(f"Porcentaje de cumplimiento: {porcentaje:.1f}%")
print("\n--- DETALLES ---")
for felicitacion in felicitaciones:
    print(felicitacion)