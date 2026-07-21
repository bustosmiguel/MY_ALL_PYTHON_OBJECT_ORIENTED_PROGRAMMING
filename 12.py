#%% DECORADOR PROPERTY (PROPERTY DECORATOR)


class Persona:
    def __init__(self, nombre, edad):
        self._nombre =nombre
        self._edad = edad

    @property
    def get_nombre(self): # Getter es una f(x) que llama al nombre, getter hace referencia a una f(x) que accede a un valor privado (lineas 18 o 19) de una clase.
        return self._nombre
    
    # Al usar @property, no hace falta usar mb.get_nombre():

mb = Persona("Miguel", 40) # El objeto "mb" de la clase "Persona"
nombre = mb.get_nombre # Obtuvimos el nombre mb. con get_nombre(), pero al usar @property (line 9), ahora nos queda como si fuera una propiedad
print(nombre)



# %%
