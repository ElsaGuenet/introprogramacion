

#-----Entradas-----#
MENSAJE_SALUDAR = """
        Bienvenido
            a etse programa,
        Jeguemos!!! """
MENSAJE_SEGUNDO_NIVEL = "Felicidades pasaste el primer nivel ahora ve por el ultimo !!"
MENSAJE_CALIENTE = "Estas caliente"
MENSAJE_FRIO = "Estas Frio"
PREGUNTA_NUMERO = """
    En este juego debes asetar un numero entero
    que va desde el 1-10, la idea es que 
    lo puedes intentar ante de que se te 
    acaben las vidas... no existe vida O
    Muchos éxitao, ingresa tu numero : """

PREGUNTA_DIFICUTAD = """
    1- Facil
    2- Moderado
    3- Dificil
"""
PREGUNTA_FALIDA = " Aaaaah! Fallaste... ingresa otro numero: "
MENSAJE_GANASTE = "Felicidades ganaste !!"
MENSAJE_PERDISTE = "perdiste D: ""vuelve"" a intentarlo!!"
#-----entrada al codigo-----#
import random 
numeroOculto = random.randint (1,10)
numeroOcultoDos = random.randint (1,10)
vidas = None


dificultad = int(input(PREGUNTA_DIFICUTAD))
while (dificultad !=1 and dificultad !=2 and dificultad !=3 ):
    print("ingresa una opcion valida")
    dificultad = int(input(PREGUNTA_DIFICUTAD))


if(dificultad ==1):
    print("Modo facil activado")
    vidas = 10
elif(dificultad == 2):
    print("Modo moderado activado")
    vidas = 5
else:
    print ("Modo dificil activado, sssss mucho cuidado")
    vidas = 2

numeroIngresado = int(input(PREGUNTA_NUMERO))
while (numeroIngresado != numeroOculto and vidas>1):
    if( numeroIngresado > numeroOculto):
        print(MENSAJE_CALIENTE)
    else:
        print(MENSAJE_FRIO)
    vidas -=1
    print(f"te quedan {vidas} vidas")
    numeroIngresado = int(input(PREGUNTA_FALIDA))
if(vidas >= 0 and numeroIngresado == numeroOculto):
    print (MENSAJE_SEGUNDO_NIVEL)
    numeroIngresado = int(input(PREGUNTA_NUMERO))
    while (numeroIngresado !=  numeroOcultoDos and vidas>1):
        if (numeroIngresado > numeroOcultoDos):
            print(MENSAJE_CALIENTE)
        else:
            print(MENSAJE_FRIO)
        vidas -=1
        print (f"te quedan {vidas} vidas")
        numeroIngresado= int(input(PREGUNTA_FALIDA))

    
if(vidas >= 0 and numeroIngresado == numeroOcultoDos):
        print(MENSAJE_GANASTE)

else:
    print(MENSAJE_PERDISTE,"el numero uno era el ", numeroOculto, "el numero dos era el",numeroOcultoDos)
