#HERENCIA
# De todo lo que tiene un estudiante, y tiene cosas nuevas.

#%% Clase padre (Clase hija es quién lo heredó)

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self): #estudiar hacen los Estudiante
        print("Estudiando...")

nombre = input(f"Dígame su nombre: ")
edad = input(f"Dígame su edad: ")
grado = input(f"Dígame su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
""")


# estudiar es  variable temporal, guarda la intención del user
estudiar = input() 

#convertir a minúsc evitando case sensitivity (error de tipeo)
if (estudiar.lower() == "estudiar"):
    estudiante.estudiar() # Llamamos al método (acción) contenido dentro del objeto.


#%%

class Ventas:
    def __init__(self, insumos, libreria, alimentos):
        self.insumos = insumos
        self.libreria = libreria
        self.alimentos = alimentos

    def Factura(self):
        print("Solo factura")   
    
insumos = input(f"¿Qué insumos comprará?: ")
libreria = input(f"¿Qué de libreria comprará?: ")
alimentos = input(f"¿Qué alimentos comprará?: ")

ventas = Ventas(insumos, libreria, alimentos)

print(f"""
VENTAS DEL MES \n\n
      insumos = {ventas.insumos} n\
      libreria = {ventas.libreria} n\
      alimentos = {ventas.alimentos} n\
      """)

Factura = input()
if(Factura.lower() == "factura"):
    ventas.Factura()
