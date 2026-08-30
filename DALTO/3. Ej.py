# Ejercicio 1: Crea una clase llamada "Estudiante" con 
# atributos como "nombre", "edad" y "grado". 
# Luego, crea un objeto de esta clase e imprime su nombre.




import json
import os





#%%
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    
    def estudiar(self):
        print("Estudiando...")

pedro = Estudiante("Pedro", 23,3) # Esto de ejemplo nada más
print(pedro.edad)

nombre = input("Dígame su nombre: ") #al usar input(), siempre tendré un string.
edad = input("Dígame su edad: ")
grado = input("Dígame su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
    DATOS DEL ESTUDIANTE:  \n\n
    nombre: {estudiante.nombre} \n
    edad: {estudiante.edad} \n
    grado: {estudiante.grado} \n
""")

estudiar = input()

if (estudiar.lower() == "estudiar"):
    estudiante.estudiar() #Acá pasamos a mayúscula la primera letra cuando escriba el user.

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()





# Guardamos los datos en un archivo JSON que Linux compartirá
with open('data_bridge.json', 'w') as archivo:
    json.dump(datos_factura, archivo, indent=4)

print("🚀 Python: Datos de factura guardados en data_bridge.json")