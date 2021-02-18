#-----constante-----#
pregunta_numero1 = "Elige un primero numero: "
pregunta_nombre2 = "Elige un secundo numero: "
pregunta_comparacion = "tu primero numero es mas grande que tu secundo numero ?: "
MENSAJE_BIENVENIDA = "hola, vamos a comparar dos numeros"

#-----entrada al codigo-----#
print(MENSAJE_BIENVENIDA)
nombre1 = float(input(pregunta_numero1))
nombre2 = float(input(pregunta_nombre2))
comparacion = input(pregunta_comparacion)
isMayorNumbre = nombre1 >= nombre2
print("el numero uno es mayor que el numero dos", isMayorNumbre)
isMenorNumbre = nombre1 <= nombre2 
print("el numero uno es menor que el numero dos", isMenorNumbre)