from cProfile import label
from dis import Instruction
from distutils.log import info
from importlib.resources import open_text
from operator import concat
from pickle import FRAME
import plistlib
from tkinter import * 
import tkinter as tk
from tkinter import font
from tkinter import filedialog
from unittest import TextTestResult
from tkinter import messagebox
from tkinter import Entry 
from tkinter import ttk
import sqlite3


def infoadicional():
    messagebox.showinfo("Family Help", "Hecho por Thomas Molina y Erwin Bañol")


def ayuda():
    messagebox.showinfo("Atencion al cliente", "Para brindarle una mejor asesoría comuniquese con el lider del grupo: thomas_molina23212@elpoli.edu.co") 


def ventana1():
    import encuetaalimentos
    encuetaalimentos 
    encuetaalimentos.mainloop()

def ventana2():
    import encuestaspersonas
    encuestaspersonas
    encuestaspersonas.mainloop()

def ventana3():
    def guardar_y_borrar_info():
        dato_nombre=nombrea.get()
        dato_apellido=apellidoa.get()
        dato_edad=edada.get()
        dato_alimento=alimentoa.get()
        dato_calimento=cantidadlimentoa.get()
        a1=varopcion1a.get()
        a2=varopcion2a.get()

        newfile=open("data.txt","a")
        newfile.write("Nombre:")
        newfile.write(dato_nombre)
        newfile.write("\t")
        newfile.write("Apellido:")
        newfile.write(dato_apellido)
        newfile.write("\t")
        newfile.write("Edad:")
        newfile.write(dato_edad)
        newfile.write("\t")
        newfile.write("Alimento:")
        newfile.write(dato_alimento)
        newfile.write("\t")
        newfile.write("cantidad De Alimento:")
        newfile.write(dato_calimento)
        newfile.write("\t")
        newfile.write("Sisben:")
        newfile.write(a2)
        newfile.write("\n")
        newfile.close
        nombre.delete(0,END)
        cuadroapellido.delete(0,END)
        cuadrocedula.delete(0,END)
        cuadroedad.delete(0,END)
        cuadroalimento.delete(0,END)
        cuadrocalimento.delete(0,END)
        
        
    win2=tk.Toplevel()
    win2.geometry('600x500')
    win2.resizable(False, False)
    win2.configure(background="#2e3192")
    win2.title("FamilyHelp")
    win2.iconbitmap("FHsimbolo.ico")
    
          
    nombre=Entry(win2, textvariable=nombrea)
    nombre.grid(row=0, column=1, padx=10, pady=10)
    cuadroapellido=Entry(win2, textvariable=apellidoa)
    cuadroapellido.grid(row=1, column=1, padx=10, pady=10)    
    cuadroedad=Entry(win2, textvariable=edada)
    cuadroedad.grid(row=1, column=3, padx=10, pady=10)
    cuadrocedula=Entry(win2, textvariable=direcciona)
    cuadrocedula.grid(row=2, column=1, padx=10, pady=10)
    cuadroalimento=Entry(win2, textvariable=alimentoa)
    cuadroalimento.grid(row=3, column=1, padx=10, pady=10)
    cuadrocalimento=Entry(win2, textvariable=cantidadlimentoa)
    cuadrocalimento.grid(row=4, column=1, padx=10, pady=10)
    
    fotosisben = PhotoImage(file="sisben.png")
     
    # c=Entry(win2, text="Masculino", variable=varopcion1a, value="Masculino",  padx=10, pady=10)
    # cuadroalimento.grid(row=4, column=1)
    # femenino=Radiobutton(win2, text="Femenino", variable=varopcion1a, value="Femenino", padx=10, pady=10)
    # femenino.grid(row=5, column=1)
    a=Radiobutton(win2, text="SISBÉN A", variable=varopcion2a, value="A",  padx=10, pady=10)
    a.grid(row=8, column=1)
    b=Radiobutton(win2, text="SISBÉN B", variable=varopcion2a, value="B",  padx=10, pady=10)
    b.grid(row=9, column=1)
    c=Radiobutton(win2, text="SISBÉN C", variable=varopcion2a, value="C",  padx=10, pady=10)
    c.grid(row=10, column=1)
    
    nombrelabel=Label(win2, text="Nombre:")
    nombrelabel.grid(row=0, column=0, sticky="e",pady=10)
    apellidolabel=Label(win2, text="Apellido:")
    apellidolabel.grid(row=1, column=0,sticky="e",pady=10)
    edadlabel=Label(win2, text="Edad:")
    edadlabel.grid(row=1, column=2,sticky="e",pady=10)
    cedulalabel=Label(win2, text="Numero De Cedula:")
    cedulalabel.grid(row=2, column=0,sticky="e",pady=10)
    fotosisben1=Label(win2, image=fotosisben, bg="#2e3192")
    fotosisben1.grid(row=7, column=1)
    Label(win2, text="Cantidad De Alimento:").grid(row=4, column=0, sticky="e",pady=10)
    Label(win2, text="Tipo De Alimento:").grid(row=3, column=0, sticky="e",pady=10)
    Label(win2, text="Tipo de sisbén:").grid(row=7, column=0, sticky="e",pady=10)
    
    barramenu=Menu(win2)
    win2.config(menu=barramenu, width=300, height=300)
    archivoayuda=Menu(barramenu, tearoff=0)
    archivoayuda.add_command(label="Licencia", command=infoadicional)
    archivoayuda.add_command(label="Acerca de...", command=ayuda)
    barramenu.add_cascade(label="Ayuda", menu=archivoayuda)
    boton1=tk.Button(win2,text="Continuar", command=(guardar_y_borrar_info),bg="#0071bc", fg="white",width="20", height="1",)
    boton1.grid(row=11, column=4, sticky="w")
    win2.mainloop()    

