


########### VIDEO_1 FUNCTIONS AND VARIABLES


#%% NOTAS GITHUB BUSTOSMIGUEL
print("hello, world")




#%% NOTAS GITHUB BUSTOSMIGUEL
name = input("What's your name? ")
print("hello,")
print(name)




#%% NOTAS GITHUB BUSTOSMIGUEL
name = input("What's your name? ")
print("hello, " + name)




#%% NOTAS GITHUB BUSTOSMIGUEL
name = input("What's your name? ")
print("hello,", name)




#%% NOTAS GITHUB BUSTOSMIGUEL
name = input("What's your name? ")
print("hello, ", end="")
print(name)





#%%  NOTAS GITHUB BUSTOSMIGUEL
name = input("What's your name? ")
print(f"hello, {name}")





#%% NOTAS GITHUB BUSTOSMIGUEL
name = input("What's your name? ").strip().title()
print(f"hello, {name}")




#%% NOTAS GITHUB BUSTOSMIGUEL
name = input("What´s your name?").strip().title()
first, last = name.split(" ")
print(f"Hello, {first}")





#%% NOTAS GITHUB BUSTOSMIGUEL
print("Hello,", name, sep = " W", end = "\n")





# %% NOTAS GITHUB BUSTOSMIGUEL
print(f"Hello, {name}")





# %% NOTAS GITHUB BUSTOSMIGUEL
class greet:
    def __init__(self, hi):
        self.hi = hi

    def greet_action(self):
        print(f"here {self.hi}")

ho = greet("Hi")
ho.greet_action()















# INTEGERS (0, 1, 2.... ETC)


# %%NOTAS GITHUB BUSTOSMIGUEL
# HERE I GO Escribir en la terminal: python
# Aparecerán unas flechitas en la terminal, eso es INTERACTIVE MODE

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





# %%
