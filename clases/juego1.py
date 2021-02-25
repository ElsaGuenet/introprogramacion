#-----Entradas-----#
MENSAJE_SALUDAR = """Bienvenido 
                        a este programa, 
                            !!!jueguemos!!"""
PREGUNTA_NUMERO = """
        En este juego debes asetar un numero
        que va a desde el 1-10, la idea es que 
        lo puedes intentar las veces que quieras...
        Muchos exitos, ingresa tu numero
"""
PREGUNTA_FALLIDA = "aaaah ! Fallaste **** ingrese otro numero"
MENSAJE_GANASTE = "Felicidados ganaste !!"
MENSAJE_PERDISTE = "Perdiste... Vuelve a intentarlo"

#-----Entrada al codigo-----#
numeroOculto = 7
vidas = 5
print(MENSAJE_SALUDAR)
numeroIngresado = int(input(PREGUNTA_NUMERO))
if(numeroIngresado != numeroOculto):
    vidas -=1
while(numeroOculto != numeroIngresado and vidas > 1) :
    numeroIngresado = int(input(PREGUNTA_FALLIDA))
    vidas -=1

if(vidas >0):
    print(MENSAJE_DESPEDIDA)
    print(vidas)
else:
    print(MENSAJE_PERDISTE, "El numero era el", numeroOculto)
