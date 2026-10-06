# ==========================================
# IMAGEN 1: PYTHON BEGINNER CHEATSHEET
# ==========================================

# 1. BASIC
# Print text
print("Hello, World!")


# 2. VARIABLES
x = 10  # int
y = 3.14  # float
name = "Sam"  # string
is_on = True  # boolean


# 3. DATA STRUCTURES
list1 = [1, 2, 3]  # List
tuple1 = (1, 2, 3)  # Tuple
set1 = {1, 2, 3}  # Set
dict1 = {"a": 1, "b": 2}  # Dictionary, se identifican los datos por un nombre


# --- 4 ESTRUCTURAS PRINCIPALES (Las más usadas) ---

# List: Secuencia ordenada y mutable. Permite elementos duplicados.
list1 = [1, 2, 3]

# Tuple: Secuencia ordenada e INMUTABLE (no se puede modificar tras crearla). Permite duplicados.
tuple1 = (1, 2, 3)

# Set: Colección desordenada de elementos ÚNICOS (sin duplicados) y mutables.
set1 = {1, 2, 3}

# Dictionary: Colección de pares clave-valor. Claves únicas e indexadas.
dict1 = {"a": 1, "b": 2}

# --- 3 ESTRUCTURAS ADICIONALES (Datos específicos y binarios) ---

# FrozenSet: Versión INMUTABLE de 'set'. No se puede alterar ni añadir elementos.
fset1 = frozenset([1, 2, 3])

# Bytes: Secuencia binaria e INMUTABLE de bytes (números del 0 al 255).
bytes1 = b"Hola"

# ByteArray: Versión MUTABLE de 'bytes'. Permite modificar sus bytes.
b_array = bytearray(b"Hola")

# 4. CONDITIONALS
if x > 5:
    print("Big")
elif x == 5:
    print("Equal")
else:
    print("Small")


# 5. LOOPS
for i in range(5):
    print(i)

while x > 0:
    x -= 1


# 6. METHODS / FUNCTIONS
def greet(name):
    return "Hi " + name


greet("Jordan")
print(greet("Jordan"))  # Hi Jordan


# 7. STRINGS
s = "Python"
print(s[0:3])  # Pyt
print(s[0:3].lower())  # pyt
print(s[0:3].upper())  # PYT


# 8. CLASSES
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("bark bark")


d = Dog("Max")
d.bark()  # bark bark


# 9. INPUT
# name = input("Enter name: ")
# print("Hello", name)


# 10. COMMON BUILT-INS
len([1, 2, 3])  # 3
type(3.14)  # <class 'float'>
range(5)  # 0, 1, 2, 3, 4


# 11. IMPORTS
import math

print(
    math.sqrt(16)
)  # 4.0 (Nota: en la imagen dice max(16), pero se corrige a math.sqrt)


# 12. FILE HANDLING
# Open file (modes: r, w, a, r+)
# f = open("file.txt", "r")
# print(f.read())
# f.close()

# Read line by line
# with open("file.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# Write to a file (overwrites)
# with open("file.txt", "w") as f:
#     f.write("Hello World!\n")

# Append to a file
# with open("file.txt", "a") as f:
#     f.write("More text\n")


# ==========================================
# IMAGEN 2: ONE SHEET CHEAT - 15+ CHEATS
# ==========================================

# 1. PRINT FORMATTING (f-strings)
name = "John Doe"
age = 21
print(f"Hi, I'm {name} and I am {age} years old.")
# Clean & readable way to format strings


# 2. LIST COMPREHENSION
squares = [x**2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]
# Short & powerful way to create lists


# 3. DICTIONARY GET()
d = {"name": "John Doe", "age": 21}
print(d.get("name"))  # John Doe
print(d.get("city", "Not Found"))  # Not Found
# Avoids KeyError


# 4. SWAP TWO VARIABLES
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
# Simple & Pythonic!


# 5. ENUMERATE()
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry


# 6. ZIP()
names = ["John", "Doe", "Smith"]
scores = [90, 85, 88]
for n, s in zip(names, scores):
    print(n, s)
# Output:
# John 90
# Doe 85
# Smith 88


# 7. LAMBDA FUNCTION
add = lambda x, y: x + y
print(add(5, 3))  # 8
# Small anonymous function


# 8. SLICING
s = "seekho.cse"
print(s[:])  # sh.e (o el string completo según el caso)
print(s[1:])  # eekho.cse
print(s[:-1])  # seekho.cs
print(s[::2])  # sekoe
print(s[::-1])  # esc.oohkees
# [start : stop : step]


# 9. SET OPERATIONS
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a | b)  # Union {1, 2, 3, 4, 5}
print(a & b)  # Intersection {3, 4}
print(a - b)  # Difference {1, 2}


# 10. CHECK IF KEY EXISTS
d = {"name": "John Doe", "age": 21}
if "name" in d:
    print("Key exists!")
else:
    print("Key not found!")
# Works for dict, list, string, set


# 11. DEFAULT VALUES
def greet_default(name="Guest"):
    print(f"Hello, {name}!")


greet_default()  # Hello, Guest!
greet_default("John")  # Hello, John!
# Default arguments in functions


# 12. UNPACKING
a, b, *rest = [1, 2, 3, 4, 5]
print(a, b)  # 1 2
print(rest)  # [3, 4, 5]
# *rest collects remaining items


# 13. USEFUL BUILT-IN FUNCTIONS
# len(x)      -> Length
# max(x)      -> Maximum
# min(x)      -> Minimum
# sum(x)      -> Sum
# sorted(x)   -> Sorted list
# type(x)     -> Data type
# round(x, n) -> Round to n digits


# 14. HANDLE EXCEPTIONS
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will run always!")
# Graceful error handling


# 15. LIST METHODS (TOP ONES)
lst = [1, 2, 3]
lst.append(4)  # [1, 2, 3, 4]
lst.pop()  # remove last
lst.insert(1, 99)  # [1, 99, 2, 3, 4]
lst.remove(2)  # remove 2
lst.clear()  # []


# BONUS CHEATS
# Comments: # single line / """ multi-line """
# input():  x = input("Enter: ")
# range():  range(1, 5) -> 1 2 3 4
# help():   help(len)


####### INSTRUCCIONES LINEALES #######
####### INSTRUCCIONES LINEALES #######
####### INSTRUCCIONES LINEALES #######


# %% LIST | ADD | REMOVE | TYPE
frutas = ["banana", "pera", "manzana", "kiwi", "sandia"]
frutas[0]  # banana
print("lista original:", frutas)  # print original list

frutas.append("naranja")  # add "naranja"
print("lista original + naranja:", frutas)

frutas[4] = "uva"  # in 5th position. (We write 4 in .py)
print("lista original + uva:", frutas)

frutas.remove("naranja")  # remove "naranja"
print("lista original - naranja:", frutas)

print(type(frutas))  # <class 'list'> type (x) shows variable class

# %% SMALL QUESTIONNAIRE PROGRAMM
print("====")
print("HELLO USER")
print("====")

nombre = input("Cual es tu nombre? ")  # input() function to get user input
edad = input("Cual es tu edad? ")
altura = input("Cual es tu altura? ")
peso = input("Cual es tu peso? ")

peso_saludable = 70  # healthy weight

print("==USER==")
print("Tu nombre es:", nombre)
print("Tu edad es:", edad, "años")
print("Tu altura es:", altura, "metros")
print("Tu peso es:", peso, "kilogramos")
print("¿Tu peso es mayor o igual a 70 kilos?:", peso_saludable)


# %% SMALL CALCULATOR PROGRAMM
numero_1 = float(input("Ingrese el primer número: "))  # input() to get user input
numero_2 = float(input("Ingrese el segundo número: "))

suma = numero_1 + numero_2
print("La suma de", numero_1, "y", numero_2, "es", suma)


# %% CALCULAR AVERAGE O PROMEDIO

nombre = input("Ingrese su nombre: ")
print("=Ingreso de notas alumno")
total = float(input("Ingrese la nota 1: "))
total += float(input("Ingrese la nota 2: "))
total += float(input("Ingrese la nota 3: "))

