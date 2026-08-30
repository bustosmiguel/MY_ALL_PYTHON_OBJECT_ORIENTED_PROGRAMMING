#%% POLIMORFISMO POLYMORPHISM (1:30)s
# Envía mensaje sintáctico, el mensaje es el mismo, pero llega distinto porque son propiedades distintas
# 
# Tiene tipado dinámico y estáticos


# %%
class Gato: # clase gato
    def sonido(self): # método o función sonido
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
        print(animal.sonido())
    
gato = Gato()
perro = Perro()

print(gato.sonido()) # Miau
print(perro.sonido()) # Guau

hacer_sonido(perro) # Miau
# %%
