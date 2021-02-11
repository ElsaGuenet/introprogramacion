# Estos son buleos 

pruebaV = True 
pruebaF = False 
print(pruebaF)
print(pruebaV)
pruebaV = pruebaF 
print(pruebaV)
edad = 21
estatura = 1.56
peso = 51
NOMBRE = "Elsa Guenet"
print("#"*15, "Mayor Edad", "#"*15)
isMayorEdad = edad >= 18
print(isMayorEdad)
print("#"*15, "Bajo la Estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)
# Calculando si el peso es diferente de 51 
print("#"*15, "Peso diferente 51", "#"*15)
isPesoDiferente = peso != 51
print(isPesoDiferente)
# vamos a ver si un apellido esta en el nombre completo 
apellido = "Guenet"
isApellido = apellido in NOMBRE 
print("#"*15, "Esta appellido en el nombre?", "#"*15)
print(isApellido)
