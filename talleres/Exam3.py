#----Punto1----#
import matplotlib.pyplot as plt 
# entradaSnackFav = []
# entradaPrecios = []
# snack = input("Por favor entra tus cinco snacks favoritos: ")
# precio = float(input("Por favor entra los precios de los cinco snacks: "))
# for i in range (0,snack):
#     elemento= input()
#     entradaSnackFav.append(elemento)
# for i in range (0, precio):
#     elemento= float(input())
#     entradaPrecios.append(elemento)

entradaSnackFav = ["mars","tobleron", "lion", "maltesers", "milka"]
entradaPrecios = [2, 2.5, 1.6, 2.5, 1.9]
plt.bar(entradaSnackFav, entradaPrecios, color = "r")
plt.title("Precio de los cinco snacks favorito del usuario")
plt.xlabel("Snacks favoritos del usuario")
plt.ylabel("Precios en euro")
plt.savefig("graficoBarasSnack.png")
plt.show()


#----Punto 2----#
import matplotlib.pyplot as plt 
ciudadFavoritas = ["Medellin", "Rome", "Berlin", "Paris", "Barcelone"]
poblacionesCiudad = [2.569, 2.873, 3.645, 2.161, 1.62]
pieExplode = [0,0.2,0,0,0]
plt.pie(poblacionesCiudad, labels= ciudadFavoritas, explode=pieExplode, shadow = True)
plt.title("Los cinco ciudades favoritas y sus poblacion")
plt.savefig("graficoPieCiudad.png")
plt.show()


#----Punto 3----#
definicionECG = "Un ecg es el resultado del registro de los fenómenos eléctricos del corazón."
definicionPPG = "Un ppg es un método de medición óptica que determina las variaciones volumétricas de la circulación sanguínea"
print(definicionECG)
print(definicionPPG)

import pandas as pd
import matplotlib.pyplot as plt
ecgData = pd.read_csv("ecg.csv", encoding="UTF-8", header=0, delimiter=";").to_dict()
muestra = list(ecgData["muestra"].values())
voltaje = list(ecgData["valor"].values())
plt.plot(muestra, voltaje)
plt.title("resultado del ECG")
plt.savefig("Grafico ECG.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
ppgData = pd.read_csv("ppg.csv", encoding="UTF-8", header=0, delimiter=";").to_dict()
muestra = list(ppgData["muestra"].values())
valor = list(ppgData["valor"].values())
plt.plot(muestra, valor)
plt.savefig("Grafico PPG.png")
plt.title("resultado del PPG")
plt.show()