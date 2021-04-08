#---question 1----#
def lineDesignC(cantidad =15):
    print("#"* cantidad)
    return None
def sumar (valor1=0, valor2=0, valor3=0):
    return valor1 + valor2 + valor3
def restar (valor1=0, valor2=0, valor3=0):
    return valor1 - valor2 -valor3
def multiplicar (valor1=0, valor2=1, valor3=1):
    return valor1 * valor2 * valor3
def dividir (valor1=0, valor2=1, valor3=1):
    return valor1 / valor2 / valor3
def potenciar (base = 0,exponente1 =1, exponente2= 2):
    return base**exponente1 ** exponente2

def calculadora (operacion, valor1, valor2, valor3):
    print(operacion(valor1,valor2,valor3))

print(sumar(11,54,6))
print(lineDesignC())
print(restar(67,4,28))
print(lineDesignC())
print(multiplicar(23,9,66))
print(lineDesignC())
print(dividir(50,7,3))
print(lineDesignC())
print(potenciar(10,4,2))

#----Question 2----#
def mostrarLista(listaEntrada = []):
    for elemento in listaEntrada:
        print(elemento)
    return None
lista1 = [56, 85, 24, 73]
lista2 = ["Arthur", "Luc", "Adrien", "George"]
lista3 = [1.67, 1.78, 1.60, 1.90]
print(lineDesignC())
mostrarLista(lista1)
print(lineDesignC())
mostrarLista(lista2)
print(lineDesignC())
mostrarLista(lista3)
print(lineDesignC())

#----question 3----#
def calculadoraAir(base = 1, altura =1, divisor=2):
    return (base*altura) / divisor
baseIngresada = float (input("Ingrese la base del triangulo : "))
alturaIngresada = float (input("Ingrese la altura del triangulo : "))
print(calculadoraAir(baseIngresada,alturaIngresada))

#----question 4----#
def InfoLista (listaEntrada = []):
    mayor = max(listaEntrada)
    menor = min(listaEntrada)
    acumulador = 0
    for elemento in listaEntrada:
        acumulador += elemento
    tamanoLista = len(listaEntrada)
    promedio = acumulador / tamanoLista
    print(f"el numero mayor en la lista es {mayor}, el numero menor en la lista es {menor} y el promedio en la lista es {promedio}")
listaEntrada = [17, 97, 167, 43, 2, 46]
InfoLista(listaEntrada)

#----question 4----# 

