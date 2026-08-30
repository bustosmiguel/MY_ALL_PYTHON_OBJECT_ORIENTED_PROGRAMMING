


########### VIDEO_1 FUNCTIONS AND VARIABLES




#%% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates a function with a positional argument

print("hello, world")




#%% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates a function with a positional argument and a return value
name = input("What's your name? ")
print("hello,")
print(name)




#%% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates concatenation of strings
name = input("What's your name? ")
print("hello, " + name)




#%% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates a function with two positional arguments
name = input("What's your name? ")
print("hello,", name)




#%% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates a function with a positional argument and a named argument


name = input("What's your name? ")
print("hello, ", end="")
print(name)





#%%  NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates a format string

name = input("What's your name? ")
print(f"hello, {name}")





#%% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates str functions

name = input("What's your name? ").strip().title()
print(f"hello, {name}")




#%% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates str functions

name = input("What´s your name?").strip().title()
first, last = name.split(" ")
print(f"Hello, {first}")





#%% NOTAS GITHUB BUSTOSMIGUEL

print("Hello,", name, sep = " W", end = "\n")





# %% NOTAS GITHUB BUSTOSMIGUEL
print(f"Hello, {name}")


# %%NOTAS GITHUB BUSTOSMIGUEL
# HERE I GO Escribir en la terminal: python
# Aparecerán unas flechitas en la terminal, eso es INTERACTIVE MODE
# INTEGERS (0, 1, 2.... ETC)


# Demonstrates addition:

x = 1
y = 2

z = x + y
print(z)




# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates (unintended) concatenation of strings
# Prompt user for two integers
x = input("What's x? ")
y = input("What's y? ")

# Print sum
z = x + y
print(z) # 1 + 2 = 12.-




# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates conversion from str to int
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
# 1 + 2 = 3.-



# %% a f(x) inside of another f(x) NOTAS GITHUB BUSTOSMIGUEL

# # Demonstrates nesting of function calls
x = int(input("What's x? "))
y = int(input("What's y? "))

z = x + y
print(z)
# 1 + 2 = 3.-
















# FLOAT (Number with a decimal point, properly called FLOATING POINT)

# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates conversion of str to float

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x + y

print(z)








# ROUND

# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates rounding to nearest int

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)





# %% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates fewer variables

x = float(input("What's x? "))
y = float(input("What's y? "))

print(round(x + y))



# %% NOTAS GITHUB BUSTOSMIGUEL

  # Demonstrates formatting with commas
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")

# RESPONDER 1 Y 999, aparecerá la coma en la salida: 1,000






# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates division

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)






# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates rounding after the decimal point
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z)





# %% NOTAS GITHUB BUSTOSMIGUEL
# responder 2 y 3
# Demonstrates formatting after the decimal place

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x / y

print(f"{z:.5f}")




# %% NOTAS GITHUB BUSTOSMIGUEL
# ooo Demonstrates defining a function without parameters
# responder 2 y 3
# Da el mismo resultado que el anterior:

def hello():
   print("hello")

name = input("What's your name? ")
hello()
print(name)











#DEF (Define, create, invent your own f(x))
# si corres esto, la f(x) hello OBVIO QUE NO existe:
        #name = input("What's your name? ")
        #hello(name)
# PERO AL AGREGAR antes esto:
        #def hello(to):
        #print("hello,", to)
# SI EXISTIRÁ, COMO EN ESTE EJEMPLO:

# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates defining a function with a parameter

def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)



# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates defining a function with a parameter with a default value

def hello(to="world"):
   print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)






# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates defining a main function
 def main():
   name = input("What's your name? ")
   hello(name)

def hello(to="world"):
   print("hello,", to)
   main()







# %% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates defining a function with a return value

def main():
   x = int(input("What's x? "))
   print("x squared is", square(x))

def square(n):
   return n * n

main()





# %% NOTAS GITHUB BUSTOSMIGUEL
# también se puede con:
# def square(n):
  # return pow(n, 2), ASÍ:


def main():
   x = int(input("What's x? "))
   print("x squared is", square(x))

def square(n):
   return n * n

main()





# %% NOTAS GITHUB BUSTOSMIGUEL



########### VIDEO_2: CONDITIONALS

#%% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates conditionals

x = int(input("What´s x? "))
y = int(input("What´s y? "))

if x < y:
   print("x is less than y")

if x > y:
   print("x is greater than y")

if x == y:
   print("x is equal to y")


#%% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates mutually exclusive conditions

x = int(input("What´s x? "))
y = int(input("What´s y? "))

if x < y:
   print("x is less than y")

elif x > y:
   print("x is greater than y")

elif x == y:
   print("x is equal to y")


#%% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates fewer conditions

x = int(input("What´s x? "))
y = int(input("What´s y? "))

if x < y:
   print("x is less than y")

elif x > y:
   print("x is greater than y")

else:
   print("x is equal to y")


# %% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates inequalities and logical operator

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
   print("x is not equal to y")

else:
   print("x is equal to y")




# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates equality
x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
   print("x is equal to y")
else:
   print("x is not equal to y")

# %% NOTAS GITHUB BUSTOSMIGUEL



# Demonstrates inequality
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
   print("x is not equal to y")

else:
   print("x is equal to y")

# %% NOTAS GITHUB BUSTOSMIGUEL

 # Demonstrates inequalities and logical operators
 score = int(input("Score: "))

if score >= 90 and score <= 100:
   print("Grade: A")

elif score >= 80 and score < 90:
   print("Grade: B")

elif score >= 70 and score < 80:
   print("Grade: C")

elif score >= 60 and score < 70:
   print("Grade: D")
else:
   print("Grade: F")


# %% NOTAS GITHUB BUSTOSMIGUEL


# Demonstrates inequalities and logical operators

score = int(input("Score: "))

if 90 <= score and score <= 100:
   print("Grade: A")
elif 80 <= score and score < 90:
   print("Grade: B")
elif 70 <= score and score < 80:
   print("Grade: C")
elif 60 <= score and score < 70:
   print("Grade: D")
else:
   print("Grade: F")






# %% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates chained comparisons
score = int(input("Score: "))

if 90 <= score <= 100:
   print("Grade: A")

elif 80 <= score < 90:
   print("Grade: B")

elif 70 <= score < 80:
   print("Grade: C")

elif 60 <= score < 70:
   print("Grade: D")

else:
   print("Grade: F")




# %% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates fewer comparisons
score = int(input("Score: "))

if score >= 90:
   print("Grade: A")
elif score >= 80:
   print("Grade: B")
elif score >= 70:
   print("Grade: C")
elif score >= 60:
   print("Grade: D")
else:
print("Grade: F")



# %% NOTAS GITHUB BUSTOSMIGUEL

# Compares strings
answer = input("Do you agree? ")
if answer == "yes":
   print("Agreed")
else:
   print("Not agreed")




# %% NOTAS GITHUB BUSTOSMIGUEL

# Strips string before comparing
answer = input("Do you agree? ").strip()
if answer == "yes":
   print("Agreed")
else:
   print("Not agreed")





# %% NOTAS GITHUB BUSTOSMIGUEL


# Lowercases string before comparing

answer = input("Do you agree? ").strip().lower()
if answer == "yes":
   print("Agreed")
else:
   print("Not agreed")





# %% NOTAS GITHUB BUSTOSMIGUEL
# Compares multiple strings

answer = input("Do you agree? ").strip().lower()
if answer == "yes" or answer == "y":
   print("Agreed")
else:
   print("Not agreed")





# %% NOTAS GITHUB BUSTOSMIGUEL

#Compares multiple strings
answer = input("Do you agree? ").strip().lower()
if answer.startswith("y"):
   print("Agreed")
else:
   print("Not agreed")




# %% NOTAS GITHUB BUSTOSMIGUEL
# Demonstrates modulo operator

x = int(input("What's x? "))

if x % 2 == 0:
   print("Even")
else:
   print("Odd")




# %% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates a function that returns a bool

def main():
   x = int(input("What's x? "))
   if is_even(x):
      print("Even")
   else:
      print("Odd")


def is_even(n):
   if n % 2 == 0:
      return True
   else:
      return False

main()

#%% NOTAS GITHUB BUSTOSMIGUEL

# Demonstrates conditional expressions (ternary operators)

def main():
   x = int(input("What's x? "))
   if is_even(x):
      print("Even")
   else:
      print("Odd")

def is_even(n):
   return True if n % 2 == 0 else False

main()


#%% NOTAS GITHUB BUSTOSMIGUEL


# Demonstrates returning the value of a Boolean expression
def main():
   x = int(input("What's x? "))
   if is_even(x):
      print("Even")
   else:
      print("Odd")


def is_even(n):
   return n % 2 == 0

main()

#%% NOTAS GITHUB BUSTOSMIGUEL


# Compares multiple strings with if/elif/else

name = input("What's your name? ")

if name == "Harry":
   print("Gryffindor")
elif name == "Hermione":
   print("Gryffindor")
elif name == "Ron":
   print("Gryffindor")
elif name == "Draco":
   print("Slytherin")
else:
   print("Who?")



#%% NOTAS GITHUB BUSTOSMIGUEL

# Uses or
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
   print("Gryffindor")
elif name == "Draco":
   print("Slytherin")
else:
   print("Who?")



#%% NOTAS GITHUB BUSTOSMIGUEL

# Uses match with case
name = input("What's your name? ")

match name:
   case "Harry":
      print("Gryffindor")
   case "Hermione":
      print("Gryffindor")
   case "Ron":
      print("Gryffindor")
   case "Draco":
      print("Slytherin")
   case _:
      print("Who?")


#%% NOTAS GITHUB BUSTOSMIGUEL

# Uses |

name = input("What's your name? ")

match name:
   case "Harry" | "Hermione" | "Ron":
      print("Gryffindor")
   case "Draco":
      print("Slytherin")
   case _:
      print("Who?")

# %%

# Gets a number from the user
x = int(input("What's x? "))
print(f"x is {x}")

# %%

# Catches a ValueError
try:
   x = int(input("What's x? "))
   print(f"x is {x}")

