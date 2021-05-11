import matplotlib.pyplot as plt 
items = list()
prix = list()
for i in range(0,5):
	print("entrega el nombre de un snack: ")
	entradaSnackFav = input()
	print("entrega el percio de este snack: ")
	entradaPrecios = input()
	prix.append(float(entradaPrecios))
	items.append(entradaSnackFav)


# entradaSnackFav = ["mars","tobleron", "lion", "maltesers", "milka"]
# entradaPrecios = [2, 2.5, 1.6, 2.5, 1.9]
plt.bar(items,prix, color = "r")
plt.title("Precio de los cinco snacks favorito del usuario")
plt.xlabel("Snacks favoritos del usuario")
plt.ylabel("Precios en euro")
plt.savefig("graficoBarasSnack.png")
plt.show()
	
plt.bar(dic.keys(),dic.items(), color = "r")

item.append(raw_input())
item.append(float(raw_input())