#-----Constante----#
mensaje_bienvenido = "Hola, voy a comparar dos numeros"
pregunta_numeroA = "cual es el numero A ?: "
pregunta_numeroB = "cual es el numero B?: "
mensaje_mayor = "el numero A es mayor que el numero B"
mensaje_menor = "el numero A es menor que el numero B"
mensaje_igual = "el numero A es igual que el numero B"

#------entrada al codigo-----# 
print(mensaje_bienvenido)
numeroA = int(input(pregunta_numeroA))
numeroB = int(input(pregunta_numeroB))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB
resultado =""
if(isMayor):
    resultado = mensaje_mayor
elif(isMenor):
    resultado = mensaje_menor
else:
    resultado = mensaje_igual
print(resultado)

