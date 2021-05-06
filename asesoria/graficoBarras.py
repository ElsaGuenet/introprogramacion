import matplotlib.pyplot as plt 
meses = ["enero", "febrero", "marso", "abril", "mayo","junio", "julio", "agosto"]
ingresos = [2000000, 1000000, 1850000, 2000000, 1500000, 1600000, 1900000, 1500000 ]
plt.bar(meses, ingresos)
print(meses, ingresos)
plt.title("Nivel de ingresos en un ano")
plt.xlabel("Meses")
plt.ylabel("Ingresos mensual en COP")
plt.savefig('graficoIngresos.png')
plt.show()