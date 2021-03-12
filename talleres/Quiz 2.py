ListaPesos = [20000,30000,4000,2500,1000,7600]
PreguntaNumero = """ Hola! Bienvenido
                    Por favor elije una opcion:
                    1.Hacer convercion de Pesos a Dolares o Euros
                    2.Agregar una valor a la lista
                    3.Mostrar el ingreso más alto, el Ingreso más bajo 
                        y el Promedio de ingresos
                    4.Eliminar elemento de la lista
                    5.Salir 
                    """

PreguntaConvercion = """
Elije una opcion :  C = mostrar original en pesos Colombianos
                    D = mostrar en dolares
                    E = mostrar en euro 
                    """ 

PreguntaValorAgregada = "Ingresa la valor que quieres agregar: "

PreguntaPosicion = "Ingrese la posición que desea borrar: "

#----Mensaje-----#
MensajePesos = "Mostrando lista original"
MensajeDolares = "Mostran lista en dolares"
MensajeEuro = "Mostran lista en Euro"
MensajeEror = "Valor ingresado no valido"
MensajeMayor = "El mayor numero ingresado es :"
MensajeMenor = "El menor numero ingresado es :"
MensajePromedio = "El promedio es :"
MensajeDespedida = "Adios, que tengas un feliz dia"

#convercion punto 1
listaEuro = []
for elemento in ListaPesos:
    conversor = round(elemento*0.00023,2)
    listaEuro.append(conversor)
ListaDolares = []
for elemento in ListaPesos:
    conversor = round (elemento*0.00023,2)
    ListaDolares.append(conversor)

#-----entrada al codigo-----#
OpcionEscogida = int(input(PreguntaNumero))
while(OpcionEscogida !=5):
    #----Opcion1----#
    if(OpcionEscogida == 1):
        OpcionConvercion = input(PreguntaConvercion)
        if(OpcionConvercion == "C"):
            print(MensajePesos)
            print(ListaPesos)
        elif(OpcionConvercion == "D"):
            print(MensajeDolares)
            print(ListaDolares)
        elif(OpcionConvercion == "E"):
            print(MensajeEuro)
            print(listaEuro)
        else:
            print(MensajeEror)
    #----opcion2----#
    elif(OpcionEscogida == 2):
        ValorIngresado = float(input(PreguntaValorAgregada))
        ListaPesos.append(ValorIngresado)
        print(ListaPesos)
    #----opcion3----#
    elif(OpcionEscogida == 3):
        print(MensajeMayor,max(ListaPesos))
        print(MensajeMenor,min(ListaPesos))
        print(MensajePromedio,sum(ListaPesos)/len(ListaPesos))
    #----Opcion4----#
    elif(OpcionEscogida == 4):
        print(ListaPesos)
        posicion = int(input(PreguntaPosicion))-1
        ListaPesos.pop(posicion)
        print(ListaPesos)
    #----Opcion no valida----#
    else:
        print(MensajeEror)
    OpcionEscogida = int(input(PreguntaNumero))

print(MensajeDespedida)

