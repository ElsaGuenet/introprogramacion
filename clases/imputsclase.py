#-----Constantes-----#
PREGUNTA_NOMBRE = "como te llamas? : "
PREGUNDAD_EDAS = "Cuantos anos tienes ?"
PREGUNDAD_ESTATURA = "Cuantos metros mides ?"

MENSAJE_SALUDO = "Un gusto conecerte"

#-----Entrada al codigo-----#
nombre = input(PREGUNTA_NOMBRE)
edad = int (input (PREGUNDAD_EDAS))
estatura = float (input(PREGUNDAD_ESTATURA))
print(MENSAJE_SALUDO,nombre)
