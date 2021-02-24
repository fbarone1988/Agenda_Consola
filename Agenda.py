#%%
import os
import csv
import pandas as pd
from operator import itemgetter
import re

def email_valid(email):
   if(re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',email)):
       return True
   else:
        return False
    
try: 
    with open("Agenda.csv", "r") as archivo:
        lectura = csv.DictReader(archivo)
        contactos = list(lectura)
        contactos = sorted(contactos, key=itemgetter('Apellido'))
        df_contactos = pd.DataFrame(contactos) 
except:
    contactos = []   #Si no encuentra el archivo crea una lista vacía.
    
os.system("cls")
while True:
    print("Menu:")
    print(" 1 - Ingresar contacto")
    print(" 2 - Ver contactos")
    print(" 3 - Borrar contacto")
    print(" 4 - Modificar contacto")
    print(" 5 - Hacer backup")
    print(" 6 - Restaurar backup")
    print(" 7 - Salir")
    print("")
    opcion = input(">>> ")

    if opcion.isdecimal() == True: 
        opcion = int(opcion)
        if opcion == 1: #Ingresar contacto
            os.system("cls")
            apellido = input("Ingrese apellido: ")
            nombre = input("Ingrese nombre: ")
            telefono = input("Ingrese telefono: ")
            direccion = input("Ingrese direccion: ")
            email = input("Ingrese email: ")
            while email_valid(email) == False:
                email = input("Formato incorrecto. Ingrese email nuevamente: ") 
                
            Persona = {
            "Apellido": apellido,
            "Nombre": nombre,
            "Telefono": telefono,
            "Direccion": direccion,
            "Email": email
            }
                        
            contactos.append(Persona)
            contactos = sorted(contactos, key=itemgetter('Apellido')) 
            print("")
            os.system("cls")
            print("El contacto", Persona["Nombre"] + " " + Persona["Apellido"],  "fue agregado exitosamente.")
            print("")
            df_contactos = pd.DataFrame(contactos)
            df_contactos.to_csv(r'Agenda.csv', index=False)

        elif opcion == 2: #Ver contactos
            os.system("cls")
            print("")

            if not contactos:
                print("No hay contactos registrados.")
                print("")

            else:
                print("Contactos:")
                df_contactos = pd.DataFrame(contactos)
                print(df_contactos)
                print("")
        
        elif opcion == 3: #Borrar contacto
            os.system("cls")
            print("")
            
            if not contactos:
                print("No hay contactos registrados.")
                print("")
            
            else:
                print("Contactos:")
                df_contactos = pd.DataFrame(contactos)
                print(df_contactos)
                print("")
                id = ""
                while id == "" or id.isnumeric() == False:
                    print("Ingrese el numero de indice del contacto a borrar: ")
                    id = input(">>> ")
                print("")
                while int(id) > len(contactos)-1 or int(id) < 0:
                    print("Numero de indice inexistente.")
                    print("Ingrese el numero de indice del contacto a borrar: ")
                    id = input(">>> ")
                    print("")
                
                id = int(id)
                print("Confirma borrar contacto", contactos[id]['Nombre'] + " " + contactos[id]['Apellido'] ,  "con indice", id +"? \n 1 - Si \n 2 - No")
                borrar = input(">>> ")
                print("")
                if borrar == "1":
                    print("El contacto", contactos[id]['Nombre'] + " " + contactos[id]['Apellido'] ,  "con indice", id, "fue borrado exitosamente.")
                    del contactos[id]
                    contactos = sorted(contactos, key=itemgetter('Apellido')) 
                    print("")
                    df_contactos = pd.DataFrame(contactos) 
                    df_contactos.to_csv(r'Agenda.csv', index=False)
                    print("")
                elif borrar == "2":
                    os.system("cls")
                else:
                    print("Opcion incorrecta.")
        
        elif opcion == 4: #Modificar contacto
            os.system("cls")
            print("")
            
            if not contactos:
                print("No hay contactos registrados.")
                print("") 

            else:
                print("Contactos:")
                df_contactos = pd.DataFrame(contactos)
                print(df_contactos)
                print("")
                id = ""
                while id == "" or id.isnumeric() == False:
                    print("Ingrese el numero de indice del contacto a modificar: ")
                    id = input(">>> ")
                print("")
                while int(id) > len(contactos)-1 or int(id) < 0:
                    print("Numero de indice inexistente.")
                    print("Ingrese el numero de indice del contacto a modicar: ")
                    id = input(">>> ")
                    print("")
                
                id = int(id)
                len_campo = len(contactos[id])
                print("Ingrese el campo a modificar:")
                print(" 1 - Apellido")
                print(" 2 - Nombre")
                print(" 3 - Telefono")
                print(" 4 - Direccion")
                print(" 5 - Email")
                print("")
                campo = input(">>> ")
                
                while campo == "" or campo.isnumeric() == False:
                   print("Ingrese el campo a modificar: ")
                   campo = input(">>> ")
                print("")
                while int(campo) > len_campo or int(campo) < 0:
                    print("Campo inexistente.")
                    print("Ingrese el campo a modicar: ")
                    id = input(">>> ")
                    print("")
                int(campo)
                
                if campo == "1":
                    key = "Apellido"
                    print("Ingrese nuevo apellido: ")
                    nuevo_apellido = input("Nuevo apellido:")
                    apellido = contactos[id][key] 
                    contactos[id][key] = nuevo_apellido
                    print("El apellido", apellido, "fue cambiado por", nuevo_apellido + " exitosamente.")
                    contactos = sorted(contactos, key=itemgetter('Apellido'))
                    df_contactos = pd.DataFrame(contactos) 
                    df_contactos.to_csv(r'Agenda.csv', index=False)
                    print("")
                
                elif campo == "2":
                    key = "Nombre"
                    print("Ingrese nuevo nombre: ")
                    nuevo_nombre = input("Nuevo nombre:")
                    nombre = contactos[id][key] 
                    contactos[id][key] = nuevo_nombre
                    print("El nombre", nombre, "fue cambiado por", nuevo_nombre + " exitosamente.")
                    contactos = sorted(contactos, key=itemgetter('Apellido'))
                    df_contactos = pd.DataFrame(contactos) 
                    df_contactos.to_csv(r'Agenda.csv', index=False)
                    print("")
                
                elif campo == "3":
                    key = "Telefono"
                    print("Ingrese nuevo telefono: ")
                    nuevo_telefono = input("Nuevo telefono:")
                    telefono = contactos[id][key] 
                    contactos[id][key] = nuevo_telefono
                    print("El telefono", telefono, "fue cambiado por", nuevo_telefono + " exitosamente.")
                    contactos = sorted(contactos, key=itemgetter('Apellido'))
                    df_contactos = pd.DataFrame(contactos) 
                    df_contactos.to_csv(r'Agenda.csv', index=False)
                    print("")

                elif campo == "4":
                    key = "Direccion"
                    print("Ingrese nueva direccion: ")
                    nueva_direccion = input("Nueva direccion:")
                    direccion = contactos[id][key] 
                    contactos[id][key] = nueva_direccion
                    print("La direccion", direccion, "fue cambiada por", nueva_direccion + " exitosamente.")
                    contactos = sorted(contactos, key=itemgetter('Apellido'))
                    df_contactos = pd.DataFrame(contactos) 
                    df_contactos.to_csv(r'Agenda.csv', index=False)
                    print("")

                elif campo == "5":
                    key = "Email"
                    print("Ingrese nuevo email: ")
                    nuevo_email = input("Nuevo email:")
                    while email_valid(nuevo_email) == False:
                        nuevo_email = input("Formato incorrecto. Ingrese email nuevamente: ")
                    email = contactos[id][key] 
                    contactos[id][key] = nuevo_email
                    print("El email", email, "fue cambiado por", nuevo_email + " exitosamente.")
                    contactos = sorted(contactos, key=itemgetter('Apellido'))
                    df_contactos = pd.DataFrame(contactos) 
                    df_contactos.to_csv(r'Agenda.csv', index=False)
                    print("")       
        
        elif opcion == 5:
            os.system("cls")
            if os.path.exists("Agenda.bak") == True:
                bak = ""
                while bak == "" or bak.isnumeric() == False:
                    os.system("cls")
                    print("Atencion: Esta accion sobrescribira al backup existente y no puede deshacerse. Confirma continuar? \n 1 - No \n 2 - Si")
                    bak= input(">>> ")
                    print("")

                if bak == "1":
                    os.system("cls")
                    print("No se han realizado cambios.")
                    print("")

                elif bak == "2":
                    os.system("cls")
                    df_contactos = pd.DataFrame(contactos)
                    df_contactos.to_csv(r'Agenda.bak', index=False)
                    print("El backup se ha realizado exitosamente.")
                    print("")

                else:
                    print("Opcion incorrecta")
                    print("")
            else:
                os.system("cls")
                df_contactos = pd.DataFrame(contactos)
                df_contactos.to_csv(r'Agenda.bak', index=False)
                print("El backup se ha realizado exitosamente.")
                print("")

        elif opcion == 6:
            bak = ""
            while bak == "" or bak.isnumeric() == False:
                os.system("cls")
                print("Atencion: Esta accion sobrescribira a los datos actuales y no puede deshacerse. Confirma continuar? \n 1 - No \n 2 - Si")
                bak= input(">>> ")
                print("")

            if bak == "1":
                os.system("cls")
                print("No se han realizado cambios.")
                print("")

            elif bak == "2":
                os.system("cls")
                print("El backup ha sido restaurado.")
                contactos = []
                df_contactos = pd.DataFrame(contactos)
                with open("Agenda.bak", "r") as archivo:
                    lectura = csv.DictReader(archivo)
                    contactos = list(lectura)
                df_contactos = pd.DataFrame(contactos) 
                df_contactos.to_csv(r'Agenda.csv', index=False)
                print("")
            
            else:
                print("Opcion incorrecta")
                print("")

        elif opcion == 7: #Salir
            break

        elif opcion <1 or opcion >5:
            print("Opcion incorrecta.")
            print("")
    else:
        print("Opcion incorrecta.")
        print("")


