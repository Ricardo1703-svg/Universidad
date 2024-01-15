import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def submit():
    total = float(precio.get()) * float(cantidad.get())
    print("Cliente: ", cliente.get())
    print("Fecha: ", fecha.get())
    print("No. de Factura: ", factura.get())
    print("Producto: ", producto.get())
    print("Cantidad: ", cantidad.get())
    print("Precio: ", precio.get())
    print("Total: ", total)
    
    c = canvas.Canvas("factura.pdf", pagesize=letter)
    width, height = letter
    c.drawString(50, height - 50, "Cliente: " + cliente.get())
    c.drawString(50, height - 70, "Fecha: " + fecha.get())
    c.drawString(50, height - 90, "No. de Factura: " + factura.get())
    c.drawString(50, height - 110, "Producto: " + producto.get())
    c.drawString(50, height - 130, "Cantidad: " + cantidad.get())
    c.drawString(50, height - 150, "Precio: " + precio.get())
    c.drawString(50, height - 170, "Total: " + str(total))
    c.save()

root = tk.Tk()
root.title("Formulario de Factura")

cliente = tk.StringVar()
fecha = tk.StringVar()
factura = tk.StringVar()
producto = tk.StringVar()
cantidad = tk.StringVar()
precio = tk.StringVar()

ttk.Label(root, text="Cliente:").grid(row=0, column=0, padx=10, pady=10)
ttk.Entry(root, textvariable=cliente).grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Fecha:").grid(row=1, column=0, padx=10, pady=10)
ttk.Entry(root, textvariable=fecha).grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="No. de Factura:").grid(row=2, column=0, padx=10, pady=10)
ttk.Entry(root, textvariable=factura).grid(row=2, column=1, padx=10, pady=10)

ttk.Label(root, text="Producto:").grid(row=3, column=0, padx=10, pady=10)
ttk.Entry(root, textvariable=producto).grid(row=3, column=1, padx=10, pady=10)

ttk.Label(root, text="Cantidad:").grid(row=4, column=0, padx=10, pady=10)
ttk.Entry(root, textvariable=cantidad).grid(row=4, column=1, padx=10, pady=10)

ttk.Label(root, text="Precio:").grid(row=5, column=0, padx=10, pady=10)
ttk.Entry(root, textvariable=precio).grid(row=5, column=1, padx=10, pady=10)

ttk.Button(root, text="Enviar", command=submit).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()