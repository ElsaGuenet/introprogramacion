#-----Mensajes-----#
MENSAJE_SALUDAR = "Bienvenido! te apoyaré ahorrando"
MENSAJE_AHORRO = "LLEVAS AHORRADO ..."
PREGUNTA_VALOR_CPU = "Cuanto vale el pc que deseas?: "
PREGUNTA_CUANTO_TIENE = "Cuanto llevas ahorrado?: "

#-----Entradas-----#
print(MENSAJE_SALUDAR)
valor = float(input(PREGUNTA_VALOR_CPU))
ahorrado = float(input(PREGUNTA_CUANTO_TIENE))

while(valor > ahorrado):
    print(MENSAJE_AHORRO, ahorrado, "te faltan ...", valor - ahorrado)
    ahorrado = ahorrado + 1000
print(valor == ahorrado)