promedio = total / 3
print("El promedio de", nombre, "es:", round(promedio, 3))


####### CONDICIONALES #######
####### CONDICIONALES #######
####### CONDICIONALES #######
####### CONDICIONALES #######

# %% Condicional simple = IF

saldo = 150
retiro = 100
if saldo >= retiro:
    print("Retiro exitoso. Su saldo actual es:", saldo - retiro)

# %% Condicional simple = else (DE LO CONTRARIO)

stock = int(input("Ingrese la cantidad de stock disponible: "))
print("Stock disponible:", stock)

if stock > 40:
    print("Si hay stock disponible")
else:  # de lo contrario
    print("No hay stock disponible")


# %% Condicional simple = elif (SI NO, entonces SI)

nota = int(input("Ingrese la nota del alumno: "))

if nota >= 16:
    print("Excelente")
elif nota >= 14:
    print("Muy bien")
elif nota >= 12:
    print("Bien")
else:
    print("Insuficiente")


# %% OPERADORES LÓGICOS (AND, OR, NOT)
# AND:
matriculado = True
pago_realizado = True

if matriculado and pago_realizado:  # creando la condición
    print("El alumno puede acceder al curso")

# %% OPERADORES LÓGICOS (AND, OR, NOT)
# OR:
premium = False
compra = 250

if premium or compra >= 200:  # creando la condición
    print("El usuario puede acceder al descuento")


# %% OPERADORES LÓGICOS (AND, OR, NOT) | CUENTA BLOQUEADA | PREMISO PAGO ACCESO
# NOT:
cuenta_bloqueada = False
if not cuenta_bloqueada:  # creando la condición
    print("El usuario puede acceder a su cuenta")


# %% CONDICIONALES ANIDADAS (IF DENTRO DE IF)
usuario_registrado = True
suscripcion_activa = True

if usuario_registrado:
    if (
        suscripcion_activa
    ):  # se llama anidada porque esta condición está dentro del IF anterior
        print("Acceso permitido")
    else:
        print("Necesitas una suscripción activa")
else:
    print("Usuario no registrado")


# %% while loop (bucle mientras, mientras sea verdadera, se sigue ejecutando)
# repetir una parte de nuestro dódigo mientras se cumpla una condición

print("===== SISTEMA DE ACCESO =====")

usuario_correcto = "adminprueba"
clave_correcta = "123456"

intentos = 0
acceso = False

while (
    intentos < 3 and acceso == False
):  # mientras intentos sea menor a 3 y acceso sea falso

    usuarii = input("Ingrese su usuario: ")
    clavee = input("Ingrese su clave: ")

    if usuarii == usuario_correcto and clavee == clave_correcta:
        acceso = True
        print("Acceso concedido")
    else:
        intentos += 1
        print("Usuario o clave incorrecta")

        if intentos < 3:
            print("Te quedan", 3 - intentos, "intentos")

if acceso == False:
    print("Acceso denegado. Se han agotado los intentos.")

# "adminprueba"
#  "123456"
# ACCESO CONCEDDO.


# %% while true y break (bucle mientras verdadero y romper)
# break detiene el bucle, al cumplir x condición.
# siempre con while true se tiene que terminar el bucle y es con "break".

while True:
    print("\n1. Ver perfil")
    print("2. Ver cursos")
    print("3. SALIR")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("Mostrando perfil...")
    elif opcion == "2":
        print("Mostrando cursos...")
    elif opcion == "3":
        print("Saliendo del programa...")
        break  # Ahora sí funciona porque está dentro del bucle while
    else:
        print("Opción inválida. Intente nuevamente.")


# %%CONTADORES: Cuántas veces repetir una acción
# contador es una variable de llevar la cuenta de algo, hasta BREAK.
# contador con while controlamos la cantidad de veces que el código se ejecuta
# CONTADOR HACE: ES CUANTAS VECES DE REPITE
# (Y CON BREAK ES DETENERLO)

intentos = 0
while intentos < 3:
    clave = input("Ingrese la clave: ")

    if clave == "1234":
        print("Acceso concedido")
        break  # Salir del bucle si la clave es correcta

    intentos += 1
print("Intentos agotados. Acceso denegado.")

# %% CONTINUE
# si recorremos una lista de producto, podemos ignorar :
# los productossin stock
# CONTINUE HACE:
# # NO EJECUTES ESTO EN ESTA VUELTA Y PASA A LA SIGUIENTE.
# CONTINUE HACE: SALTA LA VUELTA ACTUAL

numero = 0
while numero < 10:  # while se ejecuta al ser menor que 10
    numero += 1  # en cada vuelta aumentamos el contador en 1

    if (
        numero == 5
    ):  # pero cuando llega a 5 se cumple esta condición. ## o t% 2 == 0:  # Si el número es par
        continue  # Saltar a la siguiente iteración, salta la vuelta y continua con la siguiente

    print("numero", numero)  # y el número 5 NO APARECE.


# %% BLUCLE FOR ("para" repetir una acción y recorre elementos uno por uno).
# PARA: Repetir una acción en una cantidad determinada de veces.
# con FOR lo hacemos mucho más sencillo.

for numero in range(1, 6):
    print("numero", numero)  # imprime del 1 al 5
# CON FOR: no hay más números y termina automáticamente.
# (Mientras que con WHILE: numeros del 1 al 5 con while se pone un contador hasta controlar la condición, y con FOR no es así, NO)
# WHILE REPITE UNA CONDICIÓN MIENTRAS QUE SEA VERDADERA.
# FOR, PYTHON RECORRE ÚNICAMENTE LOS ELEMENTOS QUE LE INDICAMOS.
# (Por eso es util for cuando SABEMOS CUANTAS VECES QUEREMOS REPETIR UNA ACCIÓN, y con while es más útil cuando NO SABEMOS CUANTAS VECES SE VA A REPETIR, y depende de una condición que se cumpla o no))
# CON FOR TAMBIÉN PODEMOS REPETIR TEXTOS, LISTAS Y MÁS.

# RECORDAR:
# - while: Repite mientras una condición sea verdadera.
# - for: Recorre elementos uno por uno.

# AMBOS SOM ÚTILES, PERO DEPENDE DEL PROBLEMA QUE QUERAMOS RESOLVER, USAREMOS UNO U OTRO.

# %% RANGE: Controlar las repeticiones.
# usar RANGE con FOR
# range: hace la secuencia de números

for numero in range(1, 6):  # del 1 al 5
    print("numero", numero)

for numero in range(5):  # Acá cuando colocamos solo un número python comienza desde ese
    print("numero", numero)

for numero in range(0, 11, 2):  # colocamos solo un número python comienza desde ese
    print("numero", numero)


# %% ####################### EJERCICIO : ANALIZADOR DE NÚMEROS #######################

# cuales son pares e impares y llevar la cuenta
pares = 0  # contador de números pares
impares = 0  # contadorde números impares
suma_pares = 0  #
suma_impares = 0  #

for numero in range(1, 21):  # analizar los números del 1 al 20
    print("\nAnalizando número:", numero)  #
    if numero % 2 == 0:  # si el número es par
        print("El número es par")  #

        pares += 1  # contador de pares
        suma_pares += numero  #


# %% LISTAS

# esto puede ser tedioso:
nombre1 = "Carlos"
nombre2 = "Ana"
nombre3 = "Pedro"
nombre4 = "Luis"
nombre5 = "María"
# ... hacerlo con miles así, sería cansador

# para esto existe la LISTA:
# 1 variable NOMBRES con 5 ELEMENTOS:
# ÍNDICE: Python cuenta desde CERO, donde se dice: Carlos índice CERO, Ana índice UNO.

nombres = ["Carlos", "Ana", "Pedro", "Luis", "María"]
print(nombres[3])

for nombre in nombres:
    print("Hola", nombre)


# %% LEN es longitud, oermite saber cuantos elementos tiene una lista.

frutas = ["manzana", "platano", "naranja", "fresa"]
print(len(frutas))

# len muestra cuantos elementos tiene una lista: 4 elementos (Las frutas)

