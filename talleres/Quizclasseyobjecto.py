#----Punto 3----#

class Pagina ():
    """Esta es la clase pagina, muestra en la pantalla 
        Tipo de contenido 
        Formato 
        Fecha de publicacion
        """ 
    def __init__ (self,entradaContenido, entradaFormato, entradaFecha):
        self.contenido = entradaContenido
        self.Formato = entradaFormato
        self.Fecha = entradaFecha
    def atributos (self):
        print(f"""El tipo de contenido de esta pagina es {self.contenido}
                el formato es {self.Formato}
                la fecha de publicacion es {self.Fecha}
                """)

pagina1 = Pagina ("Reggaeton", "mp3", "2021")
pagina1.atributos()


#-----Punto 3---#

class Favoritos (Pagina):
    def __init__ (self,entradaContenido, entradaFormato, entradaFecha, entradaFavoritos, entradaFechaActualisacion):
        Pagina.__init__(self, entradaContenido, entradaFormato, entradaFecha)
        self.Favoritos = entradaFavoritos
        self.FechaActualisacion = entradaFechaActualisacion
    def nueva (self, nombreCancion, fechaCancion):
        self.cancion = nombreCancion 
        