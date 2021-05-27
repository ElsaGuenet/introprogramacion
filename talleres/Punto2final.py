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
        print(f"Hola, sou {self.nombre} y me gustaria decir", mensaje)

class Doctor (Humano):
    def calcularIMC(self, estaturaIn, PesoIn, IMC):
        preguntaEstatura = float(input("Ingrese tu estatura en metro: "))
        preguntaPeso = int(input("Ingrese tu peso en kg: "))
        IMC = preguntaPeso/(preguntaEstatura**2)
        self.estatura = estaturaIn
        self.peso = PesoIn
        self.IMC = IMC 
        print(IMC)