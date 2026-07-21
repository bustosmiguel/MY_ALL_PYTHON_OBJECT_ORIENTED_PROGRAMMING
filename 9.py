#%% ENCAPSULAMIENTO ENCAPSULATION
# proteger metodos, proteger clases, propiedades que nisiquiera el desarrollador puede acceder a ellas, solo la clase puede acceder a ellas

class MiClase:
    def __init__(self):
        self._atributos_privados = "Valor" # Con ese guión bajo _, le decimos a py que tiene un atributo que es privado.

objeto = MiClase()
print(objeto._atributos_privados) #OBJETO... PUNTO... PROPIEDAD A LA QUE QUEREMOS ACCEDER (O MÉTODO QUE QUEREMOS EJECUTAR)


# Con GETTERS accedemos a propiedades
# Con SETTERS modificamos propiedades







# %% AL COLOCAR DOS GUIONES JUNTOS __ SON ATRIBUTOS MUY MUY PRIVADOS: (1:51)

class MiClase:
    def __init__(self):
        self.__Satributos_privados = "Valor" # Con ese guión bajo _, le decimos a py que tiene un atributo que es privado.

objeto = MiClase()
print(objeto.__Satributos_privados)

# %%
