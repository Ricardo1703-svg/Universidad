import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from time import strftime
from fpdf import FPDF  # Añade esta importación para trabajar con PDF
import serial

ser = serial.Serial('COM5', 9600)

client = MongoClient("mongodb://Ricardo:root2023@localhost:27017/?authMechanism=DEFAULT")
db = client["Arduino"]
collection = db["TemperaturayHumedad"]

def actualizar_etiqueta():
    data = ser.readline().decode('utf-8').rstrip()
    etiqueta.config(text="Dato recibido: " + data)
    root.after(1000, actualizar_etiqueta)

def actualizar_hora():
    string_hora = strftime('%H:%M:%S %p')
    etiqueta_hora.config(text=string_hora)
    string_fecha = strftime('%d/%m/%Y')
    etiqueta_fecha.config(text=string_fecha)
    root.after(1000, actualizar_hora)

def guardar_datos():
    datos_arduino = ser.readline().decode('utf-8').rstrip()
    datos_hora = strftime('%H:%M:%S %p')
    datos_fecha = strftime('%d/%m/%Y')
    documento = {"Datos": datos_arduino, "Fecha": datos_fecha, "Hora": datos_hora}
    result = collection.insert_one(documento)
    messagebox.showinfo("Genial", f"Documento insertado con id: {result.inserted_id}!")

    # Mostrar resultados en una nueva ventana
    mostrar_resultados(datos_arduino, datos_hora, datos_fecha)

    # Generar un PDF con los resultados
    generar_pdf(datos_arduino, datos_hora, datos_fecha)

def mostrar_resultados(datos_arduino, datos_hora, datos_fecha):
    resultados_window = tk.Toplevel(root)
    resultados_window.title("Resultados")
    
    tk.Label(resultados_window, text=f"Datos Arduino: {datos_arduino}").pack()
    tk.Label(resultados_window, text=f"Hora: {datos_hora}").pack()
    tk.Label(resultados_window, text=f"Fecha: {datos_fecha}").pack()

def generar_pdf(datos_arduino, datos_hora, datos_fecha):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Resultados", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Datos Arduino: {datos_arduino}", ln=True)
    pdf.cell(200, 10, txt=f"Hora: {datos_hora}", ln=True)
    pdf.cell(200, 10, txt=f"Fecha: {datos_fecha}", ln=True)

    pdf_output_path = "resultados.pdf"
    pdf.output(pdf_output_path)
    messagebox.showinfo("Genial", f"PDF generado con éxito: {pdf_output_path}")

root = tk.Tk()
root.title("Datos desde Arduino")

# Resto del código...

# Botón para guardar datos
insertar_button = tk.Button(root, text="Guardar", command=guardar_datos, bg="#8bff82", font=("Arial Black", 11))
insertar_button.place(x=10, y=100)

# Cerrar la conexión serial al cerrar la ventana
def cerrar_ventana():
    ser.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Iniciar el bucle principal de Tkinter
root.mainloop()