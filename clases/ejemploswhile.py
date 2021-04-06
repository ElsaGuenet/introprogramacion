#----Entradas----#
Mensaje_bienvenida = "Muy buenos dias despierte que esta en clase de 6"
mensaje_error = "por favor ingresa una opcion valida"
pregunta_menu = """Ingrese
        1- para mostrar los numeros del 1-5
        2- para preguntar tu nombre
        3- para mostrar el ano en el que estamos 
        4- salir 
        """
Pregunta_nombre = "Ingrese su nombre por favor : "

#----entrada al codigo----#
entrada = 1
while (entrada >=1 and entrada <=3):
    entrada = int(input(pregunta_menu))
    if (entrada == 1):
        print(1,2,3,4,5)
    elif (entrada == 2):
        nombre = input(Pregunta_nombre)
        print (f"Bienvenido {nombre} a este menu emplea las otras opciones")
    elif(entrada == 3):
        print("estamos en el ano 2021")
    elif(entrada == 4):
        print("Muchas gracias por usar el programa feliz dia")
    else:
        entrada = 1
        print(mensaje_error)
