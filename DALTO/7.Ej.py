#%% EJERCICIO DE HERENCIA 1:25

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad) #Usamos super para heredar el constructor de la clase padre (Persona) al usar super() no usamos self.
        self.grado = grado

    #def mostrar_datos(self):
        #print(f"Nombre: {self.nombre}")
        #print(f"edad: {self.edad}")

    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

estudiante = Estudiante("Juan", 24, "Décimo")
estudiante.mostrar_datos()
estudiante.mostrar_grado()

#Notas ref líne 14:
#Self no se pasa a parámetro cuandi usamos la función super(), 
#porque super ya sabe que es la clase padre, entonces no es necesario pasarle el self.
#Si no usamos super, entonces sí es necesario pasarle el self, porque no sabe que es la clase padre.



# %% AHORA ESTE EJERCICIO QUE ES MÁS FÁCIL

class Animal:
    def comer(self):
        print("El animal está comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal está Volando")

class Amamantar(Animal):
    def amamantar(self):
        print("El animal está Amamantando")

class Murcielago(Ave, Amamantar):
    pass

Murcielago = Murcielago()


ave = Ave()

ave.comer()
ave.volar()

Murcielago.comer()
Murcielago.volar()
Murcielago.amamantar()


print(Ave.mro())

#%%


