import sys
nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su eada: "))
estatura = float(input("ingrese su estatura: "))
#les informations ne vont nulle part
#les doc peuvent être "csv"--> quand il y a beauuuucoup de donné o "txt"
nombreArchivo = "estudiantes.txt"
#para validar si el archivo existe o no
try:
    archivo = open(nombreArchivo)
    print("1")
except FileNotFoundError:
    archivo = open(nombreArchivo, "w", encoding= "UTF-8") #W est la forme dans laquelle le fichier va être ouvert
    #encoding UTF-8 est pour le clavier latino 
    descripcion = "Archivo de datos de estudiantes"
    print("2")
    archivo.writelines(descripcion)
    sys.exit(1) #sortir du doc 

archivo = open(nombreArchivo, "a")
linea = "\nnombre:" + nombre + "\n edad: " + str(edad) + "\n estatura:" + str(estatura) #"\n" = enter 
archivo.writelines(linea)
archivo.close()

#lire doc 
with open (nombreArchivo) as reader: #condition
    for line in reader:
        print(line)

import pandas as pd
diccionario = {}
diccionario["nombre"] = "Daniel"
diccionario["edad"] = 22
diccionario["estatura"] = 1.66
serie = pd.Series(diccionario)
print(serie)
serie.to_csv("datos.csv", sep=";")
