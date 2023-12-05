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

    resultado_label.config(text=f"Total: ${round(total, 2)}")

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

resultado_label = ttk.Label(root, text="Total: $0.00", font=("Helvetica", 14, "bold"))

# Organizar widgets en la ventana
producto_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
producto_entry.grid(row=0, column=1, padx=10, pady=10)

precio_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
precio_entry.grid(row=1, column=1, padx=10, pady=10)

cantidad_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
cantidad_entry.grid(row=2, column=1, padx=10, pady=10)

calcular_button.grid(row=3, column=0, columnspan=2, pady=10)

resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()