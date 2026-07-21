# %% DECORADORES DECORATORS
# Toma una f(x) como entrada, le agrega una funcionalidad extra y
# devuelve como saluda la f(x) codificada.
# Es decir, la f(x) anterior MÁS las modificaciones.
# Lo mejor es que no cambia el código original de la f(x)

def decorador(funcion): #La f(x) decoradora crea una función "decorador", que pedirá como parámetro una "función".
    def funcion_modificada(): #esta es la f(x)
        print("Antes de llamar a la función") #que crea código antes
        funcion() #Acá ejecuta la función que creamos como parámetro (line 7)
        print("Después de llamar a la función") # Ejecuta un código después
    return funcion_modificada #Y nos devuelve la f(x) que nos creó # ASÍ QUE "funcion_modificada()", es la f(x)
    
# def saludo():
#     print("Hello World")

# saludo_modificado = decorador(saludo) # Para que tenga sentido, primero asignar esta variable.
# saludo_modificado

@decorador #Esto llama a 14:18, colocamos @decorador, para llamar a @decorador que esta el la line 7
def saludo(): #Y creamos esta f(x) saludo 21:22 sobre @decorador
    print("Hello World")

saludo() #Listo la f(x) es "saludo", y es una f(x) modificada

#TIP: Seleccionar lo que quiero + ctrl + k + c
# 14:18 es lo mismo que 20:24, usamos @decorador, para no escribirlo nuevamente
# En definitiva, un decorador en una f(x) que agarra una f(x), la modifica agregando funcionalidad extra antes o después de ejecutarla.


# %% tarea: invcestigar sobre:
# Decoradores de Clases
# Decoradores Múltiples.
