#----Punto1----# 
class ElementoDigital ():
    """Esta es la clase Elemento Digital, muestra en pantalla
        las generalidades de la cancion como:
        nombre
        creador
        fecha de publicacion 
        Ademas, al final muestra todos sus atributos
        """

    def __init__(self, entradaNombre, entradaFecha, entradaCreador):
        print("Esta es una nueva cancion, espero la disfrutes")
        self.nombre = entradaNombre
        self.fecha = entradaFecha
        self.creador = entradaCreador

    def atributos (self):
        print(f"""Esta cancion se llama {self.nombre}
        fue creada en {self.fecha} y 
        su creador es {self.creador}
        """)

spotify = ElementoDigital("La Tristesse du Diable","2018", "Meimuna")
spotify.atributos()
print("*"*50)

#----Punto2----# 
class Usuario ():
    """Esta es la clase Usuario, mostrara en la pantalla:
    Nombre
    Edad
    Sexo
    Naciaonalidad
    Al final muestra sus atributos
    """

    def __init__(self, entradaNombre, entradaEdad, entradaSexo, entradaNacionalidad):
        print("Hola, bienvenido en la pantalla Usuario")
        self.nombre = entradaNombre
        self.edad = entradaEdad
        self.sexo = entradaSexo
        self.nacionalidad = entradaNacionalidad

    def atributos (self):
        print(f"""Hola, me llamo {self.nombre},
                tengo {self.edad} anos,
                mi sexo es {self.sexo}
                y soy de nacionalidad {self.nacionalidad}""")
        print(f"Hola soy {self.nombre} y estoy escuchando una cancion")
    
usuario = Usuario("Elsa GUENET", 22, "femenino", "Francesa")
usuario.atributos()
print("*"*50)

#-----Punto3-----# 
class Pagina ():
    """Esta es la clase Pagina, mostara en la pantalla:
    Tipo de contenido
    Formato
    Fecha de publicacion""" 

    def __init__(self, entradaContenido, entradaFormato, entradaFecha):
        self.contenido = entradaContenido
        self.formato = entradaFormato
        self.fecha = entradaFecha

    def atributos (self):
        print(f"""el tipo de contenido de esta pagina es {self.contenido}
                el formato es {self.formato}
                y la fecha de publicacion es {self.fecha}
                """)

pagina1 = Pagina("musica","mp3", "2018")
pagina1.atributos()
print("*"*50)

#-----------Herencia-----------# 
#----Punto 1----# 
class Cancion (ElementoDigital):
    def __init__(self, entradaNombre, entradaFecha, entradaCreador, entradaGenero, entradaDuracion):
        ElementoDigital.__init__(self, entradaNombre, entradaFecha, entradaCreador)
        self.genero = entradaGenero
        self.duracion = entradaDuracion
        print(f"Esta es una nueva cancion que se llama {self.nombre} y fue creada en {self.fecha}")
    def reproducciones (self, numeroReproducciones):
        for i in range(numeroReproducciones):
            print(f"{self.nombre} sonando {i+1} vez")

cancion2 = Cancion("Baby", "junio 2012", "Justin Bieber", "pop", "3 minutos")
cancion2.reproducciones(5)
print("*"*50)

#----Punto 2----# 
class Artista (Usuario):
    def __init__ (self, entradaNombre, entradaEdad, entradaSexo, entradaNacionalidad, entradaGenero, entradaNumero, entradaAlbums, entradaCiudad):
        Usuario.__init__(self, entradaNombre, entradaEdad, entradaSexo, entradaNacionalidad)
        self.genero = entradaGenero
        self.numero = entradaNumero
        self.albums = entradaAlbums
        self.ciudad = entradaCiudad 
        print(f"El concierto se dara en la ciudad {self.ciudad}")
    def atributos (self):
        print(f"""El genero musical que canta el atrista es {self.genero}
        el numero de cancion publicadas es {self.numero}
        este artista tiene un total de {self.albums} albums
        """)
artista1 = Artista()



