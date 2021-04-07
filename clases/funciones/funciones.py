#-----sumar dos numero-----#
def sumar (a = 0,b=0):
    """
        devuelve la suma de dos numeros a y b 
        por defecto a vale 0 al igual que b
    """
    suma = a + b
    return suma

#-----restar dos numero-----#
def restar (a = 0,b=0):
    resta = a - b
    return resta
#-----multiplicar dos numero-----#
def multiplicar (a = 0,b=0):
    multiplica = a * b
    return multiplica
#-----dividir dos numero-----#
def dividir (a = 0,b=1):
    dividi = a / b
    return dividi
#-----potenciar dos numero-----#
def potenciar (base = 0,exponente =1):
    potencia = base**exponente
    return potencia
#-----funciones dependientes de otras-----#
def calcular(operacion, numeroA, numeroB):
    print(operacion(numeroA,numeroB))
