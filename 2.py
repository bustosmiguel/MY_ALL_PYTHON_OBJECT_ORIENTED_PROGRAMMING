#%%Clases y objetos

class Celular():
    marca = "SAMSUNG"
    modelo = "S23"
    camara = "48MP"

celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()
print(celular2.modelo)

#%%Atributos de instancia (o propiedades de instancia)
class Celular(): # Método constructor porque construye la clase
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
celular1 = Celular("SAMSUNG", "S23", "48MP")
celular2 = Celular("IPHONE", "14", "48MP")
    
print(celular2.marca)

# %% FUNCIÓN O MÉTODOS
def funcionxd(xd):
    print(xd)

funcionxd("Hola jajaja")
# %% Creando funciones llamar y cortar:
class Celular(): # Método constructor porque construye la clase
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self): #f(x) llamar
        print("Estás haciendo un llamado")

    def cortar(self): #f(x) cortar
        print("Has cortado la llamada")

celular1 = Celular("SAMSUNG", "S23", "48MP")
celular2 = Celular("IPHONE", "14", "48MP")

print(celular2.llamar())
print(celular2.cortar())


# %% Lo anterior, pero conn un f string {}

class Celular(): # Método constructor porque construye la clase
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self): #f(x) llamar
        print(f'Estás haciendo un llamado desde un: {self.modelo}')

    def cortar(self): #f(x) cortar
        print(f'Has cortado la llamada desde tu: {self.modelo}')

celular1 = Celular("SAMSUNG", "S23", "48MP")
celular2 = Celular("IPHONE", "14", "48MP")

print(celular2.llamar())
print(celular2.cortar())
# %%
