#------constantes------#
PREGUNTA_PESO = "cuanto psas en kg ?: "
PREGUNTA_ESTATURA = "Cuantos mides en mts: "
MENSAJE_BIENVENIDA = " Hola coma estas? voy a calcular tu IMC"
MESAJE_DESPEDIDA = "tu IMC es ..."

#-------Entrada codigo-------#
print(MENSAJE_BIENVENIDA)
peso = float(input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
IMC = peso/(estatura**2)
print(MESAJE_DESPEDIDA,IMC)
isObeso = IMC >= 30
print("El resultado de la prueba de obecidad es ...", isObeso)
