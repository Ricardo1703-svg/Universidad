def calcular_factura():
    total = 0
    iva = 0.13  # Tasa de IVA en El Salvador

    # Inicializar el diccionario de productos
    productos = {}

    # Solicitar la entrada de productos y cantidades al usuario
    while True:
        producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            break

        try:
            precio = float(input(f"Ingrese el precio del {producto}: $"))
            cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        # Calcular el precio total del producto (precio * cantidad)
        precio_total = precio * cantidad

        # Agregar el producto al diccionario
        productos[producto] = {"precio_unitario": precio, "cantidad": cantidad, "precio_total": precio_total}

        # Actualizar el total de la factura
        total += precio_total

    # Calcular impuesto (IVA)
    impuesto = total * iva

    # Calcular total con impuesto
    total_con_impuesto = total + impuesto

    # Imprimir encabezado de la factura
    print("\n------------------------")
    print("   Factura de Crédito Fiscal")
    print("------------------------")

    # Imprimir detalles de los productos o servicios
    for producto, detalles in productos.items():
        print(f"{producto} x{detalles['cantidad']}: ${detalles['precio_unitario']:.2f} c/u - Total: ${detalles['precio_total']:.2f}")

    # Imprimir resumen
    print("------------------------")
    print(f"Total: ${total:.2f}")
    print(f"IVA ({iva*100}%): ${impuesto:.2f}")
    print(f"Total con IVA: ${total_con_impuesto:.2f}")
    print("------------------------\n")


# Ejemplo de uso
calcular_factura()