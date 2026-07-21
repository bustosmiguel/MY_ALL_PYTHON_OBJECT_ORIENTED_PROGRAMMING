# GETTER & SETTER

# Con GETTERS accedemos a propiedades
# Con SETTERS modificamos propiedades

#%% 
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

mb = Persona("Miguel", 40)
print(mb.edad)



# %% ESTE ES UN GETTER (FILA 24 def get_nombre(self)...)
class Persona:
    def __init__(self, nombre, edad):
        self._nombre =nombre # ._ VA
        self._edad = edad  #._ VA
    

    def get_nombre(self): # Getter es una f(x) que llama al nombre, getter hace referencia a una f(x) que accede a un valor privado (lineas 18 o 19) de una clase.
        return self._nombre

mb = Persona("Miguel", 40) # El objeto "mb" de la clase "Persona"

nombre = mb.get_nombre() # Accede a la propiedad que está privada llamada "get_nombre" y la almacena en "nombre"
print(nombre)




# %% ESTE ES UN SETTER (FILA 24 def set_nombre(self)...)

class Persona:
    def __init__(self, nombre, edad):
        self._nombre =nombre # ._ VA
        self._edad = edad  #._ VA

    def get_nombre(self): # Getter es una f(x) que llama al nombre, getter hace referencia a una f(x) que accede a un valor privado (lineas 18 o 19) de una clase.
        return self._nombre
    
    def set_nombre(self, new_name): # Creas una f(x) llamada set_nombre, que nos pida (self) un "new_name".
        self._nombre = new_name # Y ese "new_name" será establecido a la variable "self.nombre".
    
    #o sea self.nombre (39), va a ser igual a lo que le pasemos a new_name (42)

# también esto:
mb = Persona("Miguel", 40) # El objeto "mb" de la clase "Persona"
nombre = mb.get_nombre() # Obtuvimos el nombre mb. con get_nombre()
print(nombre) #Lo mostramos en pantalla

# lo podemos cambiar:

mb.set_nombre("MABS") # CAMBIAMOS EL NOMBRE A "MABS"


nombre = mb.get_nombre() #A "nombre" mb. le colocamos la propiedad get_nombre
print(nombre)



# %%