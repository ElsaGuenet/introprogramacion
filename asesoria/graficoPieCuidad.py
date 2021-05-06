import matplotlib.pyplot as plt
pielabels = ["Bogota", "Medellin", "Cali", "Cartagena", "Manizales"]
sizes = [7181000, 2569000, 2228000, 914552, 434403]
pieexplode = [0.1,0,0,0,0]
plt.pie(sizes, labels=pielabels, explode=pieexplode, shadow = True)

plt.title("Tamano de ciudades en Colombia")
plt.savefig("TortasCiudad.png")

plt.show()