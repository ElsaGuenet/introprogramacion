guardar = print("hola")
print (guardar)

guardar = round(14.3456789,2)
print(guardar)

def linedesign(cantidad=10, simbolo="#"):
    print(simbolo*cantidad)
    return None

linedesign(30,"#")
linedesign(10,"*")
linedesign(100,"§")
linedesign()

#-----Muestra la lista-----#
def mostrarLista(listaEntrada = []):
    for elemento in listaEntrada:
        print(elemento)
    return None
lista = [213,32,23123,321,321,233,1232,23]
lista2 = [4578,679,568,567,3457,467]
linedesign(30,"¤")
mostrarLista(lista)
linedesign(30,"$")
mostrarLista(lista2)
#-----sumar dos numero-----#
def sumar (a = 0,b=0):
    suma = a + b
    return suma
linedesign(30,"¤")
resultado = sumar()
print(resultado)
print(sumar(12,14))
round(12.234567,2)
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

print(restar(83,87))
print(multiplicar(83,87))
print(dividir(83,87))