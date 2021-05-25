#Punto1. Calcular el IMC de un usuario, pero valide que 
#los datos de entrada sean los correctos en caso de que 
#alguna entrada sea errónea vuelva a solicitar el ingreso 
#del dato hasta que sea correcto (adicionalmente pida el nombre y valide que sea un nombre válido).

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

#validateString ('Nombre: ')
#validateFloat('ingrese Peso: ')

#calcular IMC => Estatura, peso => peso/estatura^2
def pedirDatosEPN():
    """
    Se le pide al usuario el peso la estatura 
    y el nombre 
    Validando que la data este buena
    """
    preguntaPeso = "Ingrese su peso en kg: "
    preguntaEstatura ="Ingrese su estatura en metros: "
    preguntaNombre = "Ingrese su Nombre: "
    peso = validateFloat (preguntaPeso)
    estatura = validateFloat (preguntaEstatura)
    nombre = validateString(preguntaNombre)
    return peso, estatura, nombre 

def calcularIMC ():
    pesoIn, estaturaIn, nombreIn = pedirDatosEPN()
    imc = pesoIn/ (estaturaIn**2)
    return imc, nombreIn

calcularIMC()

imc, nombre = calcularIMC()
print(imc, nombre)
print(f"El imc de {nombre} es de {imc} %")

#Punto2. Pida al usuario que ingrese un párrafo 
#y luego muestre en pantalla cual es la palabra 
#más grande, la palabra más pequeña. 
#Valide que el párrafo ingresado termine en punto 
#sino es así se debe pedir al usuario que ingrese nuevamente el párrafo. 

def validateEndWith (strValidate, pregunta):
    isCorrectData = False 
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.endswith(strValidate))
            isCorrectData = True 
        except AssertionError:
            print('datos incorrectos ingrese nuevamente y recuerde que debe terminar con "{strValidate}" ')
    return valor 

parrafo = validateEndWith('.','ingrese un parrafo: ')
parrafo = parrafo [:-1]
palabras = parrafo.split (' ')
print(palabras)
print(f'la palabra mas grande es "{max(palabras, key=len)}" y el menor es "{min(palabras, key=len)}"')

parrafo = "Hola, como anda todo, Muchachos"
parrafo = parrafo.replace(',','')
print(parrafo)
palabras = parrafo.split(' ')
print(palabras)

#Punto3. Un taller de biomédica desea tener un 
#archivo para el manejo de los clientes, se pide 
#que desarrolle un programa que en su primera ejecución 
#cree el archivo llamado mantenimientos.txt. Luego en cada ejecución
#se preguntará por el nombre del equipo médico, una descripción 
#y el precio acordado para el mantenimiento 
#(se deben almacenar estos datos nuevos en el archivo mantenimientos.txt).

def validarArchivo (nombreArchivo, descripcion):
    try:
        archivo = open(nombreArchivo)
        return True 
    except FileNotFoundError:
        archivo = open(nombreArchivo, "w", encoding= "UTF-8") 
        descripcion = "Archivo de datos de estudiantes"
        print("2")
        archivo.writelines(descripcion)
        return False 

def guardarLinea (nombreArchivo, lineaIn):
    archivo = open(nombreArchivo, 'a')
    archivo.writelines(lineaIn)

nameFile = "mantenimiento.txt"
isvalidate = validarArchivo(nameFile, "seguimiento de mantenimiento de equipos medicos")
if (isvalidate):
    descEquipo = input("Ingrese la description del equipo: ")
    nombre = validateString('Ingrese su nombre: ')
    precio = validateFloat ("Ingrese el precio: ")
    linea = '\nDescription: '+ descEquipo + ' nombre técnico: ' + nombre + ' precio acordado: ' + str(precio)
    guardarLinea(nameFile, linea)
else:
    print("se creo el archivo")

