Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

MensajeHipotermia = "El paciente está hipotérmico si su temperatura es inferior a 36°C"
MensajeNormal = "El paciente tiene una temperatura normal si está entre 36 y 37.5°C"
MensajeFievre = "El paciente tiene fiebre si su temperatura es superior a 37.6°C"
Hipo = "El paciente esta hipotérmico"
Normal = "El paciente tiene una temperatura normal"
Fievre = "El paciente tiene fievre"

print(MensajeHipotermia)
print(MensajeNormal)
print(MensajeFievre)
for elementos in Temperatura_Corporal:
    Temperatura_Corporal_Hipo=[]
    if(elementos < 36):
        print(Hipo)
        Temperatura_Corporal_Hipo.append(elementos)
        print(Temperatura_Corporal_Hipo)
    Temperatura_Corporal_Normal=[]
    if(36 < elementos < 37.5):
        print(Normal)
        Temperatura_Corporal_Normal.append(elementos)
        print(Temperatura_Corporal_Normal)
    Temperatura_Corporal_Fievre = []
    if(elementos > 37.6):
        print(Fievre)
        Temperatura_Corporal_Fievre.append(elementos)
        print(Temperatura_Corporal_Fievre)