for i in range(len(frutas)):
    # len frutas muestra elementos de la lista / range geenra los índices que recoreremos: PYTHON PASA POR CERO, 1, 2 Y 3--
    print("índice", i)
    print("Fruta:", frutas[i])

# %% LEN es longitud
nombre = "Carlos"
print(len(nombre))  # 6 letras o seis elementos.


########### OPERADOR IN:
########### OPERADOR IN:
########### OPERADOR IN:
########### OPERADOR IN:
########### OPERADOR IN:

### "IN"        :   Comprueba que un elemento SI existe.
### "NOT IN"    :   Comprueba que un elemento NOexiste.

######## AMBOS ENTREGAN UN BOOLEANO: TRUE OR FALSE.


# %% OPERADOR IN
# Si naranja existe en la lista fruta.
# Aquí solo reconoce mayúsculas:
fruta = ("Zandia", "Manzana", "Plátano", "Naranja")
print("Naranja" in fruta)


# %% en caso de cambiar a mayúsculas y minúsculas, aquí las reconoce:

fruta = ("Zandia", "Manzana", "Plátano", "Naranja")
# Texto a buscar (puede estar en mayúsculas, minúsculas o mezclado)
busqueda = "naranja"
# Convertimos a minúsculas la búsqueda y cada elemento de la tupla
encontrado = busqueda.lower() in (f.lower() for f in fruta)
print(encontrado)  # Imprime: True

# %% lo mismo que lo anterior, pero más rápido:

fruta = ("Zandia", "Manzana", "Plátano", "Naranja")
print("naranja" in str(fruta).lower())  # Imprime: True
# %%
fruta = ("Zandía", "Plátano")
# Le aplicas .lower() a lo que buscas Y a la tupla
print("Zandía".lower() in str(fruta).lower())  # Imprime: True


### LO ANTERIOR CON "IF":

# %% RESPETANDO EL FORMATO COMO ESTÁ "naranja"

frutas = ["manzana", "pera", "frutilla", "naranja"]
fruta = input("¿Qué fruta buscas? ")

if fruta in frutas:
    print("La fruta está en la LISTA")
else:
    print("No se encuentra en la LISTA")

# %% MAYÚSCULAS Y MINUSCULAS "NaRaNjA"

frutas = ["manzana", "pera", "frutilla", "naranja"]

# Convertimos lo que escribe el usuario a minúsculas de inmediato
fruta = input("¿Qué fruta buscas? ").lower()

# Convertimos la lista temporalmente a texto en minúsculas para comparar
if fruta in str(frutas).lower():
    print("La fruta está en la LISTA")
else:
    print("No se encuentra en la LISTA")


# %%

# Podemos entonces, ver si:
# - Un producto existe
# - Si un usuario está registrado
# - Si una palabra está dentro de una lista
# - VALIDAR OPCIONES DE UN PROGRAMA


# %% "NOT IN" para revisar lo contrario.
frutas = ["manzana", "pera", "frutilla", "naranja"]
# Convertimos lo que escribe el usuario a minúsculas de inmediato
fruta = "naranja"

if fruta not in frutas:
    print("Esa fruta no está en la lista")


##########SITUACIÓN REAL EN CÓDIGO
##########SITUACIÓN REAL EN CÓDIGO
##########SITUACIÓN REAL EN CÓDIGO
##########SITUACIÓN REAL EN CÓDIGO
##########SITUACIÓN REAL EN CÓDIGO


# %%


# Definición de listas con los datos del inventario
productos = [
    "Mouse",
    "Teclado",
    "Monitor",
    "HMDI",
    "LAPTOP",
]  # Lista con los nombres de los productos
precios = [21, 33, 23, 22, 11]  # Lista con los precios correspondientes
stock = [
    2122,
    3223,
    4332,
    1212,
    1120,
]  # Lista con las cantidades disponibles de cada producto

# Bucle principal del programa que se repetirá hasta que el usuario decida salir
while True:
    print("\n==tiendas==")  # Imprime el encabezado del menú
    print("1. Ver productos")  # Opción 1: Muestra el catálogo
    print("2. Comprar")  # Opción 2: Proceso de compra
    print("3. Salir")  # Opción 3: Finaliza el programa

    opcion = input(
        "Selecciona una opción: "
    )  # Solicita al usuario ingresar el número de opción

    if opcion == "1":  # Si elige la opción 1
        print("\n--- Catálogo de Productos ---")  # Encabezado del catálogo
        for i in range(
            len(productos)
        ):  # Recorre la lista usando las posiciones (índices)
            print(
                f"{productos[i]} - Precio: S/.{precios[i]} - Stock: {stock[i]}"
            )  # Muestra producto, precio y stock actual

    elif opcion == "2":  # Si elige la opción 2 (Comprar)
        producto = input(
            "¿Qué producto desea comprar? "
        )  # Pregunta el nombre del producto deseado

        if (
            producto not in productos
        ):  # Revisa si el producto NO está en la lista de productos
            print(
                "Producto no encontrado"
            )  # Advierte al usuario si escribió mal el producto
            continue  # Vuelve al inicio del bucle `while` sin ejecutar el resto del código

        posicion = productos.index(
            producto
        )  # Encuentra la posición (índice) del producto en la lista
        cantidad = int(
            input("Cantidad: ")
        )  # Pide la cantidad deseada y la convierte a número entero

        if (
            cantidad <= 0
        ):  # Evalúa si la cantidad ingresada es un número negativo o cero
            print("Cantidad invalida")  # Alerta sobre la cantidad no válida
        elif (
            cantidad > stock[posicion]
        ):  # Compara la cantidad pedida con el stock disponible en esa posición
            print(
                "Stock insuficiente"
            )  # Alerta si el usuario pide más de lo que hay guardado
        else:  # Si la cantidad es válida y hay suficiente stock
            subtotal = (
                precios[posicion] * cantidad
            )  # Calcula el precio total multiplicando precio por cantidad
            stock[
                posicion
            ] -= cantidad  # Descuenta la cantidad comprada del stock actual

            print("Compra realizada")  # Confirma que la transacción se concretó
            print("total S/.", subtotal)  # Muestra el monto final a pagar

    elif opcion == "3":  # Si elige la opción 3
        print("¡Gracias por su visita!")  # Muestra mensaje de despedida
        break  # Rompe el bucle `while` y finaliza el programa

    else:  # Si ingresa cualquier opción diferente de 1, 2 o 3
        print(
            "Opción no válida, intente de nuevo."
        )  # Maneja entradas incorrectas del usuario
# %%


########## FUNCIONES EN PYTHON
########## FUNCIONES EN PYTHON
########## FUNCIONES EN PYTHON
########## FUNCIONES EN PYTHON
########## FUNCIONES EN PYTHON
########## FUNCIONES EN PYTHON

# %%

# TAREA PARA REALIZAR VARIAS VECES,PARA ESO USAMOS F(X) LA FUNCIÓN.
# DEF indica a python que vamos a definir una f(x) función.
# después escribimos el nombre de la función con paréntesis y ":".
# donde:
# - def         = definición de la f(x)
# - nombre      = nombre de la f(x)
# - ":"         = Para comenzar el bloque de instrucciones.
# - Identación  = Indica qué código pertenece a la función.


def saludar():
    print("Hola, Bienvenido")


# %%

# llamamos a la función, utilizando su nombre:
# python ejecutará las instrucciones que están dentro:

saludar()


# %%


def mostrar_menu():  # función mostrar_menu()
    print("\n ####TIENDA####")
    print("1. Ver Productos")
    print("2. Comprar")
    print("3. Salir")


def mostrar_productos():  # función mostrar_productos()
    productos = ["laptop", "mouse", "monitor", "hdmi", "headphones"]

    print("\n PRODUCTOS")

    for i in range(len(productos)):
        print(i + 1, productos[i])


# %% lo nterior con while true podemos separar cada tarea:

while True:
    mostrar_menu()

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_productos

    if opcion == "2":
        print("Aquí realizamos una compra")

    elif opcion == "3":
        print("Programa finalizado")
        break
    else:
        print("Opción no válida")


