
# HERENCIA MÚLTIPLE

#%% HERENCIA MÚLTIPLE multiple inheritance es cuando una clase hereda de dos o más clases.

class Persona: #Esta es clase uno, clase persona
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self): #Esta es clase dos, clase persona puede HABLAR
        print("Hola, estoy hablando un poco")



class Artista: # Esta es clase uno, un artista.
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self): #Esta es clase dos, artista que muestra HABILIDAD
        return f"Mi habilidad es: {self.habilidad}" #Y este es un método (return: lo que nos devuelva el llamado sea el return)


# Esta clase es el ejemplo de la herencia múltiple, porque (leer los # abajo)
class EmpleadoArtista(Persona, Artista): # Define un método constructor, que permita heredar ciertas propiedades: (Además propiedades salario y empresa)
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad) #De persona vamos a heredar nombre, edad y nacionalidad.
        Artista.__init__(self, habilidad) 
        self.salario = salario #Propiedad
        self.empresa = empresa #Propiedad

    def presentarse(self): #Si quiero heredar mostrar_habilidad hago estas dos líneas:
        print(f'Hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')

roberto = EmpleadoArtista("Miguel", 40, "chileno", "R y Python", "RD", 50000)
roberto.presentarse()

# %%