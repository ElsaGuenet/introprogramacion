
isCorrectInfo = False
while (isCorrectInfo == False ):
    try: 
        edad = int (input("ingrese su edad: "))
        isCorrectInfo = True
    except ValueError : 
        print("ingresaste un dato no valido")
nombreArchivo = input("Ingrese el nombre del archivo que desea encontrar: ")
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    print(f"El archivo {nombreArchivo} no se ha encontrado")

base = 4
dividor = 0
try: 
    dividir = base/dividor
except ZeroDivisionError : 
    print("El divisor ingresado es igual a 0 por lo tanto es imposible dividir")

nombre = "Elsa"
print(nombre.isalpha()) #es ce que c'est des lettres ou non ? 
assert (nombre.isalpha())

isCorrectInfo = False
while (isCorrectInfo == False)
    try: 
        edad = int (input("ingrese su edad: "))
        isCorrectInfo = True
    except ValueError : 
        print("ingresaste un dato no valido")

isCorrectInfo = False
while (isCorrectInfo == False)
    try: 
        edad = int (input("ingrese su edad: "))
        assert (edad >= 18)
        isCorrectInfo = True
    except AssertionError : 
        print("Los menores de edad no pueden acceder")
    except ValueError:
        print("las edades son numeros enteros")

listas = [2, 43, 42, 5]
try:
    listas [5]
except:
    print("El indice es mayor al tamano de la lista")