####### FUNCIONES CON PARÁMETROS
####### FUNCIONES CON PARÁMETROS
####### FUNCIONES CON PARÁMETROS
####### FUNCIONES CON PARÁMETROS
####### FUNCIONES CON PARÁMETROS
####### FUNCIONES CON PARÁMETROS
####### FUNCIONES CON PARÁMETROS
####### FUNCIONES CON PARÁMETROS
# donde:
# - Parámetro: es la información que nuestra función espera recibir.
# - Y el valor que colocamos cuando llamamos a la función es el dato que le estamos enviando.
# - ASÍ LAS F(X) SEAN MÁS ÚTILES Y REUTILIZABLES.

# %% FUNCIONES CON PARÁMETROS
# Cómo hacer que nuestra f(x) reciba información?
# QUE NUESTRA F(X) TRABAJE CON DIFERENTES DATOS
# ESTA F(X) PERMITE ÚNICAMENTE SALIDAR A CARLOS


def saludar():
    print("Hola Carlos")


# %%
saludar()


# %% PERO SI QUIERO SALUDAR A OTRA PERSONA?, PARA ELLO, LOS PARÁMETROS:

# function definition:
# def add(a, b):
# return a + b

# function call:
# add(2 + 3)

# un parámetro es un dato que enviamos a nuestra función para que trabaje con el.
# la estructura sería "nombre" como parámetro:


def saludar(nombre):  # PARAMETRO "nombre".
    print("Hola", nombre)


saludar("Carla")
saludar("Miguel")

# %% Dado esto, no crearemos una f(x) diferente para cada producto:


def mostrar_producto(nombre, precio, stock):

    print("\n -----PRODUCTO------")
    print("nombre: ", nombre)
    print("precio: S/.", precio)
    print("stock: ", stock)


mostrar_producto("Laptop", 2500, 30)
mostrar_producto("Mouse", 2500, 30)
mostrar_producto("Monitor", 2500, 30)

# podemos reutilizar este código con información diferente


####### return
####### return
####### return
####### return
####### return
# donde:
# - parámetros  =Permiten enviar datos a una función
# -return       = Permite devolver el resultado para utilizarlo en otra parte en nuestro programa
# -print        = muestra información en pantalla


# %%


def calcular_total(precio, cantidad):  # LA F(X) REALIZA LA OPERACIÒN
    total = (
        precio * cantidad
    )  # PERO EL RESULTADO SE ENCUENTRA DENTRO DE ELLA. # acá realiza el cálculo
    return total  # Y SE SACA ESE RESULTADO CON RETURN () (O permite devolver un valor de nuestra función) # acá devuelve el resultado que se guarda en *total (abajo)


producto = "Mouse"
precio = 20
cantidad = 12

total = calcular_total(precio, cantidad)  # *total
# guardamos el resultado de lo anterior en este "total".
print("Producto", producto)
print("Cantidad", cantidad)
print("Total S/.", total)

if total >= 200:
    print("Tienes envío gratis")
else:
    print("Debes pagar adicional por el envío")

# IMPORTANTE | IMPORTANTE | IMPORTANTE:
# Entonces: Una f(x) puede recibir info mediante parámetros, y devolver información mediante return()

# DESDE AHORA NUESTRAS FUNCIONES PERMITIRAN:
# - procesar cálculos
# - Entregar información


####### PRINT, STR(),  CONCATENACIÓN (+) y FORMATO STRING (f)
####### PRINT, STR(),  CONCATENACIÓN (+) y FORMATO STRING (f)
####### PRINT, STR(),  CONCATENACIÓN (+) y FORMATO STRING (f)
####### PRINT, STR(),  CONCATENACIÓN (+) y FORMATO STRING (f)
####### PRINT, STR(),  CONCATENACIÓN (+) y FORMATO STRING (f)

# print() = mostrar información
# str() = Convertir valor a texto
# Operador concatenar "+"= Une textos y variables
# Formato String f"" = Insertar variables dentro de un texto, y es más claro que concatenar con "+"

# PRINT:
# Permite mostrar información:
# - información en la consola
# - mostrar el contenido de una variable.

# CONCATENAR:
# Con "+" unimos textos y variables
# Y mostramos como solo un mensaje.

# F-STRING:
# Cuando es mucha info, es mejor f-string que concatenar.

# %%

nombre = "Carlos"
curso = "Python"
edad = 40

print("hola soy " + nombre + ", y tengo " + str(edad))

# donde la variable numércica debe estructurarse con str()

# PERO CUANDO SON MUCHAS CONCATENACIONES CON "+", es mejor hacerlo con:
# F-STRING:

# %% F STRING (FORMAT STRING)
# cuando convertimos los números a texto

print(f"hola {nombre}")  # al usar f-string, las variables van con corchetes.
print(f"Hola, {nombre}, y tengo {edad}")  # F-STRING FACILITA Y MEJOR QUE CONCATENAR

# %% fstring también podemos utilizar variables dentro de las llaves:
precio = 32112
cantidad = 22

print(f"El total es: S/. {precio * cantidad}")

# %% SI LO ANTERIOR LO HACEMOS A UNA TIENDA:
producto = "Mouse"
precio = 80
cantidad = 3

total = precio * cantidad

print("######compra######")
print(f"Producto: {producto}")
print(f"Precio: S/.{precio}")
print(f"Cantidad: {cantidad}")
print(f"Total: S/. {total}")


# fstrings:
# combinamos texto, variables y números de una forma más limpia y fácil de leer.

# si las tuplas nos ayudasn a almacenar datos que NO queremos modificar
# y hemos trabajado en datos para identificar mediante posiciones.
# con los diccionarios, los encontramos por su nombre, almacenando una clave y un valor.

#### Diccionario
#### Diccionario
#### Diccionario
#### Diccionario
# Dictionary, se identifican los datos por un nombre:
# {} LLAVES ES DICCIONARIO.
# .keys() CLAVES IDENTIFICA EL DATO
# .values() VALOR ES LA INFORMACIÓN ALMACENADA
# DICCIONARIO["CLAVE"] NOS PERMITE ACCEDER AL VALOR.

# %%

alumno = {"nombre": "Carlos", "edad": 19, "curso": "python"}

print(alumno)
# para acceder a un dato, es mediante clave:

print(alumno["nombre"])
print(alumno["curso"])

# la ventaja de los diccionarios es que se pueden modificar los valores:

alumno["edad"] = 20
print(alumno["edad"])

# se pueden agregar nuevos datos, utilizando una clave:
# se agrega tiktok al diccionario con la clave "carlos_12";

alumno["tiktok"] = "carlos_12"
print(alumno)

if "nombre" in alumno:
    print("El nombre está registrado")

# Ahora si almacenamos información de un producto:


# %%

producto = {"Nombre": "Mouse", "Precio": 19, "Stock": 22}


print(f"Producto: {producto['Nombre']}")
print(f"Precio: S/. {producto['Precio']}")
print(f"Stock: {producto['Stock']}")


####### RECORRER DICCIONARIOS CON FOR EN PYTHON
####### RECORRER DICCIONARIOS CON FOR EN PYTHON
####### RECORRER DICCIONARIOS CON FOR EN PYTHON
####### RECORRER DICCIONARIOS CON FOR EN PYTHON
####### RECORRER DICCIONARIOS CON FOR EN PYTHON
# ÚTIL CUANDO HAY MUCHA INFO Y NO SABEMOS CUANTOS DATOS TENDREMOS

# for clave in diccionario: Recorre las claves
# diccionario[clave]:Obtiene el valor correspondiente
# print(f"{clave}: {usuario[clave]}")  Muestra de forma sencilla: claves y valores


# %% RECORRER DICCIONARIOS CON FOR EN PYTHON
# Si tenemos esto o muchos datos, tendríamos que escribir un print() para cada uno
# Podemos utilizar el ciclo "for" para recorrer un diccionario:

# Ejemplo del ciclo "for": recorre CLAVES del diccionario, las muestra una por una:


# %%
producto = {"Nombre": "Mouse", "Precio": 19, "Stock": 22}


# %% MUESTRA TODAS LAS CLAVES
for clave in producto:
    print(clave)  # (Sin hacer print() a cada una)

