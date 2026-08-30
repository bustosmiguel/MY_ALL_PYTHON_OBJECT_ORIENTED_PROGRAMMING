# %%[INPUT Y PRINT]
# # %% [INPUT para recibir texto]


texto_ingresado = input("Escriba al texto aquí: ")
texto_ingresado

# %% PRINT para presentar texto de vuelta a un usuario (lo contrario a input)

print("Bienvenido")
print(1, 2, 3, 4, 5)
print("también puedes", "combinar", "textos y números", 1, 2, 3)


######## strings


# %% string format(f-string)
año = 2026
mes = "agosto"
print(f"estamos en el añi {año} en el mes de {mes}")


# %% strings
# métodos: txt.count(s) |
"manzana".count("a")  # cuántas veces está el string "a" en txt manzana.


# %% strings
"manzana".find(
    "a"
)  # Muestra la posición en que ocurre por primera vez el string s (si no está presente, retorna -1)

# %% strings
"manzana linda".isalpha()  # Revisa si un string solo está compuesto por letras del alfabeto (mayúsculas y minúsculas)


# %% strings
"manzana".isdigit()  # Revisa si un string solo está compuesto dígitos

# %% strings
"manzana".upper()  # Entrega una versión del string donde todos los caracteres están en mayúsculas

# %% strings
"manzana".lower()  # Entrega una versión del string donde todos los caracteres están en minúsculas


# OPERADORES MATEMATICOS Y BOOLEANOS


# %% OPERADORES MATEMÁTICOS

a = 5 + 7  # Adición
b = 12 - 2  # Sustracción
c = 2 * 4  # Multiplicación
d = 80 / 2  # División
e = 9 % 3  # MÓDULO muestra el resto
f = 7 // 3  # División entera
g = 2**3  # Potenciación


print(a, b, c, d, e, f, g)


# %% OPERADORES BOOLEANOS
# a == b verifica si "a" esigual a "b"
"hola" == 5
# %%
"hola" != "HOLA"


#
# %% OPERADORES BOOLEANOS
5 < 7  # a > b Verifica si a es menor que b
# %% OPERADORES BOOLEANOS
5 <= 5  # a <= b Verifica si a es menor o igual a b
# %% OPERADORES BOOLEANOS
5 > 7(False)  # a> bVerifica si a es mayor que b
# %% OPERADORES BOOLEANOS
5 >= 7(False)  # a >= b Verifica si a es mayor o igual que b


##### control de flujo


# %% IF PARA SOLO UNA CONDICIÓN

# controlar este comportamiento y realizar algunas acciones solo si se cumple
# alguna condición o repetir instrucciones un número determinado de veces.

# el caso de un
# programa que permite que distintos usuarios compren productos en una tienda: solo queremos realizar la
# venta si el comprador tiene dinero suficiente para pagar, y si eso no es posible queremos permitirle elegir
# otro medio de pago, hasta que logre pagar o que decida no realizar la compra.

# IF
# Si solo si se cumple una condición, usamos un bloque if.
# “ejecuta este segmento de código solo si la condición es verdadera”:

numero = 5
if numero < 10:
    print("Menor que 10")  # Sí lo imprime
if numero < 3:
    print("Menor que 3")  # No lo imprime


# %% ELIF Y ELSE

# ELIF
# Permite chequear una nueva condición y ejecutar un bloque de código si esa condición es cierta,
# tal como un bloque if.
# Sin embargo, este chequeo solo ocurrirá si es que no existe un bloque anterior cuya
# condición se haya cumplido.

# ELSE
# el bloque else nos permite declarar código que se ejecutará
# solo si ninguna de las condiciones anteriores, tanto de bloques if como elif, se ha cumplido.

numero = 10  # Primero prueba esta condición
if numero < 5:  # Primero prueba esta condición única (Por eso solo el "if")
    print("Menor que 5")
elif numero < 7:  # Solo si la anterior fue falsa, prueba esta
    print("Menor que 7")  # No lo imprime
elif numero < 9:  # Solo si la anterior también fue falsa, prueba esta
    print("Menor que 9")  # No lo imprime
else:  # Si ninguna anterior fue verdadera, ejecuta esta definitivamente
    print("Mayor que 9")

# %% ELABORACIÓN PROPIA

genero = input("¿Cuál es tu género? (Hombre/Mujer): ").strip().capitalize()
nombre = input("¿Cuál es tu nombre? ")

