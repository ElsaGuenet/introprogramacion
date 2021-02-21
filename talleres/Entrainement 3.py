#-----constantes-----#
mensaje_bienvenido = "Hola! bienvenido al codigo!"
pregunta_AnoActual = "qué ano es ?: "
pregunta_otroAno = "elija un ano al azar :"
mensaje_AnoFaltan = "Numero de anos que faltan para llegar a este anos: "
mensaje_AnoPasado = "Numero de anos que han pasado desde este ano:"
mensaje_igual = "es el mismo ano"
resultado = ""

#-----entrada al codigo-----#
print(mensaje_bienvenido)
AnoActual = int(input(pregunta_AnoActual))
OtroAno = int(input(pregunta_otroAno))
isMayor = AnoActual > OtroAno
restarMayor = AnoActual - OtroAno
isMenor = AnoActual < OtroAno
restarMenor = OtroAno - AnoActual
isIgual = AnoActual = OtroAno
if(isMayor):
    resultado = mensaje_AnoPasado, restarMayor
elif(isMenor):
    resultado = mensaje_AnoFaltan, restarMenor
else:
    resultado = mensaje_igual

print(resultado)
