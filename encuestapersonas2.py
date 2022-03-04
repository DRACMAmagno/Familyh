from cProfile import label
from tkinter import * 
import tkinter as tk
from tkinter import Entry 
from tkinter import ttk
import sqlite3 

class Product():

    # connection dir property
    db_name1 = 'database.db'
    db_name2 = 'databasecomida.db'

    def __init__(self,win2):
        # Initializations 
        # def guardar_y_borrar_info():
        #     dato_nombre=nombrea.get()
        #     dato_apellido=apellidoa.get()
        #     dato_edad=edada.get()
        #     dato_alimento=alimentoa.get()
        #     dato_calimento=cantidadlimentoa.get()
        #     a1=varopcion1a.get()
        #     a2=varopcion2a.get()

        #     newfile=open("data.txt","a")
        #     newfile.write("Nombre:")
        #     newfile.write(dato_nombre)
        #     newfile.write("\t")
        #     newfile.write("Apellido:")
        #     newfile.write(dato_apellido)
        #     newfile.write("\t")
        #     newfile.write("Edad:")
        #     newfile.write(dato_edad)
        #     newfile.write("\t")
        #     newfile.write("Alimento:")
        #     newfile.write(dato_alimento)
        #     newfile.write("\t")
        #     newfile.write("cantidad De Alimento:")
        #     newfile.write(dato_calimento)
        #     newfile.write("\t")
        #     newfile.write("Sisben:")
        #     newfile.write(a2)
        #     newfile.write("\n")
        #     newfile.close
        #     nombre.delete(0,END)
        #     cuadroapellido.delete(0,END)
        #     cuadrocedula.delete(0,END)
        #     cuadroedad.delete(0,END)
        #     cuadroalimento.delete(0,END)
        #     cuadrocalimento.delete(0,END)
        #     mainloop()

        
    
        self.wind = win2
        self.wind.title('Encuesta De Personas')
        
        nombrea=StringVar()
        apellidoa=StringVar()
        edada=StringVar()
        direcciona=StringVar()
        alimentoa=StringVar()
        cantidadlimentoa=StringVar()
        varopcion1a=StringVar()
        varopcion2a=StringVar()
        frame = LabelFrame(self.wind)
        Label(frame, text = 'Nombre: ')
        self.name = Entry(frame)
        self.name.focus()
        Label(frame, text = 'Apellidos: ')
        self.apellido = Entry(frame)
        self.cedula = Entry(frame)
        Label(frame, text = 'Tipo de sisbén: ')
        self.sisben = Entry(frame)
        Label(frame, text = 'Número de integrantes: ')
        self.edad = Entry(frame)
        
        Label(frame, text = 'Nombre: ')
        self.name1 = Entry(frame)
        self.name1.focus()
        Label(frame, text = 'Cantidad: ')
        self.price = Entry(frame)
        self.message = Label(win2,text = '', fg = 'red')
        

        # self.tree1 = ttk.Treeview(win2,height = 10, columns = (2))
        # self.tree1.grid()
        # self.tree1.heading('#0', text = 'Nombre', anchor = CENTER)
        # self.tree1.heading('#01', text = 'Cantidad', anchor = CENTER)
    

        ttk.Button(frame, text = 'Guardar Encuesta', command = self.add_product)
        self.message = Label(win2,text = '', fg = 'red')
        self.tree = ttk.Treeview(win2,height = 9, column = 0, columns = ("1","2","3","4"))
        self.tree.pack()
        self.tree.column = ("#1")
        self.tree.column = ("#2")
        self.tree.column = ("#3")
        self.tree.column = ("#4")
        self.tree.heading("#0" ,text = 'Nombre',anchor= CENTER)
        self.tree.heading("1", text = 'Apellido',anchor= CENTER)
        self.tree.heading("2", text = 'Cédula',anchor= CENTER)
        self.tree.heading("3", text = 'Sisbén',anchor= CENTER)
        self.tree.heading("4", text = 'Integrantes',anchor= CENTER) 
        self.get_products()

        self.tree1 = ttk.Treeview(win2,height = 10, columns = (2))
        self.tree1.pack()
        self.tree1.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree1.heading('#01', text = 'Cantidad', anchor = CENTER)
        self.get_products1()
        
       
        mainloop()
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name1) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def run_query1(self, query1, parameters = ()):
        with sqlite3.connect(self.db_name2) as conn:
            cursor = conn.cursor()
            result1 = cursor.execute(query1, parameters)
            conn.commit()
        return result1    


    def get_products(self):
        
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        
        query = 'SELECT * FROM product ORDER BY sisben,edad'
        db_rows = self.run_query(query)
        
        for row in db_rows:
            self.tree.insert('', tk.END,text=row[0],values=(row[1:5]))


    
    def validation(self):
        return len(self.name.get()) != 0 and len(self.apellido.get()) != 0 and len(self.cedula.get()) != 0 and len(self.sisben.get()) != 0 and len(self.edad.get()) != 0 
        

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(?,?,?,?,?)'
            parameters =  (self.name.get(), self.apellido.get(),self.cedula.get(), self.sisben.get(), self.edad.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Familia {} Añadida Satisfactoriamente'.format(self.name.get())
            self.name.delete(0, END)
            self.apellido.delete(0, END)
            self.cedula.delete(0, END)
            self.sisben.delete(0, END)
            self.edad.delete(0, END)
            
        else:
            self.message['text'] = 'Nombre y Apellidos Son Requeridos'
        self.get_products()
        

    def delete_product(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name,))
        self.message['text'] = 'Record {} deleted Successfully'.format(name)
        self.get_products()

        

    def edit_product(self):
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            return
        old_name = self.tree.item(self.tree.selection())['values']
        old_apellido = self.tree.item(self.tree.selection())['values'][0]
        old_sisben = self.tree.item(self.tree.selection())['values'][1]
        old_cedula = self.tree.item(self.tree.selection())['values'][2]
        old_edad = self.tree.item(self.tree.selection())['values'][3]

        self.edit_wind = Toplevel(win2)
        self.edit_wind.title = 'Edit Product'
        # Old Name
        Label(self.edit_wind, text = 'Viejo Nombre:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_name), state = 'readonly').grid(row = 0, column = 2)
        # New Name
        Label(self.edit_wind, text = 'Nuevo Nombre:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)


        # Old last name 
        Label(self.edit_wind, text = 'Viejo Apellido:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_apellido), state = 'readonly').grid(row = 2, column = 2)
        # New last name
        Label(self.edit_wind, text = 'Nuevo Apellido:').grid(row = 3, column = 1)
        new_apellido= Entry(self.edit_wind)
        new_apellido.grid(row = 3, column = 2)

        # Old id
        Label(self.edit_wind, text = 'Vieja Cédula:').grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_cedula), state = 'readonly').grid(row = 4, column = 2)
        # New id
        Label(self.edit_wind, text = 'Nueva Cédula:').grid(row = 5, column = 1)
        new_cedula= Entry(self.edit_wind)
        new_cedula.grid(row = 5, column = 2)

        # Old sisben
        Label(self.edit_wind, text = 'Viejo Sisbén:').grid(row = 6, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_sisben), state = 'readonly').grid(row = 6, column = 2)
        # New sisben
        Label(self.edit_wind, text = 'Nuevo Sisbén:').grid(row = 7, column = 1)
        new_sisben= Entry(self.edit_wind)
        new_sisben.grid(row = 7, column = 2)

        # Old age
        Label(self.edit_wind, text = 'Vieja Edad:').grid(row = 8, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_edad), state = 'readonly').grid(row = 8, column = 2)
        # New age
        Label(self.edit_wind, text = 'Nueva Edad:').grid(row = 9, column = 1)
        new_edad= Entry(self.edit_wind)
        new_edad.grid(row = 9, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_name.get(), old_name, new_apellido.get(), old_apellido,new_cedula.get(), old_cedula,new_sisben.get(), old_sisben, new_edad.get(), old_edad)).grid(row = 10, column = 2, sticky = W)
        self.edit_wind.mainloop()
        

    # def run_query1(self, query1, parameters = ()):
    #     with sqlite3.connect(self.db_name2) as conn:
    #         cursor = conn.cursor()
    #         result1 = cursor.execute(query1, parameters)
    #         conn.commit()
    #     return result1

    def get_products1(self):

        records1 = self.tree1.get_children()
        for element in records1:
            self.tree1.delete(element)

        query1 = 'SELECT * FROM product ORDER BY name DESC,price'
        db_rows1 = self.run_query1(query1)
        for row in db_rows1:
            self.tree1.insert('', 0, text = row[1], values = row[2])


    def validation1(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product1(self):
        if self.validation():
            query1 = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters =  (self.name.get(), self.price.get())
            self.run_query(query1, parameters)
            self.message['text'] = 'Product {} added Successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Nambre y Precio es Requirido'
        self.get_products1()

    def delete_product1(self):
        self.message['text'] = ''
        try:
           self.tree1.item(self.tree1.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccionar Lote'
            return
        self.message['text'] = ''
        name = self.tree1.item(self.tree1.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query1(query, (name, ))
        self.message['text'] = 'Lote {} Borrado Exitosamente'.format(name)
        self.get_products1()

    def edit_product1(self):
        self.message['text'] = ''
        try:
            self.tree1.item(self.tree1.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccionar Lote'
            return
        name = self.tree1.item(self.tree1.selection())['text']
        old_price = self.tree1.item(self.tree1.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Lote'
        Label(self.edit_wind, text = 'Antiguo Nombre:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)
        Label(self.edit_wind, text = 'Nuevo Nombre:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)
        Label(self.edit_wind, text = 'Antiguo Lote:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)
        Label(self.edit_wind, text = 'Nuevo Lote:').grid(row = 3, column = 1)
        new_price= Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)
        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records1(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)
        self.edit_wind.mainloop()
    
    def edit_records1(self, new_name, name, new_price, old_price):
        query1 = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters = (new_name, new_price,name, old_price)
        self.run_query1(query1, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfylly'.format(name)
        self.get_products()

   

win2=Tk
win2 = tk.Tk()
win2.iconbitmap("FHsimbolo.ico")
win2.config(bg="#2e3192")
application = Product(win2)