# %% MUESTRA TODOS LOS VALORES
for clave in producto:
    print(producto[clave])  # (Sin hacer print() a cada uno)


# %% EN VEZ DE HACERLO MANUALMENTE...

usuario = {"nombre": "Carlos", "edad": 20, "lenguaje": "python"}
print(usuario["nombre"])
print(usuario["edad"])
print(usuario["lenguaje"])  # TODO ESTO ES HACER PRINT A CADA UNO

# %% ... EL CICLO "FOR" RECORRE TODO EL DICCIONARIO DA CLAVES Y SUS VALORES.
for clave in usuario:
    print(f"{clave}: {usuario[clave]}")


########### .KEYS(), .VALUES() y .ITEMS() EN DICCIONARIOS
########### .KEYS(), .VALUES() y .ITEMS() EN DICCIONARIOS
########### .KEYS(), .VALUES() y .ITEMS() EN DICCIONARIOS
########### .KEYS(), .VALUES() y .ITEMS() EN DICCIONARIOS
########### .KEYS(), .VALUES() y .ITEMS() EN DICCIONARIOS
# A VECES CUANDO TRABAJAMOS CON DICCIONARIOS SOLO NECESITAMOS:

# 1. .keys() SOLAMENTE LAS CLAVES
# 2. .values() SOLAMENTE LOS VALORES
# 3. .items() CLAVES Y VALORES.

# CON: .keys()

# %% volvemos al diccionario simple:

producto = {"Nombre": "Mouse", "Precio": 19, "Stock": 22}

# %% .key:

print(producto.keys())  # MUESTRA LAS CLAVES QUE EXISTEN DENTRO DEL DICCIONARIO


# %% O SE PUEDEN RECORRER UTILIZANDO EL CICLO FOR()

for clave in producto.keys():
    print(clave)  # recorre únicamente las claves...

# %% ... pero si queremos valores:

for valor in producto.values():
    print(valor)  # recorre únicamente las claves...

# %% .values() ENTREGA LAS CLAVES Y SUS VALORES CORRESPONDIENTES:

usuario = {"nombre": "Carlos", "edad": 20, "lenguaje": "python"}

for clave, valor in usuario.items():
    print(f"{clave}:{valor}")


######## EVITA ERRORES CON GET() EN PYTHON
######## EVITA ERRORES CON GET() EN PYTHON
######## EVITA ERRORES CON GET() EN PYTHON
######## EVITA ERRORES CON GET() EN PYTHON

# 1.- diccionario["clave"] : Accede directamente al valor, o muestra ERROR.

# 2.- diccionario.get("clave"): Obtiene valor sin generar ese ERROR.

# 3.- get("clave", "valor") : Permite establecer un valor alternativo si la clave NO existe.
# (como sin existencias, etc. categoría no registrada, etc.)
# %% EVITA ERRORES CON GET() EN PYTHON
usuario = {"nombre": "Carlos", "edad": 20, "lenguaje": "python"}

print(usuario.get("Carlos"))
print(usuario.get("nombre"))
print(
    usuario.get("correo"), "Correo no registrado"
)  # si la clave "correo" no existe que diga esto-

# %%

producto = {"nombre": "laptop", "cantidad": 332, "precio": 154}


nombre = producto.get("nombre", "producto desconocido")
categoria = producto.get("categoria", "categoría no registtrada")

# %%

print(f"Producto = {nombre}")
print(f"Producto = {categoria}")
# como categoria no existe, py solo proporciona los existentes que es laptop
# esto permite trabajar diccionarios de una manera mucho más segura.


######## MODIFICAR ELIMINAR DATOS DE UN DICCIONARIO
######## MODIFICAR ELIMINAR DATOS DE UN DICCIONARIO
######## MODIFICAR ELIMINAR DATOS DE UN DICCIONARIO
######## MODIFICAR ELIMINAR DATOS DE UN DICCIONARIO
######## MODIFICAR ELIMINAR DATOS DE UN DICCIONARIO
######## MODIFICAR ELIMINAR DATOS DE UN DICCIONARIO
# MODIFICAR Y ELIMINAR DATOS DE NUESTROS DICCIONARIOS
# NOS DA MUCHO CONTROL SOBRE LA INFORMACIÓN QUE ALMACENAMOS.

# .update() PARA:
# editar/agregar una nueva clave

# .pop() PARA:
# eliminar una clave y su valor

# diccionario["clave"] = valor PARA:
# Modificar directamente un valor.


# %% MODIFICAR Y ELIMINAR DATOS DE NUESTROS DICCIONARIOS

producto = {"Nombre": "Mouse", "Precio": 19, "Stock": 22}

# PODEMOS CAMBIAR EL VALOR DE UNA CLAVE:
# PODEMOS CAMBIAR EL value() DE UNA keys():

producto["precio"] = 90


# %%
producto.update({"precio": 100, "stock": 322})

# %%
# tambien par una nueva clave, que se llame categoría:
producto.update({"categoría": "accesorios"})


# %% # .pop() para eliminar una clave:
producto.pop("stock")

# %% PODEMOS GUARDAR EL VALOR ELIMINADOQUE ERA "STOCK", AHORA SE GUARDA:
# solo la elimina si la clave existe obviamente.
# por eso antes de modificar el diccionario, ver qué valores tengo.

producto = {"nombre": "mouse", "precio": 19, "stock": 22}

stock = producto.pop("stock")
print(f"stock eliminado:{stock}")
print(producto)


########## MÉTODO CLEAR: ELIMINA TODO EN EL DICCIONARIO, CUIDADO CON CLEAR().
########## MÉTODO COPY: CREAR UNA COPIA DE TODO EL DICCIONARIO.

# CLEAR
# %% CLEAR BORRA TODO EN EL DICCIONARIO

usuario = {"nombre": "Carlos", "edad": 20, "lenguaje": "python"}

# %% CLEAR BORRANDO TODO EN EL DICCIONARIO
usuario.clear()


# COPY
# %% COPI COPIA TODO EN NUESTRO DICCIONARIO

usuario = {"nombre": "Carlos", "edad": 20, "lenguaje": "python"}


# %% usuario_COPIA

usuario = {"nombre": "Carlos", "edad": 20, "lenguaje": "python"}

# %%

usuario_copia = usuario.copy()
# %%

print(usuario_copia)

# %%


############ diccionarios dentro de diccionarios
############ diccionarios dentro de diccionarios
############ diccionarios dentro de diccionarios
############ diccionarios dentro de diccionarios
############ diccionarios dentro de diccionarios
# GUARDAR MÁS INFO DENTRO DE UN MISMO DATO
# INFO MAS ORGANIZADA COMO CATEGORIA Y DATOS DEL PROVEEDOR
# ASÍ COLOCAR OTRO DICCIONARIO DENTRO DEL PRIMERO

# %%

producto = {
    "nombre": "COMPUTADOR",
    "precio": 1000,
    "stock": 2112,
    "proveedor": {"nombre": "NET", "ciudad": "EEUU"},
}


print(producto["proveedor"]["nombre"])
print(producto["proveedor"]["ciudad"])

# %% CAMBIAR A CHILE


producto = {
    "nombre": "COMPUTADOR",
    "precio": 1000,
    "stock": 2112,
    "proveedor": {"nombre": "NET", "ciudad": "EEUU"},
}


producto["proveedor"]["ciudad"] = "Chile"


# %%
print(producto["proveedor"]["nombre"])
print(producto["proveedor"]["ciudad"])


###### DICCIONARIO ANIDADO: ES DICCIONARIO CON OTROS DICCIONARIOS.
#### CON MAYOR INFORMACIÓN ORGANIZADA
###### DICIONARIO CON OTROS DICCIONARIOS ES: DICCIONARIO ANIDADO.
###### ORGANIZAMOS POR NIVELES.
### sobretodo para trabajar con API´s, BBDD, etc.

# diccionario["clave"]["otra_clave"] Accedemos a datos internos.

# %%

productos = {
    "producto1": {"nombre": "monitor", "precio": 900},
    "producto2": {"nombre": "laptop", "precio": 2333},
}
# %%

