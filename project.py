#------- REALIZADO POR: Juan Esteban Salazar y Alejandro Clavijo ---------------

import couchdb
conn_string= "http://Juanes:7184@localhost:5984"
server = couchdb.Server(conn_string)
db_name = "recommendation-system"

if db_name in server:
    print("Conectado con la Base de datos: "+db_name)
    db= server[db_name]
else:
    print("--- Creando la base de datos")
    db = server.create(db_name)

def Create(data):
  nuevoDoc  = db.save(data)
  return nuevoDoc

def crear():
   tipo = int(input("Ingrese por favor el numero correspondiente al tipo de registro que desea crear \n 1. Usuario \n 2. Tutor \n 3. Curso \n Realizar: "))
   if (tipo == 1):
      Id_Usuario = input("Introduzca el ID del usuario: ")
      Nombre = input("Introduzca el nombre del usuario: ")
      Carrera= input("Introduzca la carrera del usuario: ")
      Semestre = int(input("Introduzca el numero de semestre del usuario: "))
      usuario = {
               "Id_Usuario": Id_Usuario ,
                "Nombre": Nombre ,
                "Carrera":Carrera ,
                "Semestre": Semestre
      }
      Create(usuario)
      
      print("------- REGISTRO CREADO CON EXITO------")
   elif (tipo== 2):
      Id_Tutor = input("Introduzca el ID del tutor: ")
      Nombre = input("Introduzca el nombre del tutor: ")
      Carrera = input("Introduzca la carrera del tutor: ")
      Semestre= int(input("Introduzca el semestre del tutor: "))
      Calificacion_Prom= float(input("Introduzca la calificación promedio del tutor: "))
      tutor = {
        "Id_Tutor": Id_Tutor,
        "Nombre": Nombre,
        "Carrera":Carrera ,
        "Semestre": Semestre,
        "Calificacion_Prom":Calificacion_Prom 
      }
      Create(tutor)
      
      print("------- REGISTRO CREADO CON EXITO------")
   elif (tipo==3):

      Id_Curso= input("Introduzca el ID del curso: ")
      Nombre = input("Introduzca el nombre del curso: ")
      Categoria=  input("Introduzca la categoria del curso: ")
      Modalidad =  input("Introduzca la modalidad del curso: ")
      Gratuito= input("¿El curso es gratuito?: ")
      Precio = int( input("Introduzca el precio del curso: "))
      Duracion= int( input("Introduzca la duracion en horas del curso: "))
      Certificado =  input("¿El curso tiene certificado?: ")
      califPromedio= float( input("Introduzca la calificación promedio del curso: "))

      curso = {
         
      
        "Id_Curso": Id_Curso,
        "Nombre": Nombre,
        "Categoria":Categoria ,
        "Modalidad": Modalidad,
        "Gratuito":Gratuito ,
        "Precio": Precio,
        "Duracion": Duracion,
        "Certificado":Certificado ,
        "califPromedio":califPromedio 

      }
      Create(curso)
      
      print("------- REGISTRO CREADO CON EXITO------")
   else:
    print("Ingrese una opcion válida -----------------")


def Select_By_Key(type, key,value):
    results = []
    for row in db.view(f"{type}/buscar_por_{key}", startkey=value, endkey=value):
        results.append(row.value)
    return results


def consultar():
   t= int(input("Ingrese la opción que desea \n 1. Usuario \n 2. Tutor \n 3. Curso \n Consultar:   "))
   if (t==1):
      type= "Usuarios"
      key= input("Ingrese la llave de busqueda para el usuario (Id_Usuario, Nombre, Carrera, Semestre): ")
      value= input("Ingrese el valor para la llave digitada: ")
      usuarios = Select_By_Key(type, key, value)
      print(f"Se muestran resultados para {type}: ")
      for usuario in usuarios:
         print(usuario)
   elif (t==2):
      type= "Tutores"
      key= input("Ingrese la llave de busqueda para el tutor (Id_Tutor, Nombre, Carrera, Semestre, Calificacion_Prom): ").capitalize()
      value= input("Ingrese el valor para la llave digitada: ")
      tutores = Select_By_Key(type, key, value)
      print(f"Se muestran resultados para {type}: ")
      for tutor in tutores:
         print(tutor)
   elif (t==3):
      type= "Cursos"
      key= input("Ingrese la llave de busqueda para el tutor (Id_Curso, Nombre, Categoria, Modalidad, Gratuito, Precio, Duracion, Certificado, califPromedio): ").capitalize()
      value= input("Ingrese el valor para la llave digitada: ")
      cursos = Select_By_Key(type, key, value)
      print(f"Se muestran resultados para {type}: ")
      for curso in cursos:
         print(curso)
    
      
   

operacion= int(input("Introduzca la operación CRUD que desea realizar \nCREAR: 1  \nCONSULTAR: 2\nRealizar: "))

if (operacion == 1):
   crear()

elif(operacion== 2):
   consultar()
   
   

