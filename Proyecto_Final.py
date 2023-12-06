import serial
import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from time import strftime
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas

ser = serial.Serial('COM5', 9600)
client = MongoClient("mongodb://Ricardo:root2023@localhost:27017/?authMechanism=DEFAULT")
db = client["Arduino"]
collection = db["TemperaturayHumedad_SanMiguel"]

# Funcion para Recibir e imprimir los datos desde el arduino
def actualizar_etiqueta():
    data = ser.readline().decode('utf-8').rstrip()
    etiqueta.config(text="Dato recibido: " + data)
    root.after(1000, actualizar_etiqueta)

# Funcion para imprimir la fecha y hora en tiempo real
def actualizar_hora():
    string_hora = strftime('%H:%M:%S %p')
    etiqueta_hora.config(text=string_hora)
    string_fecha = strftime('%d/%m/%Y')
    etiqueta_fecha.config(text=string_fecha)
    root.after(1000, actualizar_hora)

def Guardar_Datos():
    Datos_Arduino = ser.readline().decode('utf-8').rstrip()
    Datos_Hora = strftime('%H:%M:%S %p')
    Datos_Fecha = strftime('%d/%m/%Y')
    documento = {"Datos": Datos_Arduino, "Fecha": Datos_Fecha,"Hora": Datos_Hora}
    result = collection.insert_one(documento)
    messagebox.showinfo("Genial", f"Documento insertado con id: {result.inserted_id}!")

def buscar_Datos():
    resultados.delete(0, tk.END)
    for doc in collection.find():
        resultados.insert(tk.END, f"Datos: {doc['Datos']}, Fecha: {doc['Fecha']}, Hora: {doc['Hora']}")

def generar_PDF():
    pdf_filename = "Datos_Sensores.pdf"
    c = canvas.Canvas(pdf_filename)
    
    c.drawString(100, 800, "Datos Recopilados:")
    
    y_position = 780
    for doc in collection.find():
        data_str = f"Datos: {doc['Datos']}, Fecha: {doc['Fecha']}, Hora: {doc['Hora']}"
        c.drawString(100, y_position, data_str)
        y_position -= 20
    
    c.save()
    messagebox.showinfo("Genial", f"PDF generado: {pdf_filename}")

# Diseño de Ventana
root = tk.Tk()
root.title("Datos desde Arduino")
root.geometry("1250x720")

# Cargar la imagen de fondo
background_image = Image.open("Fondo Ard.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Elementos de la GUI
# -----------------------------------------Hora-----------------------------------------------------
etiqueta_hora = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
etiqueta_hora.place(x=450,y=10)
# -----------------------------------------Fecha------------------------------------------------------
etiqueta_fecha = tk.Label(root, font=('calibri', 30, 'bold'), background='red', foreground='black')
etiqueta_fecha.place(x=500,y=90)
# ----------------------------------------------Arduino-------------------------------------------------------------------
etiqueta = tk.Label(root, text="Esperando datos...", font=('calibri', 26, 'bold'), background='black', foreground='white')
etiqueta.place(x=250,y=200)

# Actualización de los datos
actualizar_etiqueta()
actualizar_hora()

def cerrar_ventana():
    ser.close()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", cerrar_ventana)

insertar_button = tk.Button(root, text="Guardar", command=Guardar_Datos, bg="#8bff82", font=("Arial Black", 11))
insertar_button.place(x=500, y=300)

buscar_button = tk.Button(root, text="Consultar", command=buscar_Datos, bg="#07FBEF", font=("Arial Black", 11))
buscar_button.place(x=620, y=300)

generar_pdf_button = tk.Button(root, text="Generar PDF", command=generar_PDF, bg="#FFD700", font=("Arial Black", 11))
generar_pdf_button.place(x=750, y=300)

resultados = tk.Listbox(root, width=72, height=10, font=("Arial Black", 10), fg="black")
resultados.place(x=350, y=400)
resultados.configure(bg="#D3D3D3")

# Iniciar el bucle principal de Tkinter
root.mainloop()