print(productos["producto1"]["nombre"])
print(productos["producto2"]["precio"])


###### LISTAS DENTRO DE DICCIONARIOS
###### LISTAS DENTRO DE DICCIONARIOS
###### LISTAS DENTRO DE DICCIONARIOS
###### LISTAS DENTRO DE DICCIONARIOS
# SI AHORA EL PRODUCTO TIENE:
# VARIOS COLORES Y CARACTERÍSTICAS.
# GUARDAREMOS VARIOS VALORES DENTRO DE 1 CLAVE.

# Una nota diferenciadora para claridad
# con diccionarios organizamos la info con claves y valores.
# con listas guardamos varios elementos dentro de una de esas claves .


# %%


producto = {
    "nombre": "COMPUTADOR",
    "precio": 1000,
    "colores": ["negro", "blanco", "rojo"],
}


# %% llamar a elemntos utilizando sus índices:

print(producto["colores"][0])
print(producto["colores"][1])

# %% llamar ALL elemntos con el ciclo for:

for color in producto["colores"]:
    print(color)

# %% Agregar nuevos elementos: ASI LLEGAR A 4 COLORES

producto["colores"].append("azul")

# %% OTRO EJEMPLO:

estudiante = {
    "nombre": "Javier",
    "edad": 26,
    "cursos": ["python", "java", "javascript"],
}

# %% Acceder al primer curso, el primero es cero:

print(estudiante["cursos"][0])

# %% Acceder a todos los cursos

for curso in estudiante["cursos"]:
    print(curso)


###### VARIOS DICCIONARIOS DENTRO DE UNA LISTA:
###### VARIOS DICCIONARIOS DENTRO DE UNA LISTA:
###### VARIOS DICCIONARIOS DENTRO DE UNA LISTA:
###### VARIOS DICCIONARIOS DENTRO DE UNA LISTA:
###### VARIOS DICCIONARIOS DENTRO DE UNA LISTA:

# %%

productos = [
    {"nombre": "monitor", "precio": 433},
    {"nombre": "teclado", "precio": 33},
    {"nombre": "teclado", "precio": 33},
]

print(productos[2])  # al diccionario número 3
print(productos[2]["nombre"])  # solo al nombre del número 3


# %% Como tenemos varios, podemos recorrerlos con ciclo for()

for producto in productos:
    print(producto["nombre"])


#
# %% AHORA PARA UN SISTEMA: UNA LISTA CON VARIOS DICCIONARIOS

productos = [
    {"nombre": "teclado", "precio": 900},
    {"nombre": "monitor", "precio": 300},
    {"nombre": "lápices", "precio": 20},
]

print("=====PRODUCTOS=====")

for producto in productos:
    print(f"{producto["nombre"]} -USD {producto["precio"]}")


# %% AHORA BUSCAR INFO DE ESA LISTA QUE TIENE 3 DICCIONARIOS.

for producto in productos:
    if producto["nombre"] == "lápices":
        print(producto)


# %%


for producto in productos:
    if producto["nombre"] == "lápices":
        print(f"El producto es: USD {producto["precio"]}")
# %% condiciones , para búsquedas útiles.

for producto in productos:
    if producto["precio"] > 100:  # muestra solo >100 usd.
        print(producto["nombre"])

# %%

busqueda = "lápices"

for producto in productos:
    if producto["nombre"] == busqueda:
        print(f"Producto encontrado: {producto["nombre"]}")
        print(f"Precio USD{producto["precio"]}")


### ordenar con sort
### ordenar con sort
### ordenar con sort

### varios productos ordenados por precios:


# %%
#### key: dato que vamos a ordenar para registrar
productos = [
    {"nombre": "teclado", "precio": 900},
    {"nombre": "monitor", "precio": 300},
    {"nombre": "lápices", "precio": 20},
]

productos.sort(key=lambda producto: producto["precio"])

for producto in productos:
    print(f"{producto["nombre"]} USD {producto["precio"]}")


# ahora al revés:
# %%ahora al revés:
# con reverse = True.
# sort ordena la lista
# key indica a python qué dato debe utilizar para ordenar
# reverse = True (Invierte el orden)


productos.sort(key=lambda producto: producto["precio"], reverse=True)
for producto in productos:
    print(f"{producto["nombre"]} USD {producto["precio"]}")


###### qué es lambda
###### qué es lambda
###### qué es lambda
###### qué es lambda
###### qué es lambda
# map escribe una operación
# lambda: Permite escribir esa operación de forma corta
# list(): convierte el resultado en una lista.

# %% SIN LAMBDA SIN LAMBDA SIN LAMBDA SIN LAMBDA SIN LAMBDA
#  SIN LAMBDA


def doble(numero):
    return numero * 2


doble(5)

# %% con lambda
# CON LAMBDA:

doble = lambda numero: numero * 2
doble(5)

# %%

# cuando se usó lambda en unos 20 lineas atrás, era:
productos.sort(key=lambda producto: producto["precio"])

# porque creó una función pequeña llamada "producto" y sencilla en una línea-

# %%
######### MAP, aplica una operación a todos los elementos:

precios = [
    132,
    322,
    3222,
    322,
    322,
    322,
    221,
    231,
    544,
    654,
    132,
    322,
    3222,
    322,
    322,
    322,
    221,
    231,
    544,
    654,
]


# %%

nuevos_precios = map(lambda precio: precio + 5, precios)


# %%

print(nuevos_precios)

# %%
# CONVERTIRLOS EN UNA LISTA:
# CONVERTIRLOS EN UNA LISTA:

nuevos_precios = list(map(lambda precio: precio + 5, precios))

# %%
print(nuevos_precios)
# %%


numeros = [
    132,
    322,
    3222,
]


resultado = list(map(lambda numero: numero * 2, numeros))
print(resultado)
# %%
precios_con_igv = list(map(lambda precio: precio * 1.19, precios))

print(precios_con_igv)
# %%


######## FILTRAR DATOS CON FILTER
######## FILTRAR DATOS CON FILTER
######## FILTRAR DATOS CON FILTER
######## FILTRAR DATOS CON FILTER
# map = transforma datos
# filter = filtra datos
# filtra los elementos que únicamente cmplen esa condición
# y mezclando ambos con lambda, se puede manipular mejor los datos.

# %%
# LISTA DE PRECIOS:

precios = [32, 23, 22, 31, 54, 620]
# se puede hacer if para las condiciones, pero igual se
# puede con filter, y esta es la estructura de filter:
# filter(condicion, lista)

# %%
resultado = filter(lambda precio: precio > 100, precios)
print(resultado)  # Esto NO sirve, debe llevar list:
# con list nuevamente se transforma a una lista:

# %% llevamos el resultado a una lista, con list:

print(list(resultado))


### segundo ejemplo:

# %%

productos = [
    {"nombre": "lápiz", "precio": 89},
    {"nombre": "teclado", "precio": 89},
    {"nombre": "audífonos", "precio": 109},
    {"nombre": "monitor", "precio": 289},
]


# %%

productos_over_100 = list(filter(lambda producto: producto["precio"] > 100, productos))

# %%

for productos in productos_over_100:
    print(f"{producto["nombre"]} usd. {producto["precio"]}")


##### REDUCE / TRABAJAR CON LISTAS
##### REDUCE / TRABAJAR CON LISTAS
##### REDUCE / TRABAJAR CON LISTAS
##### REDUCE / TRABAJAR CON LISTAS
##### Tomar varios elementos y combinarlos, hasta obtener un solo resultado.
# map() transforma elementos
# filter() selecciona elementos
# reduce() combina elementos hasta obtener un solo resultado


# %%

from functools import reduce

# %% ejemplo simple

numeros = [2, 3, 4]  # podemos sumarlos con un ciclo, o utilizando reduce:
total = reduce(lambda a, b: a * b, numeros)
print(total)

# %% ejemplo en algún negocio


precios = [23, 34, 5, 66]

total = reduce(lambda a, b: a + b, precios)

print(f"El total de la compra es: USD {total}")


