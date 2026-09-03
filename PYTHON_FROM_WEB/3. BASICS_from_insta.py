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
dict1 = {"a": 1, "b": 2}  # Dictionary


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


# %%