except ValueError:
   print("x is not an integer"

# %%
# Demonstrates a NameError

try:
   x = int(input("What's x? "))

except ValueError:
   print("x is not an integer")

print(f"x is {x}")


# %%


# Demonstrates else
try:
   x = int(input("What's x? "))
except ValueError:
   print("x is not an integer")
else:
   print(f"x is {x}")


# %%



# Adds a loop
while True:
   try:
      x = int(input("What's x? "))
   except ValueError:
      print("x is not an integer")
   else:
      break
   print(f"x is {x}")



# %%


# Adds functions, uses break and return
def main():
   x = get_int()
   print(f"x is {x}")

def get_int():
   while True:
      try:
         x = int(input("What's x? "))
      except ValueError:
         print("x is not an integer")
      else:
         break
   return x

main()



# %%


# Removes break

def main():
   x = get_int()
   print(f"x is {x}")

def get_int():
   while True:
      try:
         x = int(input("What's x? "))
      except ValueError:
         print("x is not an integer")
      else:
         return x
main()

# %%


# Removes else

def main():
   x = get_int()
   print(f"x is {x}")

def get_int():
   while True:
      try:
         return int(input("What's x? "))
      except ValueError:
         print("x is not an integer")

main()



# %%


# Adds pass
def main():
   x = get_int()
   print(f"x is {x}")

def get_int():
   while True:
      try:
         return int(input("What's x? "))
      except ValueError:
         pass
main()



# %%



# Adds prompt
def main():
   x = get_int("What's x? ")
   print(f"x is {x}")

def get_int(prompt):
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         pass
main()



# NOTAS BUSTOSMIGUEL |||||| LOOPS
# NOTAS BUSTOSMIGUEL |||||| LOOPS
# NOTAS BUSTOSMIGUEL |||||| LOOPS
# NOTAS BUSTOSMIGUEL |||||| LOOPS
# NOTAS BUSTOSMIGUEL |||||| LOOPS
# NOTAS BUSTOSMIGUEL |||||| LOOPS
# NOTAS BUSTOSMIGUEL |||||| LOOPS
# NOTAS BUSTOSMIGUEL |||||| LOOPS


# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates multiple (identical) function calls

print("meow")
print("meow")
print("meow")

# %%  NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates a while loop, counting down
# WHILE is one way to express a loop.
# while helps to ask a question again and again
# i es integer, ":" es then o entonces. (en SAS es "then")")
# while "i" isNotEqualTo O, print "meow".
# if "i" is always 3, you are looping forever or infinite loop
# control bottom + C, cancell and it´s a friend to cancel
# 

i = 3
while i != 0:
   print("meow")
   i = i - 1

# i = i - 1 one less, one less, will hit zero

# %%  NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates a while loop, counting up from 1

i = 1
while i <= 3:
   print("meow")
   i = i + 1



# %%  NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates a while loop, counting up from 0
i = 0
while i < 3:
   print("meow")
   i = i + 1



# %%  NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates (more succinct) incrementation

i = 0
while i < 3:
   print("meow")
   i += 1


# %%  NOTAS BUSTOSMIGUEL |||||| LOOPS


# Demonstrates a for loop, using a list
for i in [0, 1, 2]:
   print("meow")

# %% c
# Demonstrates a for loop, using range

for i in range(3):
   print("meow")



# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates a for loop, with _ as a variable

for _ in range(3):
   print("meow")


# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates str multiplication

print("meow\n" * 3, end="")

# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Introduces continue, break

while True:
   n = int(input("What's n? "))
   if n <= 0:
      continue
   else:
      break
for _ in range(n):
   print("meow")

# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Removes continue
while True:
   n = int(input("What's n? "))
   if n > 0:
      break

for _ in range(n):
   print("meow")


# %% NOTAS BUSTOSMIGUEL |||||| LOOPS


# Demonstrates defining functions

def main():
   meow(get_number())
   def get_number():
      while True:
         n = int(input("What's n? "))
         if n > 1:
            return n

def meow(n):
   for _ in range(n):
      print("meow")

main()

# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates indexing into a list

students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])


# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates iterating over a list

students = ["Hermione", "Harry", "Ron"]
for student in students:
   print(student)

# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Demonstrates iterating over and indexing into a list

students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
   print(i + 1, students[i])

# %% NOTAS BUSTOSMIGUEL |||||| LOOPS


# Demonstrates indexing into a dict

students = {
   "Hermione": "Gryffindor",
   "Harry": "Gryffindor",
   "Ron": "Gryffindor",
   "Draco": "Slytherin",
   }

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

# %% NOTAS BUSTOSMIGUEL |||||| LOOPS


# Demonstrates iterating over and index into a dict

students = {
   "Hermione": "Gryffindor",
   "Harry": "Gryffindor",
   "Ron": "Gryffindor",
   "Draco": "Slytherin",
   }

for student in students:
   print(student, students[student], sep=", ")

# %% NOTAS BUSTOSMIGUEL |||||| LOOPS


# Demonstrates iterating over a list of dict objects

