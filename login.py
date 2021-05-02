import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import Entry
import psycopg2
from psycopg2 import Error

def Login():

    Email = entry2.get()
    password = entry3.get()
    
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()

        create_table_query = '''SELECT * FROM users WHERE mail=%s;'''

        cursor.execute(create_table_query, (Email,))

        result = cursor.fetchall()

        contrasena = ""
        
        for row in result:
            contrasena = row[13]

        if (password == contrasena):
            ventanaMenuUsuario()
            print("Usuario y contraseña correcta")
            
        else:
            print("El email o contraseña es invalido")
            
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error :
        print ("Email no registrado", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    if(password == contrasena):
        print("Entro")
    else:
        try:
            connection = psycopg2.connect(user = "postgres",
                                          password = "123456",
                                          host = "127.0.0.1",
                                          port = "5433",
                                          database = "proyecto")
            cursor = connection.cursor()

            create_table_query = '''SELECT * FROM users WHERE mail=%s;'''

            cursor.execute(create_table_query, (Email,))

            result = cursor.fetchall()
            
            contrasena = ""

            for row in result:
                contrasena = row[15]
            print(contrasena, password)
            
            if (password == contrasena):
                ventanaMenu()
                print("Usuario y contraseña correcta")
                

                
            else:
                print("El email o contraseña es invalido")
                
            connection.commit()

        except (Exception, psycopg2.DatabaseError) as error :
            print ("Email no registrado", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

def crearUsuario(customerid, firstname, lastname, email, password):
    try:
    
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()

        create_table_query = '''INSERT INTO users(customerid, firstname, lastname, email, password) VALUES(%s, %s, %s, %s, %s);'''
            
        cursor.execute(create_table_query, (customerid, firstname, lastname, email, password,))

        connection.commit()
            
        messagebox.showinfo(message="Se ha registrado el cliente exitosamente.", title="Registro")

    
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar cliente.", title="Consulta fallida")
        print ("No se pudo registrar cliente.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def Signup():

    signup = tk.Tk()
    signup.title("Sign Up")
    signup.geometry("800x600")
    signup.configure(background="sky blue")

    label4= tk.Label(signup, text="Nuevo Usuario", font=("Century", 44), pady=40, bg="sky blue", fg="black")
    label4.pack()


    #NOMBRE

    nombre = tk.Frame(signup, bg="sky blue")
    label5 = tk.Label(nombre, text="Nombre: ", font=("Courier", 15), bg="sky blue", fg="black")
    label5.pack()

    entry5 = Entry(nombre)
    entry5.pack()
    nombre.pack()

    #APELLIDO

    apellido = tk.Frame(signup, bg="sky blue")
    label6 = tk.Label(apellido, text="Apellido: ", font=("Courier", 15), bg="sky blue", fg="black")
    label6.pack()

    entry6 = Entry(apellido)
    entry6.pack()
    apellido.pack()

    #EMAIL

    correo = tk.Frame(signup, bg="sky blue")
    label15 = tk.Label(correo, text="Email: ", font=("Courier", 15), bg="sky blue", fg="black")
    label15.pack()

    entry15 = Entry(correo)
    entry15.pack()
    correo.pack()

    #CONTRASEÑA

    con = tk.Frame(signup, bg="sky blue")
    label16 = tk.Label(con, text="Contraseña: ", font=("Courier", 15), bg="sky blue", fg="black")
    label16.pack()

    entry16 = Entry(con, show = "*")
    entry16.pack()
    con.pack()

    #CustumerId

    usuarioId = tk.Frame(signup, bg="sky blue")
    label17 = tk.Label(usuarioId, text="usuarioId: ", font=("Courier", 15), bg="sky blue", fg="black")
    label17.pack()

    entry17 = Entry(usuarioId)
    entry17.pack()
    usuarioId.pack()

    def registrarUsuario():
        fName = entry5.get()
        lName = entry6.get()
        password = entry16.get()
        custumerId = entry17.get()

        crearUsuario(custumerId, fName, lName, email, supportrepid, password)

    #BOTON REGISTRAR

    lbl = tk.Label(usuarioId, text="", font=("Courier", 15), bg="sky blue", fg="black")
    lbl.pack()
    registrarFrame = tk.Frame(signup, bg = "sky blue")
    button3 = tk.Button(registrarFrame, text = "SIGN UP", font = ("Courier", 15), command = registrarUsuario)
    button3.pack()
    registrarFrame.pack()

######
# MAIN 
######

gui = tk.Tk()
gui.title("Music")
gui.geometry("800x600")
gui.configure(background = "sky blue")

label1= tk.Label(gui, text="Music", font=("Century", 44), pady=40, bg="sky blue", fg="black")
label1.pack()

label2 = tk.Label(gui, text="Email:", font=("Courier", 15), bg="sky blue")
entry2 = Entry(gui)
label2.pack()
entry2.pack()

label3 = tk.Label(gui, text = "Constraseña:", font=("Courier", 15), bg="sky blue")
entry3 = Entry(gui, show="*")
label3.pack()
entry3.pack()

button1 = tk.Button(gui, text = "Log In", font=("Courier", 15), command=Login)
button1.pack(pady=10, ipadx=5)

button2 = tk.Button(gui, text="Sing Up", font=("Courier", 15), command=Signup)
button2.pack(pady=10)

gui.mainloop()
