import tkinter as tk 
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from test import ventana1


class aplicacion: 

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("FamilyHelp")
        self.ventana1.resizable(True, True)
        self.agregar_menu()
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=100, height=40)
        self.scrolledtext1.grid(column=0,row=0,padx=10,pady=10)
        self.ventana1.iconbitmap("FHsimbolo.ico")
        self.ventana1.mainloop()
    def agregar_menu(self):
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar", command=self.guardar)
        opciones1.add_command(label="Abrir", command=self.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)
        
    
    def salir(self):
        sys.exit(0)
    
    def guardar(self):
        nombrearch=fd.asksaveasfilename(initialdir="C:/Users/arequ/Downloads/Tkinter/Tkinter", title="guardar", filetypes=(("txt files","*txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w",encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("informacion", "los datos fueron guardados en el archivo")
           
    
    def recuperar(self):
        nombrearch=fd.askopenfilename(initialdir="C:/Users/arequ/Downloads/Tkinter/Tkinter", title="guardar", filetypes=(("txt files","*txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)
            
aplicacion1=aplicacion()