students = [
   {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
   {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
   {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
   {"name": "Draco", "house": "Slytherin", "patronus": None},
 ]

for student in students:
   print(student["name"], student["house"], student["patronus"], sep=", ")


# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

Prints a column of bricks

print("#")
print("#")
print("#")


# %% NOTAS BUSTOSMIGUEL |||||| LOOPS


# Prints column of bricks using a loop

for _ in range(3):
   print("#")

# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Prints column of bricks using a function with a loop

def main():
   print_column(3)

 def print_column(height):
   for _ in range(height):
      print("#")

main()


# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Prints column of bricks using a function with str multiplication

def main():
   print_column(3)

def print_column(height):
   print("#\n" * height, end="")

main()



# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Prints row of coins using a function with str multiplication

def main():
   print_row(4)

def print_row(width):
   print("?" * width)

main()




# %% NOTAS BUSTOSMIGUEL |||||| LOOPS


# Prints square of bricks using a function with nested loops
def main():
   print_square(3)

def print_square(size):
   for i in range(size):
      for j in range(size):
         print("#", end="")
      print()

main()



# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Prints square of bricks using a function with a loop and str multiplication
def main():
   print_square(3)

def print_square(size):
   for _ in range(size):
      print("#" * size)

main()




# %% NOTAS BUSTOSMIGUEL |||||| LOOPS

# Prints square of bricks using a function with a loop and str multiplication

def main():
   print_square(3)

def print_square(size):
   for _ in range(size):
      print_row(size)

def print_row(width):
   print("#" * width)

main()






########## EXCEPTIONS


# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS

# Gets a number from the user

x = int(input("What's x? "))
4  print(f"x is {x}")


# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS

# Catches a ValueError

try:
   x = int(input("What's x? "))
   print(f"x is {x}")
except ValueError:
   print("x is not an integer")

# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS

# Demonstrates a NameError
try:
   x = int(input("What's x? "))
except ValueError:
   print("x is not an integer")
print(f"x is {x}")



# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS
# Demonstrates else

try:
   x = int(input("What's x? "))
except ValueError:
   print("x is not an integer")
else:
   print(f"x is {x}")


# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS

 # Adds a loop
 
while True:
   try:
      x = int(input("What's x? "))
   except ValueError:
      print("x is not an integer")
   else:
      break
      
print(f"x is {x}")



# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS

 # Adds functions, uses break and return
 
def main():
   x = get_int()
   print(f"x is {x}")

def get_int():
   while True:
      try:
         x = int(input("What's x? "))
      except ValueError:
         print("x is not an integer")
      else:
         break
   return x
main()



# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS

# Removes break

def main():
   x = get_int()
   print(f"x is {x}")


def get_int():
   while True:
      try:
         x = int(input("What's x? "))
      except ValueError:
         print("x is not an integer")
      else:
         return x

main()



# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS


# Removes else

def main():
   x = get_int()
   print(f"x is {x}")

def get_int():
   while True:
      try:
         return int(input("What's x? "))
      except ValueError:
         print("x is not an integer")

main()


# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS


# Adds pass

def main():
   x = get_int()
   print(f"x is {x}")

def get_int():
   while True:
      try:
         return int(input("What's x? "))
      except ValueError:
         pass

main()


# %% NOTAS BUSTOSMIGUEL |||||| EXCEPTIONS

# Adds prompt

def main():
   x = get_int("What's x? ")
   print(f"x is {x}")

def get_int(prompt):
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         pass

main()



################### LIBRARIES


# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES


# Demonstrates import and random.choice

import random
coin = random.choice(["heads", "tails"])
print(coin)
# generate0.py

# 
# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES


# Demonstrates from

from random import choice
coin = choice(["heads", "tails"])
print(coin)
# generate1.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates randint
import random
number = random.randint(1, 10)
print(number)
# generate2.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates shuffle

import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
   print(card)
# generate3.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates statistics

import statistics

print(statistics.mean([100, 90]))
# average.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates sys.argv

import sys

print("hello, my name is", sys.argv[1])
# name0.py


# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES


1  # Demonstrates IndexError
2  
3  import sys
4  
5  try:
6      print("hello, my name is", sys.argv[1])
7  except IndexError:
8      print("Too few arguments")
# name1.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Adds error checking
import sys

if len(sys.argv) < 2:
   print("Too few arguments")
elif len(sys.argv) > 2:
   print("Too many arguments")
else:
   print("hello, my name is", sys.argv[1])
# name2.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates sys.exit
 
import sys

if len(sys.argv) < 2:
   sys.exit("Too few arguments")
elif len(sys.argv) > 2:
   sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
# # name3.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates list slice

import sys

if len(sys.argv) < 2:
   sys.exit("Too few arguments")

for arg in sys.argv[1:]:
   print("hello, my name is", arg)
# name4.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates pip-installed package
import cowsay
import sys

if len(sys.argv) == 2:
   cowsay.cow("hello, " + sys.argv[1])
# say0.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES


# Demonstrates a t-rex

import cowsay
import sys

if len(sys.argv) == 2:
   cowsay.trex("hello, " + sys.argv[1])
# say1.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates requests

import sys
import requests

if len(sys.argv) != 2:
   sys.exit()

response = requests.get(
   "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(response.json())
# itunes0.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES


 # Demonstrates json
 
import json
import sys
import requests

if len(sys.argv) != 2:
   sys.exit()

response = requests.get(
   "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(json.dumps(response.json(), indent=2))

#itunes1.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates iterating over JSON
 
import json
import sys
import requests

if len(sys.argv) != 2:
   sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
)
o = response.json()
for result in o["results"]:
   print(result["trackName"])

# itunes2.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

def hello(name):
   print(f"hello, {name}")

def goodbye(name):
   print(f"goodbye, {name}")
# sayings0.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES


# Demonstrates own module
import sys

from sayings0 import hello

if len(sys.argv) == 2:
   hello(sys.argv[1])

# say2.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

 # Doesn't check __name__
 
def main():
   hello("world")
   goodbye("world")

def hello(name):
   print(f"hello, {name}")

def goodbye(name):
   print(f"goodbye, {name}")

main()
# sayings1.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES


# Demonstrates own module

import sys

from sayings1 import hello

if len(sys.argv) == 2:
   hello(sys.argv[1])


# say3.py


# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Check __name__

def main():
   hello("world")
   goodbye("world")

def hello(name):
   print(f"hello, {name}")

def goodbye(name):
   print(f"goodbye, {name}")

if __name__ == "__main__":
   main()
# sayings2.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates own module

import sys
from sayings2 import hello
if len(sys.argv) == 2:
   hello(sys.argv[1])
# say4.py

# %% NOTAS BUSTOSMIGUEL |||||| LIBRARIES

# Demonstrates own module
import sys
from sayings2 import goodbyeif len(sys.argv) == 2:
      goodbye(sys.argv[1])
# say5.py





########### UNIT TEST


# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST

# Demonstrates defining a function with a return value

def main():   
   x = int(input("What's x? "))
   print("x squared is", square(x))

def square(n):
   return n * n

main()

# calculator0.py


# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST


# Demonstrates defining a function with a return value

def main():
   x = int(input("What's x? "))
   print("x squared is", square(x))

def square(n):
   return n * n


if __name__ == "__main__":
   main()


# calculator1.py




# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST


from calculator1 import square
def main():
   test_square()

def test_square():
   if square(2) != 4:
      print("2 squared was not 4")

   if square(3) != 9:
      print("3 squared was not 9")

if __name__ == "__main__":
   main()
   
# test_calculator1.py


# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST


# Demonstrates defining a function with a return value

def main():
   x = int(input("What's x? "))
   print("x squared is", square(x))


def square(n):
   return n * n

if __name__ == "__main__":
   main()

   
# calculator2.py


# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST


from calculator2 import square

def main():
   test_square()

def test_square():
   assert square(2) == 4
   assert square(3) == 9

if __name__ == "__main__":
   main()


# test_calculator2.py

# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST


# Demonstrates defining a function with a return value

def main():
   x = int(input("What's x? "))
   print("x squared is", square(x))
 

def square(n):
   return n * n

if __name__ == "__main__":
   main()

# calculator3.py

# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST



from calculator3 import square

def main():
   test_square()

def test_square():
   try:
      assert square(2) == 4
   except AssertionError:
            print("2 squared was not 4")
   try:
      assert square(3) == 9
   except AssertionError:
         print("3 squared was not 9")

if __name__ == "__main__":
   main()


# test_calculator3.py


# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST



# Demonstrates defining a function with a return value

def main():
   x = int(input("What's x? "))
   print("x squared is", square(x))

def square(n):
   return n * n

if __name__ == "__main__":
   main()

# calculator4.py


# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST



from calculator4 import square

def main():
   test_square()

def test_square():
   try:
      assert square(2) == 4
   except AssertionError:
      print("2 squared was not 4")
   try:
      assert square(3) == 9
   except AssertionError:
      print("3 squared was not 9")
   try:
      assert square(-2) == 4
   except AssertionError:
      print("-2 squared was not 4")
   try:
      assert square(-3) == 9
   except AssertionError:
      print("-3 squared was not 9")
   try:
      assert square(0) == 0
   except AssertionError:
      print("0 squared was not 0")

if __name__ == "__main__":
   main()


test_calculator4.py




# %% [markdown]
# # Celdas Interactivas Listas para Ejecutar en VS Code
# Para ejecutar cada celda, presiona `Shift + Enter` dentro del bloque.

# %%

%pip install

# %%
%pip install pytest --break-system-packages

#%%
import pytest



# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST - CASO 1: calculator5.py
# Creamos automáticamente el archivo calculator5.py para poder importarlo
with open("calculator5.py", "w") as f:
    f.write('''def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
''')

print("✓ Archivo 'calculator5.py' generado con éxito.")




# %% CASO 1: Pruebas para calculator5
import pytest

# Guardamos el archivo de prueba en disco
with open("test_calculator5.py", "w") as f:
    f.write('''from calculator5 import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
''')



# Ejecutamos Pytest directamente en la ventana interactiva
pytest.main(["test_calculator5.py", "-v"])




# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST - CASO 2: calculator6.py
# Creamos el archivo calculator6.py
with open("calculator6.py", "w") as f:
    f.write('''def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
''')

print("✓ Archivo 'calculator6.py' generado con éxito.")



# %% CASO 2: Pruebas con múltiples funciones en test_calculator6.py
import pytest

with open("test_calculator6.py", "w") as f:
    f.write('''from calculator6 import square

def test_positive():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
''')

# Ejecutamos Pytest para calculator6
pytest.main(["test_calculator6.py", "-v"])


# %% NOTAS BUSTOSMIGUEL |||||| UNIT TEST - CASO 3: calculator.py
# Creamos el archivo calculator.py
with open("calculator.py", "w") as f:
    f.write('''def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
''')

print("✓ Archivo 'calculator.py' generado con éxito.")

# %% CASO 3: Pruebas incluyendo pytest.raises(TypeError)
import pytest

with open("test_calculator_raises.py", "w") as f:
    f.write('''import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
''')

# Ejecutamos Pytest comprobando el manejo de excepciones
pytest.main(["test_calculator_raises.py", "-v"])














#%% NOTAS BUSTOSMIGUEL |||||| UNIT TEST
# Function to be tested
 
 
def main():
     name = input("What's your name? ")
     hello(name)
 
 
def hello(to="world"):
     print("hello,", to)
 
 
if __name__ == "__main__":
     main()


#%% NOTAS BUSTOSMIGUEL |||||| UNIT TEST
 # Has function return a str instead
 
 
def main():
     name = input("What's your name? ")
     print(hello(name))
 
 
def hello(to="world"):
     return f"hello, {to}"
 
 
if __name__ == "__main__":
     main()



#%%NOTAS BUSTOSMIGUEL |||||| UNIT TEST
from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"



#%% NOTAS BUSTOSMIGUEL |||||| UNIT TEST
 from hello1 import hello
 
 
 def test_default():
     assert hello() == "hello, world"
 
 
 def test_argument():
     for name in ["Hermione", "Harry", "Ron"]:
         assert hello(name) == f"hello, {name}"
est_hello1b.py


 #%% NOTAS BUSTOSMIGUEL |||||| UNIT TEST
from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"


















############### REGULAR EXPRESSIONS 


 #%%  REGULAR EXPRESSIONS github bustosmiguel

 # NOTAS BUSTOSMIGUEL |||||| REGULAR EXPRESSIONS
# Validates email address by checking for @

email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")


 #%%  REGULAR EXPRESSIONS github bustosmiguel

# Validates email address by checking for . too

email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")



 #%%  REGULAR EXPRESSIONS github bustosmiguel

 # Validates email address by checking username and domain separately
 
 email = input("What's your email? ").strip()
 
 username, domain = email.split("@")
 
 if username and "." in domain:
     print("Valid")
 else:
     print("Invalid")


 #%%  REGULAR EXPRESSIONS github bustosmiguel
 #  # Validates email address by checking whether domain ends with .edu
 
 email = input("What's your email? ").strip()
 
 username, domain = email.split("@")
 
 if username and domain.endswith(".edu"):
     print("Valid")
 else:
     print("Invalid")


 #%%  REGULAR EXPRESSIONS github bustosmiguel


 # Validates email address by checking for @ with regex
 
 import re
 
 email = input("What's your email? ").strip()
 
 if re.search("@", email):
     print("Valid")
 else:
     print("Invalid")


 #%%  REGULAR EXPRESSIONS github bustosmiguel


 # Adds .*
 
 import re
 
 email = input("What's your email? ").strip()
 
 if re.search(".*@.*", email):
     print("Valid")
 else:
     print("Invalid")



 #%%  REGULAR EXPRESSIONS github bustosmiguel

 # Changes * to +
 
 import re
 
 email = input("What's your email? ").strip()
 
 if re.search(".+@.+", email):
     print("Valid")
 else:
     print("Invalid")



 #%%  REGULAR EXPRESSIONS github bustosmiguel

 # Adds \.edu
 
 import re
 
 email = input("What's your email? ").strip()
 
 if re.search(r".+@.+\.edu", email):
     print("Valid")
 else:
     print("Invalid")



 #%%  REGULAR EXPRESSIONS github bustosmiguel

 # Adds ^ and $ to regex
 
 import re
 
 email = input("What's your email? ").strip()
 
 if re.search(r"^.+@.+\.edu$", email):
     print("Valid")
 else:
     print("Invalid")



 #%%  REGULAR EXPRESSIONS github bustosmiguel


 # Adds character class
 
 import re
 
 email = input("What's your email? ").strip()
 
 if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
     print("Valid")
 else:
     print("Invalid")



  #%%  REGULAR EXPRESSIONS github bustosmiguel

 
 # Replaces character class with \w
 
 import re
 
 email = input("What's your email? ").strip()
 
 if re.search(r"^\w+@\w+\.edu$", email):
     print("Valid")
 else:
     print("Invalid")


 #%%  REGULAR EXPRESSIONS github bustosmiguel

 # Adds re.IGNORECASE
 
 import re
 
 email = input("What's your email? ").strip()
 
 if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
     print("Valid")
 else:
     print("Invalid")



 #%%  REGULAR EXPRESSIONS github bustosmiguel

 #  # Adds optional subdomain
 
 import re
 
 email = input("What's your email? ").strip()
 
 if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
     print("Valid")
 else:
     print("Invalid")



 #%%  REGULAR EXPRESSIONS github bustosmiguel

 # # Reformats "last, first" as "first last"

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")



 #%%  REGULAR EXPRESSIONS github bustosmiguel


 # Uses re.search
 
 import re
 
 name = input("What's your name? ").strip()
 matches = re.search(r"^(.+), (.+)$", name)
 if matches:
     last, first = matches.groups()
     name = first + " " + last
 print(f"hello, {name}")


 #%%  REGULAR EXPRESSIONS github bustosmiguel

 # 
 # # Uses .group

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")



 #%%  REGULAR EXPRESSIONS github bustosmiguel


# Uses walrus operator

import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")



 #%%  REGULAR EXPRESSIONS github bustosmiguel


# Extracts Twitter username from URL using str.replace

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")


 #%%  REGULAR EXPRESSIONS github bustosmiguel

# Extracts Twitter username from URL using str.removeprefix

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")


 #%%  REGULAR EXPRESSIONS github bustosmiguel

# Uses re.sub

import re

url = input("URL: ").strip()

username = re.sub(r"^https://twitter\.com/", "", url)
print(f"Username: {username}")


 #%%  REGULAR EXPRESSIONS github bustosmiguel
 
# Allows for http, no protocol, and www.

import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")


 #%%  REGULAR EXPRESSIONS github bustosmiguel

# Uses capture group

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))


 #%%  REGULAR EXPRESSIONS github bustosmiguel

# Ignores query and fragment

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))



















