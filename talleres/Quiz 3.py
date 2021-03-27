import conversorTemperaturas as ct
PreguntaNumero = """ Hola! Bienvenido
                    Por favor elije una opcion:
                    1.Hacer convercion de Pesos a Dolares o Euros
                    2.Agregar una valor a la lista
                    3.Mostrar el ingreso más alto, el Ingreso más bajo 
                        y el Promedio de ingresos
                    4.Salir  
                    """
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

temperaturaCorporalFahrenheint = ct.conversionTemperatura(Temperatura_Corporal, "F")
temperaturaCorporalKelvin = ct.conversionTemperatura(Temperatura_Corporal, "K")
clasificacionTemperaturas = ct.clasificarTemperaturas(Temperatura_Corporal)
print(temperaturaCorporalFahrenheint)
print(temperaturaCorporalKelvin)
print(clasificacionTemperaturas)
