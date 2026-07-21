#%%Clases y objetos

class Celular():
    marca = "SAMSUNG" #Marca es un atributo de celular1, celular2, celular3, celular4.
    modelo = "S23"
    camara = "48MP"

# atributos estáticos, fijas
celular1 = Celular() #esto es un objeto, "este objeto es una instancia de la clase "Celular"(class Celular), es el resultado de haberlo creado en la clase, cuando instanceamos una clase, es un objeto, de la clase (class Celular)
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()
print(celular2.modelo)

#%%Atributos de instancia (o propiedades de instancia)
class Celular(): 
    def __init__(self, marca, modelo, camara):# Método constructor porque construye la clase
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
celular1 = Celular("SAMSUNG", "S23", "48MP")
celular2 = Celular("IPHONE", "14", "48MP")
    
print(celular2.marca) #celular2.marca me devuelve la variable, el valor de marca que es IPHONE

# %% FUNCIÓN O MÉTODOS
def funcionxd(xd):
    print(xd)

funcionxd("Hola jajaja")
# %% Creando funciones llamar y cortar:
class Celular(): 
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





# %% P
class Networks():
    def __init__(self, Access_Point, Switch, Load_Balancing):
        self.Access_Point = Access_Point
        self.Switch = Switch
        self.Load_Balancing = Load_Balancing
    
    def signal(self):
        print(f'Wireless Distribution: {self.Access_Point}')

ap = Networks("Ruckus", "Cisco", "Mikrotik")
switch = Networks("Ruckus", "Cisco", "Mikrotik")
LB = Networks("F5", "ELFIQ", "OTHER")

print(ap.signal())

# %% P
class Networks():
    def __init__(self, access_point, controller, load_balancing):
        self.access_point = access_point
        self.controller = controller
        self.load_balancing = load_balancing

    def signal(self):
        print(f'Señal buena:{self.controller}')

ap = Networks("A", "B", "c")
c = Networks("D", "E", "F")
lb = Networks("G", "H", "I")

print(c.signal())










# %%

class Games:
    def __init__(self, chess, cards, puzzle):
        self.chess = chess
        self.cards = cards
        self.puzzle = puzzle
    def PlayGames(self):
        print("It´s time to play this game")

class PastTimes (Games):
    def __init__(self, chess, cards, puzzle, running, weights):
        super().__init__(chess, cards, puzzle)
        self.running = running
        self.weights = weights

class TableGames (Games):
    def __init__(self, chess, cards, puzzle, monopoly, catan):
        super().__init__(chess, cards, puzzle)
        self.monopoly = monopoly
        self.catan = catan
JulietaPrefers = Games("Ajedrez", "AnimalCards", "Rompecabezas")
print(JulietaPrefers.chess)
#Escenario A: Usando la clase hija TableGames
mi_mesa = TableGames("Pro", "Poker", "1000pcs", "Classic", "Expansión")
print(mi_mesa.chess)    # Salida: Pro (Heredado de Games)
print(mi_mesa.monopoly) # Salida: Classic (Propio de TableGames)
mi_mesa.PlayGames()     # Salida: It´s time to play this game (Heredado de Games)
#Escenario B: Usando la clase hija PastTimes
hobbies = PastTimes("Blitz", "Uno", "Sudoku", "10km", "20kg")
print(hobbies.running)  # Salida: 10km
print(hobbies.puzzle)   # Salida: Sudoku
#
# %% gemini tip
# Herencia Múltiple REAL
# Es cuando una clase nace de dos padres distintos Deporte y Juego:
class Deporte:
    def entrenar(self):
        print("Entrenando...")

class Juego:
    def jugar(self):
        print("Jugando...")

# ESTO es herencia múltiple (Hereda de dos clases distintas)
class AjedrezPro(Deporte, Juego):
    pass

pro = AjedrezPro()
pro.entrenar() # Viene de Deporte
pro.jugar()    # Viene de Juego


# %%





class Games:
    def __init__(self, chess, cards, puzzle, **kwargs): # **kwargs catches any extra named arguments
        self.chess = chess
        self.cards = cards
        self.puzzle = puzzle
        # Note: we don't need to handle kwargs here, but we accept them
    
    def PlayGames(self):
        print("It's time to play this game!")

class TableGames(Games):
    def __init__(self, monopoly, catan, **kwargs): # First, take what's unique to TableGames
        super().__init__(**kwargs) # Then, send the rest to the Parent Class (Games)
        self.monopoly = monopoly # Specific attribute
        self.catan = catan # Specific attribute