###### CONJUNTOS O SET {}
# PARA ALMACENAR DATOS ÚNICOS, SIN REPETICIONES
# NO PERMITE ELEMENTOS DUPLICADOS
# AUNQUE ESCRIBAMOS DOS VECES DIAMOND, EL CONJUNTO SOLO CONSERVA UNA
# util cuando tenemos datos petetitivos y solo queremos los datos únicos.
# igual se puede agregar elementos utilizando .add() y eliminar con .remove()
# set() Almacena elementos únicos
# add() Agrega un elemento
# remove() Elimina un elemento
# in (Comprueba si un elemento existe)


# %%

jewels = {"diamond", "ruby", "emerald", "diamond"}
print(jewels)  # solo muestra una vez diamond, aunque lo escribamos dos veces

jewels.add("sapphire")  # agrega un nuevo elemento
print(jewels)

jewels.remove("ruby")  # elimina un elemento
print(jewels)

if "diamond" in jewels:
    print("Diamond is in the set")  # verifica si un elemento está en el conjunto


# %%

productos_vistos = {"laptop", "mouse", "monitor", "laptop", "mouse"}
print(productos_vistos)  # solo muestra una vez cada producto, aunque se repitan


# %% si los recorremos con el ciclo for:

for producto in productos_vistos:
    print(producto)


###### CONJUNTOS O SET {} ENCONTRANDO ELEMENTOS EN COMUN ENTRE ELLOS
###### intersection() = elementos en común
###### union() = combina los elementos de ambos conjuntos
###### difference() = elementos que están en un conjunto, pero no en el otro
#### todo lo anterior permite comparar conjuntos y ver qué elementos tienen en común, cuáles son diferentes, etc.

# %% Si queremos saber qué productos tienen ambos clientes:

primero = {"laptop", "tecado Dell", "computador"}
segundo = {"mouse", "tecado pro", "computador"}

a = primero.intersection(segundo)
print(a)

# %% UNE AMBOS CONJUNTOS, PERO SIN REPETICIONES:

b = primero.union(segundo)
print(b)

# %% QUÉ ELEMENTO TIENE UN CONJUNTO, PERO NO EL OTRO:

c = primero.difference(segundo)
print(c)


# COMPRENSIÓN DE LISTAS ES: es crear nuevas listas
# Escribímos código de una forma mucho más corta y fácil de leer, para crear listas.
# Escribímos código de una forma mucho más corta y fácil de leer, para crear listas.
### COMPRENSIÓN DE LISTAS EN PYTHON | LIST COMPREHENSION
### COMPRENSIÓN DE LISTAS EN PYTHON | LIST COMPREHENSION
### COMPRENSIÓN DE LISTAS EN PYTHON | LIST COMPREHENSION
### COMPRENSIÓN DE LISTAS EN PYTHON | LIST COMPREHENSION
### COMPRENSIÓN DE LISTAS EN PYTHON | LIST COMPREHENSION
### COMPRENSIÓN DE LISTAS EN PYTHON | LIST COMPREHENSION
### COMPRENSIÓN DE LISTAS EN PYTHON | LIST COMPREHENSION
### COMPRENSIÓN DE LISTAS EN PYTHON
# %%

lista = [1, 2, 3, 4, 5]
dobles = []

for numero in lista:
    dobles.append(numero * 2)

print(dobles)


# %% Lo anterior, pero de una forma más fácil:
dobles = [numero * 2 for numero in lista]
print(dobles)

# "[numero * 2" ....NUMERO POR DOS, lo que queremos GUARDAR.
# "for numero in lista]" ....DE DONDE VAMOS A OBTENER LOS ELEMENTOS
## BASICAMENTE SIGNIFICA:
# CREA UNA LISTA CON EL DOBLE DE CADA NUMERO DE LA LISTA NÚMEROS
# TAMBIÉN PODEMOS CREAR UNA CONDICIÓN:

# %%
# TAMBIÉN PODEMOS CREAR UNA CONDICIÓN, NÚMEROS PARES:
pares = [numero for numero in lista if numero % 2 == 0]
print(pares)  # CREA UNA LISTA CON LOS NÚMEROS PARES DE LA LISTA NÚMEROS

# %%
# TAMBIÉN PODEMOS CREAR UNA CONDICIÓN: NÚMEROS MAYORES A 3:
mayores_a_tres = [numero for numero in lista if numero > 3]
print(mayores_a_tres)  # CREA UNA LISTA CON LOS NÚMER

# %% TODO LO ANTERIOR A ALGO MÁS REALISTA:

precios = [23, 34, 5, 66, 12, 90, 100, 200]
precios_top = [precio for precio in precios if precio > 50]
print(precios_top)  # CREA UNA LISTA CON LOS PRECIOS MAYORES A 50


# COMPRENSIÓN DE DICCIONARIOS ES: es crear nuevos diccionarios
# Escribímos código de una forma mucho más corta y fácil de leer, para crear diccionarios.
# Escribímos código de una forma mucho más corta y fácil de leer, para crear diccionarios.
###### COMPRENSIÓN DE DICCIONARIOS EN PYTHON | DICTIONARY COMPREHENSION
###### COMPRENSIÓN DE DICCIONARIOS EN PYTHON | DICTIONARY COMPREHENSION
###### COMPRENSIÓN DE DICCIONARIOS EN PYTHON | DICTIONARY COMPREHENSION
###### COMPRENSIÓN DE DICCIONARIOS EN PYTHON | DICTIONARY COMPREHENSION
###### COMPRENSIÓN DE DICCIONARIOS EN PYTHON | DICTIONARY COMPREHENSION
###### COMPRENSIÓN DE DICCIONARIOS EN PYTHON | DICTIONARY COMPREHENSION
###### COMPRENSIÓN DE DICCIONARIOS EN PYTHON | DICTIONARY COMPREHENSION
###### COMPRENSIÓN DE DICCIONARIOS EN PYTHON | DICTIONARY COMPREHENSION

# %% CREAR LISTA DE PRODUCTOS, DONDE CADA PRODUCTO TENGA UN CÓDIGO:

products = ["car", "motor", "laptop", "mouse", "headphones"]

# esto es largo...
inventario = {}

for producto in products:
    inventario[producto] = "DISPONIBLE"

print(inventario)  # CREA UN DICCIONARIO CON CÓDIGOS PARA CADA PRODUCTO
# %%

# por eso se utiliza...

inventario = {producto: "DISPONIBLE" for producto in products}

# donde:
# "producto: " ES LA CLAVE
# "DISPONIBLE" ES EL VALOR
# "for producto in products" INDICA DE DONDE OBTENEMOS LOS DATOS.

print(inventario)  # CREA UN DICCIONARIO CON CÓDIGOS PARA

# %% TAMBIÉN SE PUEDE CREAR VALORES DISTINTOS PARA CADA ELEMENTO.

precios = [23, 34, 5, 66, 12, 90, 100, 200]
precios_igv = {precio: precio * 1.19 for precio in precios}
print(precios_igv)  # CREA UN DICCIONARIO CON LOS PRECIOS Y SUS VALORES CON IGV


# %% TAMBIÉN SE PUEDE CREAR UNA CONDICIÓN:

precios = [232, 323, 3332, 432]

precios_top = {precio: precio * 1.19 for precio in precios if precio > 300}

print(precios_top)


############### ENUMERATE RECORRER LISTAS
############### ENUMERATE RECORRER LISTAS
############### ENUMERATE RECORRER LISTAS
############### ENUMERATE RECORRER LISTAS
############### ENUMERATE RECORRER LISTAS
# Hasta ahora para RECORRER LISTAS, se ha utilizado el bucle for()
# AHORA, CON NUMERATE, TENDREMOS SU POSICIÓN
# ENUMERATE: NOS DA LA POSICIÓN Y EL ELEMENTO
# , stat = PERMITE COMENZAR EN 1.

# %%

frutas = ["manzana", "banana", "naranja", "pera"]
position = 0

for fruta in frutas:
    print(position, fruta)
    position += 1  # incrementa la posición en 1 , es un contador manual.


# %% PERO CON ENUMERATE, SE FACILITA LO ANTERIOR:

frutas = ["manzana", "banana", "naranja", "pera"]

