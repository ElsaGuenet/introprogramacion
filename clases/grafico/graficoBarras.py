#Aqui explicaremos como hacer un grafico de barras 
import matplotlib.pyplot as plt 
lenguajes = ["py","java","dart","ts","elixir"]
encuesta = [50,10,20,10,10]
plt.bar(lenguajes, encuesta, width= 0.6, color= "y")
print(lenguajes,encuesta)
plt.bar(lenguajes, encuesta)
##########
#titulo
plt.title("lenguajes mas usados")
plt.xlabel("languajes de programacion")
plt.ylabel("% de uso de lenguajes")
plt.savefig('graficolenguajes.png')
##########
plt.show()