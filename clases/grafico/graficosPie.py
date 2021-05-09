#----graficos Pie----#
import matplotlib.pyplot as plt
#---creamos los labels sizeq y explode---#
### Labels : Python, java, dart, js --> nombre porciones de torta
pielabels = ["Python", "Java", "Dart", "js"]
### Sizes = los tamanos de cada poercion de la torta
sizes = [50,25,15,10]
### Explode: que tan alejado del origen esta la torta
pieexplode = [0,0,0.2,0]

plt.pie(sizes, labels=pielabels)
#####
plt.title("Uso de lenguajes de programacion en el 2021")
plt.savefig("torasLenguaje.png")
#####
plt.show()

plt.pie(sizes, labels=pielabels, explode=pieexplode, shadow = True)
#####
plt.title("Uso de lenguajes de programacion en el 2021")
plt.savefig("torasLenguaje2.png")
#####
plt.show()

plt.pie(sizes, labels=pielabels, explode=pieexplode, shadow = True, startangle=45)
#####
plt.title("Uso de lenguajes de programacion en el 2021")
plt.savefig("torasLenguaje3.png")
#####
plt.show()
acumulador = 0
for elemento in sizes:
    acumulador += elemento

for i in range(len(pielabels)):
    pielabels[i] += "->" + str(sizes[i]/acumulador*100) + "%"
plt.pie(sizes, labels=pielabels, explode=pieexplode, shadow = True, startangle=45)
#####
plt.title("Uso de lenguajes de programacion en el 2021")
plt.savefig("torasLenguaje4.png")
#####
plt.show()