#-----constantes-----#
mensaje_bienvenido = "hola! bienvenido al codigo de conversion de unidades"
pregunta_distancia = "Elija una distancia en centimetros: "

#------entrada al codigo-----# 
print(mensaje_bienvenido)
distancia_en_centimetros = float(input(pregunta_distancia))
distancia_en_metros = distancia_en_centimetros/100
distancia_en_kilometros = distancia_en_metros/1000 
print("este distancia es", distancia_en_centimetros,"cm", distancia_en_metros,"m", distancia_en_kilometros,"km")