if genero == "Hombre":  # CONDICIÓN 1 (Condición primera)
    print("Bienvenido", nombre)
elif genero == "Mujer":  # CONDICIÓN 2 (Condición segunda)
    print("Bienvenida", nombre)
else:  # CONDICIÓN 3 (Condición distinta)
    print("Bienvenido/a", nombre)

# print() SIEMPRE DENTRO DE SU CONDICIÓN
# "nombre =" solicitarlo una vez, así evitamos duplicarlo en cada bloque
# strip().capitalize() = EVITA fallos de "espacios" o "mayúsculas".

# %% ciclo "FOR" y el concepto ITERAR

# Por ejemplo:
# si queremos imprimir un valor 3 veces o si queremos recorrer cada letra de un string,
# necesitaremos un ciclo "for".
# Python, la sentencia "for" nos permite recorrer una secuencia de un elemento a la vez ejecutando un bloque
# de código para cada elemento. A este proceso de recorrer una secuencia se le conoce como “iterar” sobre
# una secuencia.

inicio = 1
fin = 6
incremento = 2
for numero in range(inicio, fin, incremento):
    print(numero)

# %%
# PYTHON CUENTA DESDE CERO SIEMPRE
for numero in range(5):
    print(numero)

# %% ciclo WHILE

# for nos permite repetir un bloque de código una cantidad determinada de veces habrá ocasiones
# en las que no sabremos cuántas veces será necesario repetir la ejecución del bloque.
# Por ejemplo, nuestro
# programa podría requerir que una persona ingrese su nombre de usuario como un string de entre 4 y 10
# caracteres, lo que significa que debemos pedirle un nombre válido hasta que ingrese un nombre que
# cumpla con las restricciones. No sabemos, de antemano, cuántas veces se equivocará el usuario (podría ser
# cero, una o veinte veces) por lo que debemos repetir nuestro bloque de código que pide un nombre de
# usuario hasta que se cumpla una condición: que el nombre de usuario ingresado sea válido.

# Para casos en los que no sabemos cuántas veces vamos a repetir un bloque de código, utilizamos el ciclo
# while. Este ciclo requiere dos cosas: una condición a revisar y un bloque de código que se ejecutará
# mientras la condición sea verdadera. Esta condición se revisará al comienzo de cada iteración, antes de
# ejecutar el bloque de código. Para utilizar un ciclo while, utilizamos la sintaxis while condicion:, dando
# paso al código correspondiente al bloque a ejecutar hasta que condición deje de cumplirse.


nombre = input()
while len(nombre) > 10:
    print("Nombre no cumple requisitos")
nombre = input()
print(nombre)


# Control de flujo adicional
# BREAK & CONTINUE

# %% Control de flujo adicional \ BREAK & CONTINUE

# BREAK: Para el "while"
# La sentencia break nos permite detener la ejecución de un ciclo while o for de manera inmediata, en el
# punto que se encuentre la sentencia, lo que puede ser útil si determinamos que se cumplen las condiciones
# necesarias para detener todas las futuras iteraciones.

numero = 37
adivinanza = input("Adivina el número:")

while int(adivinanza) != numero:
    adivinanza = input("Intentalo de nuevo:")
    if adivinanza == "SALIR":
        break

print(numero)


# %%
# CONTINUE:
# De manera similar a break, continue nos permite modificar el flujo natural centro de un ciclo while o for.
# La diferencia es que continue detiene la iteración actual, en el punto que se encuentre la sentencia, y pasa
# inmediatamente a la siguiente iteración.

# Podemos escribir un programa que pida 3 números al usuario y los sume. Nuestra intuición es utilizar un
# ciclo for, pero ¿qué ocurre si en una de las iteraciones el usuario ingresa una letra? No podemos asumir
# que solo pediremos un input 3 veces, sino que pediremos inputs hasta haber recibido 3 números, utilizando
# un ciclo while.

# Es aquí donde continue puede ser de utilidad: si detectamos que el valor ingresado no es un dígito,
# volvemos al comienzo del bloque a pedir un nuevo valor.
suma = 0
numeros_recibidos = 0

while numeros_recibidos < 3:
    numero = input()
    if not numero.isdigit():  # Lo ingresado no es un número
        continue
    suma += int(numero)
    numeros_recibidos += 1
print(suma)


# %%