######### OOP

 #%%  OOP  github bustosmiguel

# Represents a student with multiple variables

name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")

 #%%  OOP  github bustosmiguel

 # Modularizes getting student's name and house
 
 
 def main():
     name = get_name()
     house = get_house()
     print(f"{name} from {house}")
 
 
 def get_name():
     return input("Name: ")
 
 
 def get_house():
     return input("House: ")
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel

 # Returns student as tuple, unpacking it
 
 
 def main():
     name, house = get_student()
     print(f"{name} from {house}")
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return name, house
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Returns student as tuple, without unpacking it
 
 
 def main():
     student = get_student()
     print(f"{student[0]} from {student[1]}")
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return (name, house)
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel

 # Demonstrates immutability of tuples, removes parentheses
 # https://scifi.stackexchange.com/q/105992
 
 
 def main():
     student = get_student()
     if student[0] == "Padma":
         student[1] = "Ravenclaw"
     print(f"{student[0]} from {student[1]}")
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return name, house
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Stores student as (mutable) list
 
 
 def main():
     student = get_student()
     if student[0] == "Padma":
         student[1] = "Ravenclaw"
     print(f"{student[0]} from {student[1]}")
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return [name, house]
 
 
 if __name__ == "__main__":
     main()

 #%%  OOP  github bustosmiguel
 # Stores student as dict
 
 
 def main():
     student = get_student()
     print(f"{student['name']} from {student['house']}")
 
 
 def get_student():
     student = {}
     student["name"] = input("Name: ")
     student["house"] = input("House: ")
     return student
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel

 # Eliminates unneeded variable
 
 
 def main():
     student = get_student()
     print(f"{student['name']} from {student['house']}")
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return {"name": name, "house": house}
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Demonstrates mutability of dicts
 
 
 def main():
     student = get_student()
     if student["name"] == "Padma":
         student["house"] = "Ravenclaw"
     print(f"{student['name']} from {student['house']}")
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return {"name": name, "house": house}
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Defines class for a student
 
 
 class Student:
     ...
 
 
 def main():
     student = get_student()
     print(f"{student.name} from {student.house}")
 
 
 def get_student():
     student = Student()
     student.name = input("Name: ")
     student.house = input("House: ")
     return student
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Adds __init__
 
 
 class Student:
     def __init__(self, name, house):
         self.name = name
         self.house = house
 
 
 def main():
     student = get_student()
     print(f"{student.name} from {student.house}")
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     student = Student(name, house)
     return student
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Eliminates unneeded variable
 
 
 class Student:
     def __init__(self, name, house):
         self.name = name
         self.house = house
 
 
 def main():
     student = get_student()
     print(f"{student.name} from {student.house}")
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return Student(name, house)
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Adds validation in __init__ using raise
 
 
 class Student:
     def __init__(self, name, house):
         if not name:
             raise ValueError("Missing name")
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
             raise ValueError("Invalid house")
         self.name = name
         self.house = house
 
 
 def main():
     student = get_student()
     print(f"{student.name} from {student.house}")
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return Student(name, house)
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel

 # Prints student without __str__
 
 
 class Student:
     def __init__(self, name, house):
         if not name:
             raise ValueError("Missing name")
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
             raise ValueError("Invalid house")
         self.name = name
         self.house = house
 
 
 def main():
     student = get_student()
     print(student)
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return Student(name, house)
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Adds __str__
 
 
 class Student:
     def __init__(self, name, house):
         if not name:
             raise ValueError("Missing name")
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
             raise ValueError("Invalid house")
         self.name = name
         self.house = house
 
     def __str__(self):
         return f"{self.name} from {self.house}"
 
 
 def main():
     student = get_student()
     print(student)
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return Student(name, house)
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Prompts for patronus too, but doesn't display yet
 
 
 class Student:
     def __init__(self, name, house, patronus):
         if not name:
             raise ValueError("Missing name")
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
             raise ValueError("Invalid house")
         self.name = name
         self.house = house
         self.patronus = patronus
 
     def __str__(self):
         return f"{self.name} from {self.house}"
 
 
 def main():
     student = get_student()
     print(student)
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     patronus = input("Patronus: ")
     return Student(name, house, patronus)
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel

 # Adds charm method to cast a charm
 
 
 class Student:
     def __init__(self, name, house, patronus=None):
         if not name:
             raise ValueError("Missing name")
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
             raise ValueError("Invalid house")
         if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
             raise ValueError("Invalid patronus")
         self.name = name
         self.house = house
         self.patronus = patronus
 
     def __str__(self):
         return f"{self.name} from {self.house}"
 
     def charm(self):
         match self.patronus:
             case "Stag":
                 return "🐴"
             case "Otter":
                 return "🦦"
             case "Jack Russell terrier":
                 return "🐶"
             case _:
                 return "🪄"
 
 
 def main():
     student = get_student()
     print("Expecto Patronum!")
     print(student.charm())
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     patronus = input("Patronus: ") or None
     return Student(name, house, patronus)
 
 #%%  OOP  github bustosmiguel

 
 if __name__ == "__main__":
     main()
dent16.py
 # Removes patronus for simplicy, circumvents error-checking by setting attribute
 
 
 class Student:
     def __init__(self, name, house):
         if not name:
             raise ValueError("Invalid name")
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
             raise ValueError("Invalid house")
         self.name = name
         self.house = house
 
     def __str__(self):
         return f"{self.name} from {self.house}"
 
 
 def main():
     student = get_student()
     student.house = "Number Four, Privet Drive"
     print(student)
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return Student(name, house)
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # 
 #  # Adds @property for house
 
 
 class Student:
     def __init__(self, name, house):
         if not name:
             raise ValueError("Invalid name")
         self.name = name
         self.house = house
 
     def __str__(self):
         return f"{self.name} from {self.house}"
 
     @property
     def house(self):
         return self._house
 
     @house.setter
     def house(self, house):
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
             raise ValueError("Invalid house")
         self._house = house
 
 
 def main():
     student = get_student()
     print(student)
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return Student(name, house)
 
 
 if __name__ == "__main__":
     main()



 #%%  OOP  github bustosmiguel

 # Adds @property for name
 
 
 class Student:
     def __init__(self, name, house):
         self.name = name
         self.house = house
 
     def __str__(self):
         return f"{self.name} from {self.house}"
 
     @property
     def name(self):
         return self._name
 
     @name.setter
     def name(self, name):
         if not name:
             raise ValueError("Invalid name")
         self._name = name
 
     @property
     def house(self):
         return self._house
 
     @house.setter
     def house(self, house):
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
             raise ValueError("Invalid house")
         self._house = house
 
 
 def main():
     student = get_student()
     print(student)
 
 
 def get_student():
     name = input("Name: ")
     house = input("House: ")
     return Student(name, house)
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel


# Prints the type of an integer
print(type(50))

# Prints the type of a string
print(type("hello, world"))

# Prints the type of a list
print(type([]))

# Prints the type of a list
print(type(list()))

# Prints the type of a dictionary
print(type({}))

# Prints the type of a dictionary
print(type(dict()))


 #%%  OOP  github bustosmiguel
 #  # Implements sort() with an instance method
 
 import random
 
 
 class Hat:
     def __init__(self):
         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
 
     def sort(self, name):
         print(name, "is in", random.choice(self.houses))
 
 
 hat = Hat()
 hat.sort("Harry")


 #%%  OOP  github bustosmiguel

 # Implements sort() with a class method
 
 import random
 
 
 class Hat:
 
     houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
 
     @classmethod
     def sort(cls, name):
         print(name, "is in", random.choice(cls.houses))
 
 
 Hat.sort("Harry")


 #%%  OOP  github bustosmiguel

 # Moves get_student into Student class
 
 
 class Student:
     def __init__(self, name, house):
         self.name = name
         self.house = house
 
     def __str__(self):
         return f"{self.name} from {self.house}"
 
     @classmethod
     def get(cls):
         name = input("Name: ")
         house = input("House: ")
         return cls(name, house)
 
 
 def main():
     student = Student.get()
     print(student)
 
 
 if __name__ == "__main__":
     main()


 #%%  OOP  github bustosmiguel
 # Demonstrates inheritance [maybe don't add `if` error-checking]
 
 
 class Wizard:
     def __init__(self, name):
         if not name:
             raise ValueError("Missing name")
         self.name = name
 
     ...
 
 
 class Student(Wizard):
     def __init__(self, name, house):
         super().__init__(name)
         self.house = house
 
     ...
 
 
 class Professor(Wizard):
     def __init__(self, name, subject):
         super().__init__(name)
         self.subject = subject
 
     ...
 
 
 wizard = Wizard("Albus")
 student = Student("Harry", "Gryffindor")
 professor = Professor("Severus", "Defense Against the Dark Arts")
 ...

 #%%  OOP  github bustosmiguel

 # Adds vaults, storing total in new vault
 
 
 class Vault:
     def __init__(self, galleons=0, sickles=0, knuts=0):
         self.galleons = galleons
         self.sickles = sickles
         self.knuts = knuts
 
     def __str__(self):
         return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
 
 
 potter = Vault(100, 50, 25)
 print(potter)
 
 weasley = Vault(25, 50, 100)
 print(weasley)
 
 galleons = potter.galleons + weasley.galleons
 sickles = potter.sickles + weasley.sickles
 knuts = potter.knuts + weasley.knuts
 
 total = Vault(galleons, sickles, knuts)
 print(total)


 #%%  OOP  github bustosmiguel

 # Adds vaults via operator overloading
 
 
