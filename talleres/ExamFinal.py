#Punto1 
import matplotlib.pyplot as plt 
alimentos = [input("Ingrese tu 8 alimentos favoritos por favor: ")]
precios = [input("Ingrese sus precios: ")]
plt.bar(alimentos, precios)
plt.title("Alimentos favoritos en funcion de sus precios")
plt.xlabel("Alimentos favoritos del usuario")
plt.ylabel("Precios")
plt.savefig("GraficoBarasExam.png")
plt.show 


#Punto2
class Humano():
    def __init__(self, nombreEntrada, sexoEntrada, edadEntrada):
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada 
        self.edad = edadEntrada

    def mostrarAtributos(self):
        print(f"""Hola, soy {self.nombre}, 
                mi sexo es {self.sexo},
                y tengo {self.edad} anos""")

    def hablar (self, mensaje):
        print(f"Hola, soy {self.nombre} y me gustaria decir", mensaje)

class Doctor (Humano):
    def _init_ (self, nombreEntrada, sexoEntrada, edadEntrada, estaturaIn, pesoIn ):
        Humano._init_(self, nombreEntrada, sexoEntrada, edadEntrada)
        self.estatura = estaturaIn
        self.peso = pesoIn

    def calculIMC (self, IMC):
        IMC = self.peso/(self.estatura**2)
        self.IMC = IMC 
        print(IMC)

humano1 = Humano("Elsa", "Feminina", 22)
humano1.mostrarAtributos
humano1.hablar("Estoy una estudiante francesa")
doctor1= Doctor ("Elsa", "Feminina", 22)
doctor1.calculIMC

#Punto3
nombreIngresada = print(input("Ingrese tu nombre por favor: "))
dolarIngresada = print(int(input("Ingrese tu dinero en dolares por favor: ")))
def convertir (a=dolarIngresada, b=0.82):
    return a*b 
print(convertir)

#Punto4 
def validateFloat (pregunta):
    isCorrectData = False 
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True 
        except ValueError:
            print('datos incorrectos ingrese nuevamente')
    return valor 

def validateString (pregunta):
    isCorrectData = False 
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.isalpha())
            isCorrectData = True 
        except AssertionError:
            print('datos incorrectos ingrese nuevamente')
    return valor 

def validarArchivo (nombreArchivo, descripcion):
    try:
        archivo = open(nombreArchivo)
        return True 
    except FileNotFoundError:
        archivo = open(nombreArchivo, "w", encoding= "UTF-8") 
        descripcion = "Archivo para el manejo de los clientes"
        print("2")
        archivo.writelines(descripcion)
        return False 

def guardarLinea (nombreArchivo, lineaIn):
    archivo = open(nombreArchivo, 'a')
    archivo.writelines(lineaIn)

nameFile = "pacientes.txt"
isvalidate = validarArchivo(nameFile, "Datos de un nuevo paciente")
if (isvalidate):
    nombre = validateString('Ingrese el nombre del paciente: ')
    enfermedad = validateString('Ingrese la enfermedad del paciente: ')
    precio = validateFloat ("Ingrese el precio de la consulta: ")
    linea = '\nnombre paciente:' + nombre + ' enfermedad del paciente: '+ enfermedad + ' precio consulta: ' + str(precio)
    guardarLinea(nameFile, linea)
else:
    print("se creo el archivo")