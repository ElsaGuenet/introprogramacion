#-----constantes-----#
MENSAJE_BIENVENIDO = "Hola! Bienvenido al codigo que te muestra en qué estado de triglicéridos y homocistéina tienes !"
PREGUNTA_TRI = "Ingrese el nivel de trigliceridos en mg/dL: "
PREGUNTA_HOMO = "Ingrese el nivel de homocisteina en µmol/L: "
MENSAJE_TRI_OPTIMO = "El nivel de trigliceridos es optimo"
MENSAJE_TRI_LIMITE = "El nivel de trigliceridos es sobre el limite optimo"
MENSAJE_TRI_ALTO = "El nivel de trigliceridos es alto"
MENSAJE_TRI_MUYALTO = "El nivel de trigliceridos es muy alto"
MENSAJE_HOMO_OPTIMO = "El nivel de homocisteina es optimo"
MENSAJE_HOMO_LIMITE = "El nivel de homocisteina es sobre el limite optimo"
MENSAJE_HOMO_ALTO = "El nivel de homocisteina es alto"
MENSAJE_HOMO_MUYALTO = "El nivel de homocisteina es muy alto"
resultadoTri = ""
resultadoHomo = ""
MENSAJE_DESPEDIDA = "Gracias y adios !"

#-----entrada al codigo-----#
print(MENSAJE_BIENVENIDO)
NivelTri = float(input(PREGUNTA_TRI))
NivelHomo = float(input(PREGUNTA_HOMO))
isTriOptimo = NivelTri < 150 
isTriLimite = 150 <= NivelTri <= 199
isTriAlto = 200 <= NivelTri <= 499
isTriMuyAlto = NivelTri >= 500
isHomoOptimo = 2 <= NivelHomo < 15 
isHomoLimite = 15 <= NivelHomo < 30
isHomoAlto = 30 <= NivelHomo < 100 
isHomoMuyAlto = NivelHomo >= 100 
if(isTriOptimo): 
    resultadoTri = MENSAJE_TRI_OPTIMO
elif(isTriLimite):
    resultadoTri = MENSAJE_TRI_LIMITE
elif(isTriAlto):
    resultadoTri = MENSAJE_TRI_ALTO
else:
    resultadoTri = MENSAJE_TRI_MUYALTO
if(isHomoOptimo):
    resultadoHomo = MENSAJE_HOMO_OPTIMO
elif(isHomoLimite):
    resultadoHomo = MENSAJE_HOMO_LIMITE
elif(isHomoAlto):
    resultadoHomo = MENSAJE_HOMO_ALTO
else:
    resultadoHomo = MENSAJE_HOMO_MUYALTO

print(resultadoTri)
print(resultadoHomo)
print(MENSAJE_DESPEDIDA)