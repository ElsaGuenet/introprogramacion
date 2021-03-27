def conversionTemperatura(temperaturas, unidad):
    """Convierte una lista de temperaturas
    segun la unidad ingresada, puede ser...
            K --> Kelvin
            F --> Fahrenheint
    temperaturas: lista temperatura en grados centigrados
    Retorna : 

    Si se ingresa un valor invalido devolvemos None 
    Devuelve la lista convertida en las unidades deseadas
    """
    listaConvertida= []
    for temperatura in temperaturas:
        conversion = None
        if unidad == "F":
            conversion = temperatura *1.8 +32
        elif unidad == "K":
            conversion = temperatura + 273.15
        else:
            listaConvertida = None
        listaConvertida.append(conversion)
    return listaConvertida

def clasificarTemperaturas (temperaturas):
    """Retorna la clasificacion de las temperaturas ingresadas
    deben estar en grados centigrados
    """
    listaClasificacion = []
    estado = None
    for temperatura in temperaturas:
        if temperatura < 36:
            estado = "hipotermia"
        elif temperatura >= 36 and temperatura < 37.6:
            estado = "normal"
        else:
            estado = "Fiebre"
        listaClasificacion.append(estado)
        return listaClasificacion
def mostrarTopes(lista):
    mayor = round(max(lista),2)
    menor = round(min(lista),2)
    periodoHoras = round(len(lista)/24,2)
    print("La mayor temperatura es", mayor)
    print("La menor temperature es", menor)
    print("")