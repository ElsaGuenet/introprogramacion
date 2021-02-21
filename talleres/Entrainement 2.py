#-----constante-----#
mensaje_bienvenido = "hola! bienvenido al codigo"
pregunta_edad = "Qué edad tienes ?: "
mensaje_menor = "eres menor de edad"
mensaje_joven = "eres joven"
mensaje_adulto = "eres adulto"
mensaje_adultoMayor = "eres adulto mayor"
resultado = ""

#-----entrada al codigo-----#
print(mensaje_bienvenido)
edad = int(input(pregunta_edad))
isMenor = edad < 18 
isJoven = 18 >= edad <= 25 
isAdulto = 26 >= edad <= 60 
isAdultoMayor = edad > 60 
if(isMenor):
    resultado = mensaje_menor
elif(isJoven):
    resultado = mensaje_joven
elif(isAdulto):
    resultado = mensaje_adulto
else:
    resultado = mensaje_adultoMayor
print(resultado)
