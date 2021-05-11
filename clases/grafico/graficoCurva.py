import pandas as pd
import matplotlib.pyplot as plt
ecgData = pd.read_csv("ecg.csv", encoding="UTF-8", header=0, delimiter=";").to_dict()
muestra = list(ecgData["muestra"].values())
print(muestra)
voltaje = list(ecgData["valor"].values())
print(voltaje[-10:])
plt.plot(muestra, voltaje)
plt.title("resultado del ECG")
plt.show()

