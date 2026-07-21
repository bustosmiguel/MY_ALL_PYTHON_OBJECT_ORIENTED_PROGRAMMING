# MRO METHOD RESOLUTION ORDER 
# METODO DE RESOLUCIÓN DE ORDEN

# Cuál argumento llamamos al de qué clase, se repiten a veces, y ayuda a esto.
# La próxima clase que debe ser buscada en la lista con el método.
# super busca el de la clase padre, ¿pero si las 2 clase tienen el mismo método?, para eso, MRO.

#%% MRO

class A: #Creamos clase A.
    def hablar(self): #Que tenga el método hablar, igual las otras
        print("Hola, desde A")

class B(A): #Hereda de clase A
    def hablar(self):
        print("Hola, desde B")

class C(A):  #Hereda de clase A
    pass

class D(B, C): #Hereda de clase B y C.
    def hablar(self):
        print("Hola, desde D")

d = D() #d es el objeto (de la clase D)
d.hablar()
print(D.mro()) #Esto muestrael orden de búsqueda de las clases.

# MRO es cómo está conf python
# Para decir cuál tomo, cual es la clase que doy prioridad.
# Va ramificando.

A.hablar(d)
B.hablar(d)
C.hablar(d)
D.hablar(d)

# %%