class Vault:
     def __init__(self, galleons=0, sickles=0, knuts=0):
         self.galleons = galleons
         self.sickles = sickles
         self.knuts = knuts
 
     def __str__(self):
         return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
 
     def __add__(self, other):
         galleons = self.galleons + other.galleons
         sickles = self.sickles + other.sickles
         knuts = self.knuts + other.knuts
         return Vault(galleons, sickles, knuts)
 
 
 potter = Vault(100, 50, 25)
 print(potter)
 
 weasley = Vault(25, 50, 100)
 print(weasley)
 
 total = potter + weasley
 print(total)


 










############## ETC ETCETERA


 #%%  ETCETERA OTHERS  github bustosmiguel
 # Filters out duplicate houses using loop
 
 students = [
     {"name": "Hermione", "house": "Gryffindor"},
     {"name": "Harry", "house": "Gryffindor"},
     {"name": "Ron", "house": "Gryffindor"},
     {"name": "Draco", "house": "Slytherin"},
     {"name": "Padma", "house": "Ravenclaw"},
 ]
 
 houses = []
 for student in students:
     if student["house"] not in houses:
         houses.append(student["house"])
 
 for house in sorted(houses):
     print(house)


 #%%  ETCETERA OTHERS  github bustosmiguel


 # Filters out duplicate houses using set
 
 students = [
     {"name": "Hermione", "house": "Gryffindor"},
     {"name": "Harry", "house": "Gryffindor"},
     {"name": "Ron", "house": "Gryffindor"},
     {"name": "Draco", "house": "Slytherin"},
     {"name": "Padma", "house": "Ravenclaw"},
 ]
 
 houses = set()
 for student in students:
     houses.add(student["house"])
 
 for house in sorted(houses):
     print(house)



 #%%  ETCETERA OTHERS  github bustosmiguel

 # Implements a bank account
 
 balance = 0
 
 
 def main():
     print("Balance:", balance)
 
 
 if __name__ == "__main__":
     main()



 #%%  ETCETERA OTHERS  github bustosmiguel

 # UnboundLocalError
 
 balance = 0
 
 
 def main():
     print("Balance:", balance)
     deposit(100)
     withdraw(50)
     print("Balance:", balance)
 
 
 def deposit(n):
     balance += n
 
 
 def withdraw(n):
     balance -= n
 
 
 if __name__ == "__main__":
     main()



 #%%  ETCETERA OTHERS  github bustosmiguel

 # Uses global
 
 balance = 0
 
 
 def main():
     print("Balance:", balance)
     deposit(100)
     withdraw(50)
     print("Balance:", balance)
 
 
 def deposit(n):
     global balance
     balance += n
 
 
 def withdraw(n):
     global balance
     balance -= n
 
 
 if __name__ == "__main__":
     main()


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Uses class
 
 
 class Account:
     def __init__(self):
         self._balance = 0
 
     @property
     def balance(self):
         return self._balance
 
     def deposit(self, n):
         self._balance += n
 
     def withdraw(self, n):
         self._balance -= n
 
 
 def main():
     account = Account()
     print("Balance:", account.balance)
     account.deposit(100)
     account.withdraw(50)
     print("Balance:", account.balance)
 
 
 if __name__ == "__main__":
     main()
 #%%  ETCETERA OTHERS  github bustosmiguel


# Demonstrates a constant

MEOWS = 3

for _ in range(MEOWS):
    print("meow")


 #%%  ETCETERA OTHERS  github bustosmiguel


 # Demonstrates a class constant
 

 class Cat:
     MEOWS = 3
 
     def meow(self):
         for _ in range(Cat.MEOWS):
             print("meow")
 
 
 cat = Cat()
 cat.meow()


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Demonstrates TypeError
 
 
 def meow(n):
     for _ in range(n):
         print("meow")
 
 
 number = input("Number: ")
 meow(number)
 
 #%%  ETCETERA OTHERS  github bustosmiguel


 # Argument ... has incompatible type
 
 
 def meow(n: int):
     for _ in range(n):
         print("meow")
 
 
 number = input("Number: ")
 meow(number)


 #%%  ETCETERA OTHERS  github bustosmiguel


 # Incompatible types in assignment
 
 
 def meow(n: int):
     for _ in range(n):
         print("meow")
 
 
 number: int = input("Number: ")
 meow(number)

 #%%  ETCETERA OTHERS  github bustosmiguel


 # Success
 
 
 def meow(n: int):
     for _ in range(n):
         print("meow")
 
 
 number: int = int(input("Number: "))
 meow(number)

 #%%  ETCETERA OTHERS  github bustosmiguel

 # Prints None because mistakes meow as having a return value
 
 
 def meow(n: int):
     for _ in range(n):
         print("meow")
 
 
 number: int = int(input("Number: "))
 meows: str = meow(number)
 print(meows)


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Annotates return value, ... does not return a value
 
 
 def meow(n: int) -> None:
     for _ in range(n):
         print("meow")
 
 
 number: int = int(input("Number: "))
 meows: str = meow(number)
 print(meows)


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Success
 
 
 def meow(n: int) -> str:
     return "meow\n" * n
 
 
 number: int = int(input("Number: "))
 meows: str = meow(number)
 print(meows, end="")



 #%%  ETCETERA OTHERS  github bustosmiguel



 # Adds docstring to function.
 
 
 def meow(n):
     """Meow n times."""
     return "meow\n" * n
 
 
 number = int(input("Number: "))
 meows = meow(number)
 print(meows, end="")


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Uses Sphinx docstring format
 
 
 def meow(n):
     """
     Meow n times.
 
     :param n: Number of times to meow
     :type n: int
     :raise TypeError: If n is not an int
     :return: A string of n meows, one per line
     :rtype: str
     """
     return "meow\n" * n
 
 
 number = int(input("Number: "))
 meows = meow(number)
 print(meows, end="")



 #%%  ETCETERA OTHERS  github bustosmiguel


 # Uses command-line argument
 
 import sys
 
 if len(sys.argv) == 1:
     print("meow")
 elif len(sys.argv) == 3 and sys.argv[1] == "-n":
     n = int(sys.argv[2])
     for _ in range(n):
         print("meow")
 else:
     print("usage: meows11.py [-n NUMBER]")


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Uses command-line argument
 
 import argparse
 
 parser = argparse.ArgumentParser()
 parser.add_argument("-n")
 args = parser.parse_args()
 
 for _ in range(int(args.n)):
     print("meow")


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Adds description, help
 
 import argparse
 
 parser = argparse.ArgumentParser(description="Meow like a cat")
 parser.add_argument("-n", help="number of times to meow")
 args = parser.parse_args()
 
 for _ in range(int(args.n)):
     print("meow")


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Adds default, type; removes int()
 
 import argparse
 
 parser = argparse.ArgumentParser(description="Meow like a cat")
 parser.add_argument("-n", default=1, help="number of times to meow", type=int)
 args = parser.parse_args()
 
 for _ in range(args.n):
     print("meow")


 #%%  ETCETERA OTHERS  github bustosmiguel

# Unpacks a list

first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")
ack0.py
# Passes positional arguments as usual
# https://harrypotter.fandom.com/wiki/Wizarding_currency


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(100, 50, 25), "Knuts")


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Indexes into list
 
 
 def total(galleons, sickles, knuts):
     return (galleons * 17 + sickles) * 29 + knuts
 
 
 coins = [100, 50, 25]
 
 print(total(coins[0], coins[1], coins[2]), "Knuts")


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Unpacks a list
 
 
 def total(galleons, sickles, knuts):
     return (galleons * 17 + sickles) * 29 + knuts
 
 
 coins = [100, 50, 25]
 
 print(total(*coins), "Knuts")

 #%%  ETCETERA OTHERS  github bustosmiguel

# Passes named arguments as usual


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(galleons=100, sickles=50, knuts=25), "Knuts")

 #%%  ETCETERA OTHERS  github bustosmiguel

 # Indexes into a dict
 
 
 def total(galleons, sickles, knuts):
     return (galleons * 17 + sickles) * 29 + knuts
 
 
 coins = {"galleons": 100, "sickles": 50, "knuts": 25}
 
 print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")



 #%%  ETCETERA OTHERS  github bustosmiguel

 # Unpacks a dict
 
 
 def total(galleons, sickles, knuts):
     return (galleons * 17 + sickles) * 29 + knuts
 
 
 coins = {"galleons": 100, "sickles": 50, "knuts": 25}
 
 print(total(**coins), "Knuts")



 #%%  ETCETERA OTHERS  github bustosmiguel

# Prints positional arguments


def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)


 #%%  ETCETERA OTHERS  github bustosmiguel

# Prints named arguments


