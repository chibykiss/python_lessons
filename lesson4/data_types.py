import math
#string datatypes

firstname = "Emmanuel"
lastname = "Ezuma"

# print(type(firstname))
# print(type(lastname) == str)
# print(isinstance(firstname, str))

#constructor function

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
# fullname = firstname + " " + lastname
# fullname += " is a software engineer"
# print(fullname)

# casting a number to a string
# decade = str(2020)
# print(type(decade))

#concatenation
multiline = "its a good day to be alive"
# print(multiline.replace("good", "great")) #replace a word in a string
# print(multiline.upper()) #convert to uppercase

# print(len(multiline)) #length of a string
# multiline += "                                   "
# multiline = "                         " + multiline 

# print(len(multiline.strip()))
# print(len(multiline.rstrip()))
# print(len(multiline.lstrip()))

# print("")

# Build a menu
# title = "menu".upper()
# print(title.center(20, "_"))
# print("Coffee".ljust(16, ".") + "  N500".rjust(4))
# print("Muffin".ljust(16, ".") + "  N1000".rjust(4))
# print("Pancake".ljust(16, ".") + "  N1500".rjust(4))
# print("CheeseCake".ljust(16, ".") + "  N700".rjust(4))

# print("")

# string index values
# print(firstname[-1])
# print(firstname[0:-1])
# print(firstname[0:])

# some methods return a boolean value
print(firstname.startswith("E"))
print(firstname.endswith("u"))

#boolean datatypes
myval = True
x = bool(False)
print(type(myval))
print(isinstance(x, bool))

# Numeric datatypes
# int, float, complex

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.49
print(type(gpa))
print(isinstance(gpa, float))

#complex type
comp_value = 3 + 4j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#built in functions for numeric types
print(abs(-10)) #absolute value
print(round(gpa)) #rounds to the nearest integer
print(round(gpa, 1)) #rounds to the nearest decimal place
print(pow(2, 3)) #power of a number


print(math.pi) #square root of a number
print(math.sqrt(16)) #square root of a number
print(math.ceil(gpa))

#cast string to int
zipcode = "10001"
zipval = int(zipcode)
print(type(zipval))