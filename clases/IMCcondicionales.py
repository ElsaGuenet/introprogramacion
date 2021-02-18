#------constantes------#
PREGUNTA_PESO = "cuanto psas en kg ?: "
PREGUNTA_ESTATURA = "Cuantos mides en mts: "
MENSAJE_BIENVENIDA = " Hola coma estas? voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "tu IMC es ..."
MENSAJE_BAJO_PESO = "Esta pero delgado! "
MENSAJE_NORMAL = "Estas en forma"
MENSAJE_SORRE_PESO = "Ten cuidado estas en sobre preso"
MENSAJE_OBESO = "Cuidado estas obeso tu salud corre riesgo"

#-------Entrada codigo-------#
print(MENSAJE_BIENVENIDA)
peso = float(input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
IMC = peso/(estatura**2)
isBajoPeso = IMC < 18.5
isNormal = IMC >= 18.5 and IMC < 25
isSobrePeso = IMC >= 25 and IMC < 30
resultado = ""
if(isBajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif (isNormal):
    resultado = MENSAJE_NORMAL
elif (isSobrePeso):
    resultado = MENSAJE_SORRE_PESO
else :
    resultado = MENSAJE_OBESO

print(MENSAJE_DESPEDIDA, IMC)
print(resultado)