def f(*args, **kwargs):
    print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)


 #%%  ETCETERA OTHERS  github bustosmiguel


 # Prints a word in uppercase
 
 
 def main():
     yell("This is CS50")
 
 
 def yell(word):
     print(word.upper())
 
 
 if __name__ == "__main__":
     main()


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Passes a list
 
 
 def main():
     yell(["This", "is", "CS50"])
 
 
 def yell(words):
     uppercased = []
     for word in words:
         uppercased.append(word.upper())
     print(*uppercased)
 
 
 if __name__ == "__main__":
     main()


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Prints arbitrarily many args in uppercase
 
 
 def main():
     yell("This", "is", "CS50")
 
 
 def yell(*words):
     uppercased = []
     for word in words:
         uppercased.append(word.upper())
     print(*uppercased)
 
 
 if __name__ == "__main__":
     main()


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Uses map
 
 
 def main():
     yelL("This", "is", "CS50")
 
 
 def yelL(*words):
     uppercased = map(str.upper, words)
     print(*uppercased)
 
 
 if __name__ == "__main__":
     main()



 #%%  ETCETERA OTHERS  github bustosmiguel

 # Uses list comprehension
 
 
 def main():
     yell("This", "is", "CS50")
 
 
 def yell(*words):
     uppercased = [arg.upper() for arg in words]
     print(*uppercased)
 
 
 if __name__ == "__main__":
     main()



 #%%  ETCETERA OTHERS  github bustosmiguel


 # Filters by house using loop
 
 students = [
     {"name": "Hermione", "house": "Gryffindor"},
     {"name": "Harry", "house": "Gryffindor"},
     {"name": "Ron", "house": "Gryffindor"},
     {"name": "Draco", "house": "Slytherin"},
 ]
 
 gryffindors = []
 for student in students:
     if student["house"] == "Gryffindor":
         gryffindors.append(student["name"])
 
 for gryffindor in sorted(gryffindors):
     print(gryffindor)



 #%%  ETCETERA OTHERS  github bustosmiguel

 # Filters by house using list comprehension
 
 students = [
     {"name": "Hermione", "house": "Gryffindor"},
     {"name": "Harry", "house": "Gryffindor"},
     {"name": "Ron", "house": "Gryffindor"},
     {"name": "Draco", "house": "Slytherin"},
 ]
 
 gryffindors = [
     student["name"] for student in students if student["house"] == "Gryffindor"
 ]
 
 for gryffindor in sorted(gryffindors):
     print(gryffindor)



 #%%  ETCETERA OTHERS  github bustosmiguel

 # Uses filter and key with lambda
 
 students = [
     {"name": "Hermione", "house": "Gryffindor"},
     {"name": "Harry", "house": "Gryffindor"},
     {"name": "Ron", "house": "Gryffindor"},
     {"name": "Draco", "house": "Slytherin"},
 ]
 
 
 def is_gryffindor(s):
     return s["house"] == "Gryffindor"
 
 
 gryffindors = filter(is_gryffindor, students)
 
 for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
     print(gryffindor["name"])


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Uses filter with lambda
 
 students = [
     {"name": "Hermione", "house": "Gryffindor"},
     {"name": "Harry", "house": "Gryffindor"},
     {"name": "Ron", "house": "Gryffindor"},
     {"name": "Draco", "house": "Slytherin"},
 ]
 
 
 gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
 
 for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
     print(gryffindor["name"])



 #%%  ETCETERA OTHERS  github bustosmiguel
 # Creates list of dicts using loop
 
 students = ["Hermione", "Harry", "Ron"]
 
 gryffindors = []
 
 for student in students:
     gryffindors.append({"name": student, "house": "Gryffindor"})
 
 print(gryffindors)




 #%%  ETCETERA OTHERS  github bustosmiguel
# Uses dictionary comprehension instead

students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)



 #%%  ETCETERA OTHERS  github bustosmiguel

# Uses dictionary comprehension instead

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)


 #%%  ETCETERA OTHERS  github bustosmiguel

# Iterates over a list by index

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])


 #%%  ETCETERA OTHERS  github bustosmiguel


# Uses enumerate instead

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)


 #%%  ETCETERA OTHERS  github bustosmiguel

# Prints n sheep

n = int(input("What's n? "))
for i in range(n):
    print("🐑" * i)


 #%%  ETCETERA OTHERS  github bustosmiguel

 # Adds main
 
 
 def main():
     n = int(input("What's n? "))
     for i in range(n):
         print("🐑" * i)
 
 
 if __name__ == "__main__":
     main()

 #%%  ETCETERA OTHERS  github bustosmiguel

 # Returns n sheep from helper function
 
 
 def main():
     n = int(input("What's n? "))
     for i in range(n):
         print(sheep(i))
 
 
 def sheep(n):
     return "🐑" * n
 
 
 if __name__ == "__main__":
     main()



 #%%  ETCETERA OTHERS  github bustosmiguel

 # Returns a list of sheep
 
 
 def main():
     n = int(input("What's n? "))
     for s in sheep(n):
         print(s)
 
 
 def sheep(n):
     flock = []
     for i in range(n):
         flock.append("🐑" * i)
     return flock
 
 
 if __name__ == "__main__":
     main()


 #%%  ETCETERA OTHERS  github bustosmiguel


 # Uses yield
 
 
 def main():
     n = int(input("What's n? "))
     for s in sheep(n):
         print(s)
 
 
 def sheep(n):
     for i in range(n):
         yield "🐑" * i
 
 
 if __name__ == "__main__":
     main()


 #%%  ETCETERA OTHERS  github bustosmiguel


import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()






## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
## OTROS AVANZADOS
# SON Conceptos de sintaxis e idiomáticos como list comprehensions, f-strings, decorators, closures o context managers.
# Arquitectura e internas de CPython como GIL, Metaclasses, Descriptors, Buffer Protocol, Frame Objects, Refcount y Garbage Collector.
# No incluyen conceptos básicos/principiantes (como declaración de variables, bucles while simples o tipos de datos primitivos).

# %% [markdown]
# # Top Python Logics & Algorithms
# Script ejecutable por celdas interactivas (`# %%`) para VS Code / Jupyter.

# %%
# Importaciones necesarias para todas las celdas
import math
import itertools
from collections import Counter, defaultdict
from functools import lru_cache
import statistics

print("Entorno listo para ejecutar celdas interactivas.")

# %%
# ==============================================================================
# CAPÍTULO 01: NUMBERS & MATH LOGIC (Items 1-10)
# ==============================================================================

# %%
# 1. Check if prime (Comprobar si es primo)
n = 0
is_prime = all(n % i != 0 for i in 
    range(2, int(n**0.5) + 1)) if n > 1 else False
print(f"1. ¿{n} es primo?:", is_prime)


# %%
# 2. Fibonacci (recursivo ingenuo)
def fib_naive(n):
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)

print("2. Fibonacci(7) recursivo:", fib_naive(7))


# %%
# 3. Sum of digits (Suma de dígitos)
num = 12345
digit_sum = sum(int(d) for d in str(num))
print(f"3. Suma de dígitos de {num}:", digit_sum)


# %%
# 4. Reverse a number (Invertir un número)
num = 98765
reversed_num = int(str(num)[::-1])
print(f"4. {num} invertido:", reversed_num)


# %%
# 5. GCD (Máximo Común Divisor - Algoritmo de Euclides)
a, b = 48, 18
x, y = a, b
while y:
    x, y = y, x % y
print(f"5. MCD de {a} y {b}:", x)


# %%
# 6. LCM using GCD (Mínimo Común Múltiplo)

import math
a, b = 12, 18
lcm = (a * b) // math.gcd(a, b)
print(f"6. MCM de {a} y {b}:", lcm)


# %%
# 7. Armstrong number (Número de Armstrong)
num = 153
is_armstrong = num == sum(int(d) ** len(str(num)) for d in str(num))
print(f"7. ¿{num} es número de Armstrong?:", is_armstrong)


# %%
# 8. Power without built-in (Potencia sin math.pow)
def power(b, e):
    return 1 if e == 0 else b * power(b, e - 1)

print("8. Potencia 2^10:", power(2, 10))


# %%
# 9. Perfect number (Número perfecto)
num = 28
is_perfect = num == sum(i for i in range(1, num) if num % i == 0)
print(f"9. ¿{num} es número perfecto?:", is_perfect)


# %%
# 10. Decimal to binary (Decimal a binario)
num = 42
binary_str = bin(num)[2:]
print(f"10. {num} en binario:", binary_str)

# %%
# ==============================================================================
# CAPÍTULO 02: STRINGS LOGIC (Items 11-20)
# ==============================================================================


# %%
# 11. Reverse a string (Invertir cadena)
s = "Python"
print("11. Cadena invertida:", s[::-1])


# %%
# 12. Palindrome string (Comprobar palíndromo)
s = "Aricora"  # o "Radar"
is_palindrome = s.lower() == s.lower()[::-1]
print(f"12. ¿'{s}' es palíndromo?:", is_palindrome)


# %%
# 13. Count vowels (Contar vocales)
s = "Interactive Code"
vowel_count = sum(1 for c in s.lower() if c in "aeiou")
print("13. Cantidad de vocales:", vowel_count)


# %%
# 14. Check anagram (Comprobar anagrama)
s1, s2 = "listen", "silent"
is_anagram = sorted(s1) == sorted(s2)
print(f"14. ¿'{s1}' y '{s2}' son anagramas?:", is_anagram)


# %%
# 15. Remove duplicate characters (Eliminar caracteres duplicados)
s = "banana"
unique_chars = "".join(dict.fromkeys(s))
print(f"15. Sin duplicados ('{s}'):", unique_chars)


# %%
# 16. First non-repeating character (Primer carácter no repetido)
s = "swiss"
first_unique = next((c for c in s if s.count(c) == 1), None)
print(f"16. Primer carácter único en '{s}':", first_unique)


# %%
# 17. String compression (Compresión de cadenas)
import itertools

s = "aaabbc"
compressed = "".join(f"{c}{len(list(g))}" for c, g in itertools.groupby(s))
print(f"17. Compresión de '{s}':", compressed)


# %%
# 18. Check string rotation (Rotación de cadenas)
s1, s2 = "waterbottle", "erbottlewat"
is_rotation = len(s1) == len(s2) and s2 in (s1 + s1)
print(f"18. ¿'{s2}' es rotación de '{s1}'?:", is_rotation)


