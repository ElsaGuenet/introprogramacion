Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]


#-----Preguntas-----#
PreguntaNumero = """
Hola ! Bienvenido. Por favor elije una opcion :
    1.Convertir las temperaturas a kelvin o a fahrenheit
    2.Mostrar el estado de salud del paciente según las temperaturas
    3.Mostrar temperature maxima y minima
    4.Salir
    """

PreguntaConvercion = """
Elije una opcion :  F = Mostrar las temperaturas en Fahrenheit
                    K = Mostrar las temperaturas en Kelvin
                    C = Mostrar las temperaturas originales en Celsius
                    """

#-----Mensajes-----#
MensajeFahrenheit = "Monstrando las temperaturas del paciente en Fahrenheit"
MensajeKelvin = "Monstrando las temperaturas del paciente en Kelvin"
MensajeCelsius = "La conversión no es necesaria"
MensajeEror = "Valor ingresado no valido"
MensajeHipotermia = "El paciente está hipotérmico si su temperatura es inferior a 36°C"
MensajeNormal = "El paciente tiene una temperatura normal si está entre 36 y 37.5°C"
MensajeFievre = "El paciente tiene fiebre si su temperatura es superior a 37.6°C"
Hipo = "El paciente esta hipotérmico"
Normal = "El paciente tiene una temperatura normal"
Fievre = "El paciente tiene fievre"
MensajeMax = "La temperatura maxima es :"
MensajeMin = "La temperatura minima es :"
MensajeFrecuencia = "La frecuencia con la que se tomaron los datos es :"
MensajeDespedida = "Adios, que tengas un feliz dia"


#---Convercion---#
TemperaturasFahrenheit = []
for elementos in Temperatura_Corporal:
    conversor = round((elementos*1.8)+32,3)
    TemperaturasFahrenheit.append(conversor)
TemperaturaKelvin = []
for elementos in Temperatura_Corporal:
    conversor = round(elementos+273.15,2)
    TemperaturaKelvin.append(conversor)

#----Entrada al codigo----#
OpcionEscogida = int(input(PreguntaNumero))
while(OpcionEscogida != 4):
    #---Opcion1---#
    if(OpcionEscogida == 1):
        OpcionConvercion = input(PreguntaConvercion)
        if(OpcionConvercion == "F"):
            print(MensajeFahrenheit)
            print(TemperaturasFahrenheit)
        elif(OpcionConvercion == "K"):
            print(MensajeKelvin)
            print(TemperaturaKelvin)
        elif(OpcionConvercion == "C"):
            print(MensajeCelsius)
            print(Temperatura_Corporal)
        else:
            print(MensajeEror)
    #---Opcion2---#
    elif(OpcionEscogida == 2):
        print(MensajeHipotermia)
        print(MensajeNormal)
        print(MensajeFievre)
        print( )
        for elementos in Temperatura_Corporal:
            Temperatura_Corporal_Hipo=[]
            if(elementos < 36):
                print(Hipo)
                Temperatura_Corporal_Hipo.append(elementos)
                print(Temperatura_Corporal_Hipo)
            Temperatura_Corporal_Normal=[]
            if(36 <= elementos <= 37.5):
                print(Normal)
                Temperatura_Corporal_Normal.append(elementos)
                print(Temperatura_Corporal_Normal)
            Temperatura_Corporal_Fievre = []
            if(elementos > 37.6):
                print(Fievre)
                Temperatura_Corporal_Fievre.append(elementos)
                print(Temperatura_Corporal_Fievre)
    #---Opcion3---#
    elif(OpcionEscogida == 3):
        Maximum = max(Temperatura_Corporal)
        print(MensajeMax)
        print(Maximum)
        Minimum = min(Temperatura_Corporal)
        print(MensajeMin)
        print(Minimum)
        Frecuencia = round(len(Temperatura_Corporal)/24,2)
        print(MensajeFrecuencia)
        print(Frecuencia,"por hora")
    else:
        print(MensajeEror)
    OpcionEscogida = int(input(PreguntaNumero))

print(MensajeDespedida)

