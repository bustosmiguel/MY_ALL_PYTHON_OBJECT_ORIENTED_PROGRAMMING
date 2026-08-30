#%% POLIMORFISMO CON HERENCIA , POLIMORFISMO DE SUBTIPOS O POLIMORFISMO DE SUBCLASES (1:37)

class Animal:
    def sonido(self):
        pass    
    
class Gato(Animal): # clase gato
    def sonido(self): # método o función sonido
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
        print(animal.sonido())
    
gato = Gato()
perro = Perro()

print(gato.sonido()) # Miau
print(perro.sonido()) # Guau

hacer_sonido(perro) # Miau

print(gato.sonido()) # Miau

# %% si algo camina como un pato, es pato, si tiene un metodo llamado sonido es eso.
# si tiene la posibilidad de hacer un sonido, es un animal (1:39:45)
# No hay que relacionar las clases de ninguna forma