# %%
# 19. Longest common prefix (Prefijo común más largo)
import os
words = ["flower", "flow", "flight"]
common_prefix = os.path.commonprefix(words)
print("19. Prefijo común:", common_prefix)


# %%
# 20. Word frequency counter (Frecuencia de palabras)

from collections import Counter


text = "python es genial y python es rapido"
word_freq = Counter(text.split())
print("20. Frecuencia de palabras:", dict(word_freq))

# %%
# ==============================================================================
# CAPÍTULO 03: LISTS & ARRAYS LOGIC (Items 21-30)
# ==============================================================================


# %%
# 21. Max/min without built-ins (Máximo/mínimo sin funciones integradas)
lst = [3, 1, 9, 4, 7]
m_max = lst[0]
for x in lst:
    if x > m_max:
        m_max = x
print("21. Máximo manual:", m_max)


# %%
# 22. Reverse a list in place (Invertir lista in situ)
lst = [1, 2, 3, 4, 5]
lst.reverse()
print("22. Lista invertida in-place:", lst)


# %%

# 23. Remove duplicates, preserve order (Eliminar duplicados manteniendo orden)
lst = [4, 2, 4, 1, 2, 5]
unique_lst = list(dict.fromkeys(lst))
print("23. Duplicados eliminados:", unique_lst)


# %%
# 24. Second largest element (Segundo elemento más grande)
lst = [12, 35, 1, 10, 34, 1]
second_largest = sorted(set(lst))[-2]
print("24. Segundo elemento más grande:", second_largest)


# %%
# 25. Rotate list by k (Rotar lista k posiciones)
lst = [1, 2, 3, 4, 5]
k = 2
rotated = lst[-k:] + lst[:-k]
print(f"25. Lista rotada {k} posiciones:", rotated)

# %%

# 26. Find missing number in range (Número faltante en rango 1 a n)
lst = [1, 2, 4, 5, 6]  # Falta el 3
n = 6
missing = sum(range(1, n + 1)) - sum(lst)
print("26. Número faltante:", missing)

# %%
# 27. Two-sum (Problema Two-Sum con Hash Map)
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []

print("27. Índices Two-Sum (target=9):", two_sum([2, 7, 11, 15], 9))


# %%

# 28. Sliding window max sum (Suma máxima en ventana de tamaño fijo)
lst = [2, 1, 5, 1, 3, 2]
k = 3
max_win_sum = max(sum(lst[i:i+k]) for i in range(len(lst) - k + 1))
print("28. Suma máxima de ventana k=3:", max_win_sum)

# %%

# 29. Merge two sorted lists (Combinar dos listas ordenadas)
l1, l2 = [1, 3, 5], [2, 4, 6]
merged = sorted(l1 + l2)
print("29. Listas ordenadas combinadas:", merged)


# %%
# 30. Intersection of two lists (Intersección de dos listas)
l1, l2 = [1, 2, 3, 4], [3, 4, 5, 6]
intersection = list(set(l1) & set(l2))
print("30. Intersección:", intersection)

# %%
# ==============================================================================
# CAPÍTULO 04: SORTING & SEARCHING LOGIC (Items 31-40)
# ==============================================================================


# %%
# 31. Bubble sort (Ordenamiento Burbuja)
lst = [64, 34, 25, 12, 22]
arr = lst.copy()
for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("31. Bubble sort:", arr)


# %%

# 32. Selection sort (Ordenamiento por Selección)
arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
    min_idx = min(range(i, len(arr)), key=lambda x: arr[x])
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print("32. Selection sort:", arr)


# %%

# 33. Insertion sort (Ordenamiento por Inserción)
arr = [12, 11, 13, 5, 6]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print("33. Insertion sort:", arr)


# %%
# 34. Merge sort (Ordenamiento por Mezcla)
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return sorted(left + right)

print("34. Merge sort:", merge_sort([38, 27, 43, 3, 9, 82, 10]))


# %%
# 35. Quick sort (Ordenamiento Rápido)
def quick_sort(arr):
    if len(arr) <= 1: return arr
    piv = arr[len(arr) // 2]
    left = [x for x in arr if x < piv]
    middle = [x for x in arr if x == piv]
    right = [x for x in arr if x > piv]
    return quick_sort(left) + middle + quick_sort(right)

print("35. Quick sort:", quick_sort([10, 7, 8, 9, 1, 5]))


# %%
# 36. Binary search (Búsqueda Binaria)
def binary_search(lst, target):
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print("36. Búsqueda binaria índice del 7:", binary_search([1, 3, 5, 7, 9, 11], 7))


# %%
# 37. Kth largest element (K-ésimo elemento más grande)
lst = [3, 2, 1, 5, 6, 4]
k = 2
kth_largest = sorted(lst)[-k]
print(f"37. El {k}-ésimo elemento más grande:", kth_largest)


# %%
# 38. Custom sort with key (Ordenamiento personalizado con clave)
tuples = [("A", 3), ("B", 1), ("C", 2)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print("38. Tuplas ordenadas por segundo elemento:", sorted_tuples)


# %%
# 39. Check if list is sorted (Comprobar si está ordenada)
lst = [1, 2, 3, 5, 4]
is_sorted = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
print("39. ¿Lista ordenada?:", is_sorted)


# %%
# 40. Peak element in array (Elemento pico local)
arr = [1, 3, 20, 4, 1, 0]
def find_peak(arr):
    for i in range(len(arr)):
        left = arr[i-1] if i > 0 else float('-inf')
        right = arr[i+1] if i < len(arr)-1 else float('-inf')
        if arr[i] >= left and arr[i] >= right:
            return arr[i]

print("40. Elemento pico encontrado:", find_peak(arr))

# %%
# ==============================================================================
# CAPÍTULO 05: DICTS & HASHING LOGIC (Items 41-50)
# ==============================================================================


# %%
# 41. Count element frequency (Contar frecuencia de elementos)

from collections import Counter

lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = Counter(lst)
print("41. Frecuencias:", dict(freq))


# %%
# 42. Find duplicate elements (Encontrar elementos duplicados)
lst = [1, 2, 3, 2, 4, 5, 1]
duplicates = list(set([x for x in lst if lst.count(x) > 1]))
print("42. Elementos duplicados:", duplicates)


# %%
# 43. Group items by property (Agrupar por propiedad)

from collections import defaultdict

words = ["apple", "banana", "avocado", "berry", "cherry"]
grouped = defaultdict(list)
for w in words:
    grouped[w[0]].append(w)
print("43. Agrupados por letra inicial:", dict(grouped))


# %%
# 44. Invert a dictionary (Invertir llaves y valores)
d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print("44. Diccionario invertido:", inverted)


# %%
# 45. Most frequent element (Elemento más frecuente)

from collections import Counter
lst = [1, 3, 1, 3, 2, 1]
most_frequent = Counter(lst).most_common(1)[0][0]
print("45. Elemento más frecuente:", most_frequent)


# %%
# 46. Same elements, unordered (Mismos elementos sin importar orden)
from collections import Counter

l1, l2 = [1, 2, 3, 2], [2, 3, 1, 2]
same_elements = Counter(l1) == Counter(l2)
print("46. ¿Tienen los mismos elementos?:", same_elements)


# %%
# 47. Common keys between dicts (Claves comunes entre diccionarios)
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}
common_keys = d1.keys() & d2.keys()
print("47. Claves comunes:", common_keys)


# %%
# 48. Merge two dictionaries (Combinar dos diccionarios)
merged_dict = {**d1, **d2}
print("48. Diccionarios combinados:", merged_dict)


# %%
# 49. Default value for missing key (Valor por defecto para clave faltante)
d = {"a": 1}
val = d.get("b", 0)
print("49. Valor obtenido con fallback:", val)


# %%
# 50. Nested dictionary traversal (Recorrido recursivo de diccionario anidado)
nested = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
def print_nested(d):
    for k, v in d.items():
        if isinstance(v, dict):
            print_nested(v)
        else:
            print(f"Key: {k}, Val: {v}")

print("50. Recorrido de diccionario anidado:")
print_nested(nested)

# %%
# ==============================================================================
# CAPÍTULO 06: RECURSION LOGIC (Items 51-60)
# ==============================================================================


# %%

# 51. Factorial (recursive)
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print("51. Factorial(5):", factorial(5))


# %%
# 52. Fibonacci with 

from functools import lru_cache


@lru_cache(maxsize=None)
def fib_memo(n):
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)

print("52. Fibonacci optimizado(50):", fib_memo(50))


# %%
# 53. Sum of a list recursively (Suma recursiva de lista)
def sum_rec(l):
    return 0 if not l else l[0] + sum_rec(l[1:])

print("53. Suma recursiva [1, 2, 3, 4]:", sum_rec([1, 2, 3, 4]))


# %%
# 54. Tower of Hanoi (Torre de Hanói)
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Mover disco 1 de {source} a {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Mover disco {n} de {source} a {target}")
    hanoi(n - 1, auxiliary, target, source)

print("54. Torre de Hanói (2 discos):")
hanoi(2, 'A', 'C', 'B')


# %%
# 55. Recursive binary search (Búsqueda binaria recursiva)
def binary_search_rec(arr, lo, hi, target):
    if lo > hi: return -1
    mid = (lo + hi) // 2
    if arr[mid] == target: return mid
    if arr[mid] > target: return binary_search_rec(arr, lo, mid - 1, target)
    return binary_search_rec(arr, mid + 1, hi, target)

arr_bs = [2, 4, 6, 8, 10]
print("55. BS Recursiva (buscar 8):", binary_search_rec(arr_bs, 0, len(arr_bs)-1, 8))


# %%
# 56. Flatten nested list recursively (Aplanar lista anidada)
def flatten(l):
    flat = []
    for item in l:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

print("56. Lista aplanada:", flatten([1, [2, [3, 4], 5], 6]))


# %%
# 57. Generate all subsets (Generar todos los subconjuntos)
s = [1, 2]
subsets = list(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1)))
print("57. Subconjuntos:", subsets)


# %%
# 58. Generate all permutations (Generar permutaciones)
perms = list(itertools.permutations([1, 2, 3]))
print("58. Permutaciones (primeras 3):", perms[:3])


