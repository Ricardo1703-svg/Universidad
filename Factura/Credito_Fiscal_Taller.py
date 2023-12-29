import tkinter as tk
from tkinter import ttk

def calcular_factura():
    producto = producto_var.get()
    precio = float(precio_var.get())
    cantidad = int(cantidad_var.get())

    precio_total = cantidad * precio
    precio_factura = precio_total / 1.13
    iva = precio_factura * 0.13
    total = precio_factura + iva

    precio_factura_label.config(text=f"Sumas: ${round(precio_factura, 2)}")
    iva_label.config(text=f"13% IVA: ${round(iva, 2)}")
    resultado_label.config(text=f"Venta Total: ${round(total, 3)}")    

# Crear la ventana principal
root = tk.Tk()
root.title("Factura de Crédito Fiscal")

# Variables de control
producto_var = tk.StringVar()
precio_var = tk.StringVar()
cantidad_var = tk.StringVar()

# Crear widgets
producto_label = ttk.Label(root, text="Producto:")
producto_entry = ttk.Entry(root, textvariable=producto_var)

precio_label = ttk.Label(root, text="Precio:")
precio_entry = ttk.Entry(root, textvariable=precio_var)

cantidad_label = ttk.Label(root, text="Cantidad:")
cantidad_entry = ttk.Entry(root, textvariable=cantidad_var)

calcular_button = ttk.Button(root, text="Calcular", command=calcular_factura)

precio_factura_label = ttk.Label(root, text="Sumas: $0.00", font=("Helvetica", 12, "bold"))
iva_label = ttk.Label(root, text="13% IVA: $0.00", font=("Helvetica", 12, "bold"))
resultado_label = ttk.Label(root, text="Venta Total: $0.00", font=("Helvetica", 14, "bold"))

# Organizar widgets en la ventana
producto_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
producto_entry.grid(row=0, column=1, padx=10, pady=10)

precio_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
precio_entry.grid(row=1, column=1, padx=10, pady=10)

cantidad_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
cantidad_entry.grid(row=2, column=1, padx=10, pady=10)

calcular_button.grid(row=3, column=0, columnspan=2, pady=10)

precio_factura_label.grid(row=4, column=0, columnspan=2, pady=5)
iva_label.grid(row=5, column=0, columnspan=2, pady=5)
resultado_label.grid(row=6, column=0, columnspan=2, pady=10)


# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()