for position, fruta in enumerate(frutas):
    print(position, fruta)  # enumerate() nos da la posición y el elemento de la lista

# AHORA TENEMOS LA "POSICIÓN DE ELEMENTO, 0, 1, 2, 3 etc." Y "FRUTA".
# en python COMIENZA desde CERO.
# Si queremos que comience desde 1, se puede agregar "start = 1"

# %% "start = 1"

for position, fruta in enumerate(frutas, start=1):
    print(position, fruta)


# %%
menu_tienda = {"comida_1", "comida_2", "comida_3", "comida_4", "comida_5"}

for numero, producto in enumerate(menu_tienda):
    print(numero, producto)  # enumerate() nos da la posición y el elemento de la lista


# %% y lo anterior, pero que comience en 1:

menu_tienda = {"comida_1", "comida_2", "comida_3", "comida_4", "comida_5"}

for numero, producto in enumerate(menu_tienda, start=1):
    print(numero, producto)  # enumerate() nos da la posición y el elemento de la lista


######### RECORRER DOS LISTAS AL MISMO TIEMPO CON ZIP
######### RECORRER DOS LISTAS AL MISMO TIEMPO CON ZIP
######### RECORRER DOS LISTAS AL MISMO TIEMPO CON ZIP
######### RECORRER DOS LISTAS AL MISMO TIEMPO CON ZIP
# zip = UNIR TEMPORALMENTE LOS ELEMENTOS DE DOS O MÁS LISTAS
# zip relaciona el primer elemento de una lista con el primero de la otra lista.
# zip recorre varias listas al mismi tiempo, trabajando con datos relacionados de forma más sencilla.

# %%
productos = ["A", "B", "C", "D"]
precios = [223, 2211, 547, 99]
stock = [22, 33, 44, 55]


for producto, precio, stock in zip(productos, precios, stock):
    print(f"{producto}: USD {precio} - Cantidad: {stock}")


# %% TAMBIÉN CON ZIP, CREAMOS DICCIONARIO:

productos = ["A", "B", "C", "D"]
precios = {12, 3, 4, 57}

inventario = dict(zip(productos, precios))
print(inventario)


# COMPROBAR CONDICIONES EN UNA LISTA CON ANY() Y ALL()
# COMPROBAR CONDICIONES EN UNA LISTA CON ANY() Y ALL()
# COMPROBAR CONDICIONES EN UNA LISTA CON ANY() Y ALL()
# COMPROBAR CONDICIONES EN UNA LISTA CON ANY() Y ALL()
# ANY() - DEVUELVE True SI AL MENOS UNO CUMPLE LA CONDICION
# ALL() - DEVUELVE True SI TODOS CUMPLEN LA CONDICION

# %%

numeros = [1, 2, 3, 4, 50, 33, 21]

resultado = any(numero > 10 for numero in numeros)

print(resultado)  # True, porque hay un número mayor a 10 en la lista

# %%
resultado = any(numero > 1000 for numero in numeros)
print(resultado)


# %% PERO CON ALL() TODOS LOS ELEMENTOS CUMPLEN CON UNA CONDICIÓN
resultado = any(numero == 33 for numero in numeros)

print(resultado)


# %% SI TODOS LOS PRODUCTOS TIENEN STOCK DISPONIBLE:

resultado = any(numero > 0 for numero in numeros)

print(resultado)


####### MIN , MAX Y SUM EN PYTHON
####### MIN , MAX Y SUM EN PYTHON
####### MIN , MAX Y SUM EN PYTHON
####### MIN , MAX Y SUM EN PYTHON


# %%
mumeros = [2, 3, 4, 2, 2, 2, 42, 1, 1, 34, 1000]
menor = min(mumeros)

print(f"El número menor es: {menor}")


# %%

maximo = max(mumeros)

print(f"El número máximo es: {maximo}")

# %%


suma = sum(mumeros)

print(f"El total es: {suma}")


# %%

precios = [23, 34, 5, 66, 12, 90, 100, 200]

precio_menor = min(precios)
precio_mayor = max(precios)
total = sum(precios)
promedio = total / len(precios)


print(f"El precio menor es: {precio_menor}")
print(f"El precio mayor es: {precio_mayor}")
print(f"El total es: {total}")
print(f"El promedio es: {promedio}")


########SORTED

# %%

numeros = [2, 3, 4, 2, 2, 2, 42, 1, 1, 34, 1000]
ordenados = sorted(numeros)
print(ordenados)  # ordena de menor a mayor


# %% DE MENOR A MAYOR

ordenados = sorted(numeros, reverse=True)
print(ordenados)


# %%
productos = ["Z", "B", "C", "D"]
ordenados = sorted(productos)
print(ordenados)  # ordena de menor a mayor


# %%

productos = ["Z", "B", "C", "D"]
ordenados = sorted(productos, reverse=True)
print(ordenados)  # ordena de menor a mayor

# %% AHORA, SI TENEMOS UNA LISTA DE PRODUCTOS CON SUS PRECIOS, Y QUEREMOS ORDENARLOS POR PRECIO:

productos = [
    {"nombre": "teclado", "precio": 900},
    {"nombre": "monitor", "precio": 300},
    {"nombre": "lápices", "precio": 20},
]

productos_ordenados = sorted(productos, key=lambda producto: producto["precio"])

for producto in productos_ordenados:
    print(f"{producto['nombre']} - USD {producto['precio']}")

# %% lambda nos permite utilizar qué valor para ordenar


for producto in productos_ordenados:
    productos_ordenados = sorted(
        productos, key=lambda producto: producto["precio"], reverse=True
    )

for producto in productos_ordenados:
    print(f"{producto['nombre']} - USD {producto['precio']}")

# %%

# sort(), modifica la lista original y
# sorted , crea una nueva lista ordenada, o devuelve una nueva lista ordenada.
# reverse true, ordena de forma descendente, de mayor a menor.
# key = indica que valor utilizar para ordenar


numeros = [20, 45, 55]
resultado = sorted(numeros)

print(numeros)
print(resultado)  # crea una nueva lista ordenada, sin modificar la original


####### INSISTANCE EN PYTHON
####### INSISTANCE EN PYTHON
####### INSISTANCE EN PYTHON
####### INSISTANCE EN PYTHON
####### INSISTANCE EN PYTHON
# DATOS CRECEN PERO NECESAITAMOS SABER QUÉ TIPO DE DATO ESTAMOS RECIBIENDO.
# INSISTANCE: Comprueba si un dato pertenece a un determinado tipo.
# int: números enteros
# float : números decimales
# str: texto
# list: lista
#
# %%

dato = 300

isinstance(dato, int)


# %%

edad = 25
print(isinstance(edad, int))  # True

# %% pero si lo cuadamos entre comillas, es texto:

edad = "25"
print(isinstance(edad, int))  # False

# %%

nombre = "Hellen"
print(isinstance(nombre, str))  # True

# %%

precio = 43
productos = ["teclado", "monitor", "lápices"]

print(isinstance(precio, int))  # True
print(isinstance(productos, list))  # True
print(isinstance(productos, dict))  # False
print(isinstance(precios, float))  # False


# %%

datos = [33, "mouse", 33, "teclado", ("laptop", 33), {"nombre": "Carlos"}]

for dato in datos:
    if isinstance(dato, int):
        print(f"{dato} es un número entero")
    elif isinstance(dato, str):
        print(f"{dato} es un texto")
    elif isinstance(dato, tuple):
        print(f"{dato} es una tupla")
    elif isinstance(dato, dict):
        print(f"{dato} es un diccionario")
    else:
        print(f"{dato} es de otro tipo de dato")


# %%

datos = [33, "mouse", 33, "teclado", ("laptop", 33), {"nombre": "Carlos"}]

for dato in datos:
    if isinstance(dato, int):
        print(f"{dato} es un número entero")
    elif isinstance(dato, str):
        print(f"{dato} es un texto")
    elif isinstance(dato, tuple):
        print(f"{dato} es una tupla")
    elif isinstance(dato, dict):
        print(f"{dato} es un diccionario")
    else:
        print(f"{dato} es de otro tipo de dato")