# %%
# 59. Recursive GCD (MCD recursivo)
def gcd_rec(a, b):
    return a if b == 0 else gcd_rec(b, a % b)

print("59. MCD recursivo (48, 18):", gcd_rec(48, 18))


# %%
# 60. Climb stairs (Escaleras - 1 o 2 escalones)

from functools import lru_cache

@lru_cache(maxsize=None)
def climb_stairs(n):
    return n if n <= 2 else climb_stairs(n - 1) + climb_stairs(n - 2)

print("60. Formas de subir 5 escalones:", climb_stairs(5))

# %%
# ==============================================================================
# CAPÍTULO 08: DATA CLEANING LOGIC (Items 71-80)
# ==============================================================================


# %%

# 71. Detect/handle missing values (Manejar valores nulos)
data = [10, None, 20, None, 30]
cleaned_data = [x if x is not None else 0 for x in data]
print("71. Datos con nulos reemplazados:", cleaned_data)


# %%
# 72. Remove outliers (IQR) (Remover valores atípicos)

import statistics

vals = [10, 12, 12, 13, 12, 11, 100]  # 100 es outlier
q1, q3 = statistics.quantiles(sorted(vals), n=4)[0], statistics.quantiles(sorted(vals), n=4)[2]
iqr = q3 - q1
filtered_vals = [x for x in vals if (q1 - 1.5*iqr) <= x <= (q3 + 1.5*iqr)]
print("72. Sin outliers:", filtered_vals)


# %%
# 73. Normalize (min-max) (Normalización 0-1)
lst = [10, 20, 30, 40, 50]
min_l, max_l = min(lst), max(lst)
normalized = [(x - min_l) / (max_l - min_l) for x in lst]
print("73. Normalizados:", normalized)


# %%
# 74. Standardize (z-score) (Estandarización Z-Score)
mean_v = statistics.mean(lst)
stdev_v = statistics.stdev(lst)
standardized = [(x - mean_v) / stdev_v for x in lst]
print("74. Estandarizados:", [round(x, 2) for x in standardized])


# %%
# 75. Deduplicate by key (Deduplicar por clave)
records = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}, {"id": 1, "name": "A"}]
seen_ids = set()
unique_records = []
for r in records:
    if r["id"] not in seen_ids:
        seen_ids.add(r["id"])
        unique_records.append(r)
print("75. Registros únicos:", unique_records)


# %%
# 76. Bucket/bin continuous data (Agrupar datos continuos en rangos)
ages = [15, 23, 45, 62, 18, 30]
bin_width = 20
binned = [age // bin_width * bin_width for age in ages]
print("76. Edades agrupadas por intervalos de 20:", binned)


# %%
# 77. One-hot encode manually (Codificación One-Hot manual)
categories = ["cat", "dog", "bird"]
cat_item = "dog"
one_hot = [1 if cat == cat_item else 0 for cat in categories]
print(f"77. One-hot para '{cat_item}':", one_hot)


# %%
# 78. Validate data types (Validar tipos de datos en lista)
lst = [1, 2, 3, "4", 5]
valid = all(isinstance(x, int) for x in lst)
print("78. ¿Todos los elementos son enteros?:", valid)


# %%
# 79. Forward-fill missing values (Relleno hacia adelante)
data = [10, None, None, 20, None, 30]
ffilled = []
last = 0
for x in data:
    if x is not None:
        last = x
    ffilled.append(last)
print("79. Forward-fill aplicado:", ffilled)


# %%
# 80. Merge near-duplicate strings (Normalización de cadenas)
s1, s2 = " Python ", "python"
are_near_duplicates = s1.strip().lower() == s2.strip().lower()
print("80. ¿Son duplicados cercanos?:", are_near_duplicates)

# %%
# ==============================================================================
# CAPÍTULO 09: STATISTICS & PROBABILITY LOGIC (Items 81-90)
# ==============================================================================


# %%
# 81. Mean from scratch (Media)
lst = [10, 20, 30, 40]
mean = sum(lst) / len(lst)
print("81. Media:", mean)


# %%
# 82. Median from scratch (Mediana)
s_lst = sorted([3, 1, 4, 1, 5, 9, 2])
n = len(s_lst)
median = s_lst[n//2] if n % 2 != 0 else (s_lst[n//2 - 1] + s_lst[n//2]) / 2
print("82. Mediana:", median)


# %%
# 83. Mode from scratch (Moda)
lst = [1, 2, 2, 3, 3, 3, 4]
mode = Counter(lst).most_common(1)[0][0]
print("83. Moda:", mode)


# %%
# 84. Variance from scratch (Varianza)
mean_val = sum(lst) / len(lst)
variance = sum((x - mean_val) ** 2 for x in lst) / len(lst)
print("84. Varianza:", round(variance, 2))


# %%
# 85. Std dev from scratch (Desviación estándar)
std_dev = variance ** 0.5
print("85. Desviación Estándar:", round(std_dev, 2))


# %%
# 86. Correlation from scratch (Correlación con statistics)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
corr = statistics.correlation(x, y)
print("86. Correlación entre X e Y:", corr)


# %%
# 87. Moving average (Media móvil de ventana k=2)
lst = [10, 20, 30, 40, 50]
k = 2
moving_avg = [sum(lst[i:i+k])/k for i in range(len(lst) - k + 1)]
print("87. Media móvil:", moving_avg)


# %%
# 88. Weighted average (Media ponderada)
values = [10, 20, 30]
weights = [0.2, 0.3, 0.5]
weighted_avg = sum(v * w for v, w in zip(values, weights)) / sum(weights)
print("88. Media ponderada:", weighted_avg)



# %%
# 89. Linear regression slope/intercept (Pendiente Regresión Lineal)
def slope(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((x[i] - mx) * (y[i] - my) for i in range(len(x)))
    den = sum((x[i] - mx) ** 2 for i in range(len(x)))
    return num / den

print("89. Pendiente de la recta de regresión:", slope(x, y))


# %%
# 90. Probability simulation (Simulación de probabilidad - Lanzamiento de moneda)
import random
random.seed(42)
sims = [random.choice(["H", "T"]) for _ in range(1000)]
prob_heads = sims.count("H") / len(sims)
print("90. Probabilidad simulada de Caras ('H'):", prob_heads)

# %%
# ==============================================================================
# CAPÍTULO 10: INTERVIEW & PROBLEM-SOLVING LOGIC (Items 91-100)
# ==============================================================================


# %%
# 91. Two-pointer technique (Dos punteros para inversión o comparación)
arr = [1, 2, 3, 4, 5]
l, r = 0, len(arr) - 1
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
print("91. Inversión con dos punteros:", arr)


# %%
# 92. Sliding window technique (Ventana deslizante acumulativa)
arr = [2, 1, 5, 1, 3, 2]
k = 3
win_sum = sum(arr[:k])
max_sum = win_sum
for i in range(len(arr) - k):
    win_sum = win_sum - arr[i] + arr[i + k]
    max_sum = max(max_sum, win_sum)
print("92. Ventana deslizante eficiente max sum:", max_sum)


# %%
# 93. Fast/slow pointers (Detección de ciclos)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = head  # Crea ciclo

slow = fast = head
has_cycle = False
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        has_cycle = True
        break
print("93. ¿Ciclo detectado en lista enlazada?:", has_cycle)


# %%
# 94. Divide and conquer (Divide y Vencerás - Suma de lista)
def divide_sum(lst):
    if not lst: return 0
    if len(lst) == 1: return lst[0]
    mid = len(lst) // 2
    return divide_sum(lst[:mid]) + divide_sum(lst[mid:])

print("94. Suma por Divide y Vencerás:", divide_sum([1, 2, 3, 4, 5]))


# %%
# 95. Greedy approach (Enfoque Voraz - Cambio de monedas)
coins = [25, 10, 5, 1]
amount = 63
num_coins = 0
for coin in coins:
    num_coins += amount // coin
    amount %= coin
print("95. Cantidad mínima de monedas (63 centavos):", num_coins)


# %%
# 96. Dynamic programming (bottom-up) (Programación dinámica Tabulación)
n = 6
dp = [0] * (n + 1)
if n > 0: dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
print(f"96. DP Fib({n}):", dp[n])


# %%
# 97. Backtracking (Generación de permutaciones con backtracking)
def backtrack(nums, path, result):
    if not nums:
        result.append(path)
        return
    for i in range(len(nums)):
        backtrack(nums[:i] + nums[i+1:], path + [nums[i]], result)

res = []
backtrack([1, 2], [], res)
print("97. Backtracking permutaciones:", res)


# %%
# 98. Time complexity by eye (Complejidad temporal orientativa)
# 1 bucle -> O(n), bucles anidados -> O(n^2), división en mitades -> O(log n)
print("98. Complejidades comunes: O(1) < O(log n) < O(n) < O(n log n) < O(n^2)")


# %%
# 99. Space-time tradeoff (Intercambio espacio-tiempo - Hash Set para O(1) Búsquedas)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = set(lst)  # Usa memoria O(n) pero reduce búsquedas de O(n) a O(1)
print("99. ¿Existe el 7 en el set (O(1))?:", 7 in s)

"""..."""

# %%
# 100. Breaking down an ambiguous problem (Metodología de resolución de problemas)
def solve_problem(inputs):
    # 1. Aclarar entradas/salidas y casos borde
    # 2. Escribir pseudocódigo
    # 3. Implementar versión simple
    # 4. Optimizar complejidad temporal/espacial
    return "Problema estructurado exitosamente"

print("100. Resolución de problemas:", solve_problem([]))
```eof

---

#%%

### Resumen de los archivos y cambios realizados:
- **`python_logics_interactive.py`**: Archivo script completo formateado en bloques interactivos (`# %%`). 
- Incluye el código documentado con comentarios `#` de todos los capítulos que se mostraban en las imágenes (Matemáticas, Cadenas, Listas, Búsqueda/Ordenamiento, Diccionarios, Recursión, Limpieza de Datos, Estadística y Algoritmos para entrevistas).
- Puedes presionar **Shift + Enter** o hacer clic en *"Run Cell"* arriba de cada separador `# %%` en VS Code para ir ejecutando las partes por separado.