def ventana4():
    import Archivos
    Archivos
def ventana5():
    import encuestapersonas2
    encuestapersonas2     
def ventana6():
    win4=tk.Toplevel()
    win4.geometry('1000x500')
    win4.configure(background="#2e3192")
    
    scroll=tk.Scrollbar(win4)
    InfoMod1=tk.Text(win4, height=60, width=300)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    InfoMod1.pack(side=tk.LEFT, fill=tk.Y)
    scroll.config(command=InfoMod1.yview)
    InfoMod1.config(yscrollcommand=scroll.set)
    Infinal="""
    La aplicación Family Help es una aplicación de escritorio que permite a los usuarios recolectar dos tipos de datos, 
    los alimentos que se van a ingresar y los otros datos que se pueden recolectar en la encuesta que se le hace 
    a las personas, para si hacer dos listas . Donde la persona 
    puede corregir y borrar la lista.
    
    El primer botón es el botón llamado Alimentos, donde se elegirá dos tipos de opciones de alimentos:
    
    -Alimentos no perecederos como atún, frijoles, garbanzos, etc. Por motivos externos al proyecto.
    se tuvo que globalizar todo este tipo de alimentos a un solo nombre.
    
    -Agua o líquidos. Donde estos pueden ser líquidos como agua, gaseosas, jugos en cajas o botellas con largas fechas 
    de vencimiento. 
    
    Cuando se da click en continuar en las dos encuestas la página se reinicia y guarda los datos escritos en 
    dichos campos requeridos., para así volver a digitar dichos campos. No es necesario de pulsar click en continuar 
    dos veces porque así se repetirá la información que se desea guardar. 
    """
    InfoMod1.insert(tk.END, Infinal)
    win4.title("FamilyHelp")
    win4.iconbitmap("FHsimbolo.ico")
    barramenu=Menu(win4)
    win4.config(menu=barramenu, width=300, height=300)
    archivoayuda=Menu(barramenu, tearoff=0)
    archivoayuda.add_command(label="Licencia", command=infoadicional)
    archivoayuda.add_command(label="Acerda de...", command=ayuda)
    barramenu.add_cascade(label="Ayuda", menu=archivoayuda)


    
if __name__=="__main__":
    raiz=Tk    
    raiz = tk.Tk()
    raiz.geometry()
    raiz.resizable(True, True)
    raiz.title("FamilyHelp")
    raiz.iconbitmap("FHsimbolo.ico")
    raiz.config(bg="#2e3192")

    fhframe = Frame(raiz,width=1000, height=2000)
    fhframe.pack(fill="both", expand=True)
    fhframe.config(bg="#2e3192")
    FHimage = PhotoImage(file="FamilyHelp222.png")
    mlabel = Label(fhframe, image = FHimage,bg="#2e3192").pack(pady=2)
    tex=Label(fhframe, text="MENÚ",bg="#2e3192", fg="white", font=('Arial', 25, "bold" )).pack(pady=4)
    boton1=tk.Button(fhframe,text="Alimentos",bg="#0071bc", fg="white", command=ventana1,width="20", height="1", font=('Arial', 15, "bold" )).pack(pady=5)
    boton2=tk.Button(fhframe,text=" Registro de Familias",bg="#0071bc", fg="white", command=ventana2,width="20", height="1", font=('Arial', 15, "bold" )).pack(pady=6)
    boton3=tk.Button(fhframe,text=" Registrar  ",bg="#0071bc", fg="white", command=ventana3,width="20", height="1", font=('Arial', 15, "bold" )).pack(pady=7)
    boton4=tk.Button(fhframe,text="Cuadros",bg="#0071bc", fg="white", command=ventana5,width="20", height="1", font=('Arial', 15, "bold" )).pack(pady=9)
    boton5=tk.Button(fhframe,text="Buscar",bg="#0071bc", fg="white", command=ventana4,width="20", height="1", font=('Arial', 15, "bold" )).pack(pady=8)
    boton6=tk.Button(fhframe,text="Informacion",bg="#0071bc", fg="white", command=ventana6,width="20", height="1", font=('Arial', 15, "bold" )).pack(pady=10)

    barramenu=Menu(raiz)
    raiz.config(menu=barramenu, width=300, height=300)
        
    archivoayuda=Menu(barramenu, tearoff=0)
    archivoayuda.add_command(label="Licencia", command=infoadicional)
    archivoayuda.add_command(label="Acerda de...", command=ayuda)
    barramenu.add_cascade(label="Ayuda", menu=archivoayuda)
    alimentosoliquidosa=StringVar()
    aguaoliquidosa=StringVar()
    nombrea=StringVar()
    apellidoa=StringVar()
    edada=StringVar()
    direcciona=StringVar()
    alimentoa=StringVar()
    cantidadlimentoa=StringVar()
    varopcion1a=StringVar()
    varopcion2a=StringVar()
    raiz.mainloop()

