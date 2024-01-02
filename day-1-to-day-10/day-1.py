#  Write a Python program to print "Hello, World!" to the console.
print("Day 1 - First day of python learning")
print("Hello World!")
print("*" * 10)


# variables and inputs
name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")

print(name, 'likes', favorite_color)


# Pounds to Kilograms conversion
print("Pounds to kilogram conversion")

# create a variable to store the user's weight
weight_in_pounds = input("What is your weight?(in pounds) ")
weight_in_kg =  str(int(weight_in_pounds) // 2.2)
print(weight_in_kg + "kg" )