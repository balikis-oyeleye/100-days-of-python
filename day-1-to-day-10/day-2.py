import math

# Data types

# Strings

course = "Python for Beginners"
print(course[::-1]) 
print(course[8:0:-1])
print(course[1:-1])

print(f'{course} full')     

# Arithmetic operations

x = (2 + 3) * 10 - 3
print(x)

print(math.ceil(2.9))
print(math.floor(2.1))

# Exercise

''' 
Write a Python program to add two numbers. 
'''

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
sum = int(first_number) + int(second_number)

print(f'The sum of the first number and second number is {sum}')


'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.
'''

present_age = int(input("What is your preset age? "))

years_remaining = 90 - present_age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365


print(f'You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.')


'''
Write a Python program that calculates the area of a circle given its radius.
'''

radius_of_circle = int(input("Input the radius of the circle: "))
area = math.pi * (radius_of_circle ** 2)
print(round(area, 2))