import matplotlib.pyplot as plt

tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,8,9,10]

plt.plot(tiempo,sensor,"--",'r')
plt.show()
######
plt.title("Grafico Sensor contra el tiempo")
plt.xlabel("Tiempo(s)")
plt.ylabel("Voltaje(mV)")
plt.savefig("sensor.png")
######

diccionario = {}
diccionario['NombresEstudiantes'] = ["Jabob","Dani","Maria", "Elena"]
diccionario["EdadEstudiantes"] = [18,17,24,32]
diccionario['Peso'] = [84,56,64,57]
print(diccionario)

print(diccionario["NombresEstudiantes"][-1], diccionario["EdadEstudiantes"][-1],diccionario['Peso'][-1])
print(diccionario["EdadEstudiantes"])



