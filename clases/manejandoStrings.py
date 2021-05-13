texto ="Hola espero que todo ande bien"
lista = [1, 434, 53, 2, 2]
lista.sort ()
lista.pop(2)
for elemento in lista : 
    print(elemento)
for i in range(len(lista)):
    print(lista[i])

for letra in texto:
    print(letra)

print(texto[1])
palabras = texto.split(" ")
print(palabras)
print(type(palabras))
eliminarE= texto.split("e", maxsplit= 2)
eliminarE= texto.split("e")
datos = "nombre;apellido;edad"
print(datos.split(";"))
print(eliminarE)

uniendo= "".join(eliminarE)
print(uniendo)
info = " ".join(datos.split(";"))
print(info)

listaNombres = ["Laura", "Juan", "Mario", "Elsa", "Katherine", "Daniel", "Paul"]
print(max(listaNombres))#avec les valeurs des lettre : code ASCII
print(max(listaNombres, key=len))


respuesta = input("Ingrese Si o No: ")
print(respuesta.upper()) #poner en majuscula
if respuesta == "Si":
    print("Hola bienvenido al codigo")
else:
    print("Chao !")

nombre = input("Ingrese su nombre: ")
print(nombre.capitalize()) #poner la primera letra en majuscula
print(type(nombre))

correo = "ESPERO QUE ESTES BIEN"
print(correo.casefold().capitalize()) #poner todo en minuscula exepto la primera letra 
saludo = "Hola como estas?"
nomre = "Maria Alejandra"
nombre = "maria alejandra"
nombres = nombre.split(" ")
nombre = ""
for elemento in nombres:
    nombre += elemento.capitalize() +" "
print(nombre)
print(saludo.center(50))
print(nombre.center(50))

enunciado = "Hola hola ya me cansé de decir tantos hola pero como vamos hola "
print(enunciado.upper().count("HOLA")) #compte le nombre du mot

print(enunciado.find("decir")) #trouver le mot --> dis à quel nomre de caractère le mot est 
print(enunciado[25:30])

txt = "me gusta programar en java"
print(txt.replace("java", "python"))

