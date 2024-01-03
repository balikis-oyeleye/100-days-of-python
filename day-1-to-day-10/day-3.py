
# # Conditional Statements: if, elif, else
# # Logical Operators: and, or, not
# # Comparison Operators: ==, !=, >, <, >=, <=
# # While Loop
# # For Loop

#  exercise 

'''
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February
'''

given_year = int(input("Enter a year: "))

if given_year % 4 == 0 and given_year % 100 != 0 or given_year % 400 == 0:
    print(f"{given_year} is a leap year")
else:
    print(f"{given_year} is not a leap year")

'''
Guessing game
'''

guess_remaining = 3
secret_number = 5

while guess_remaining > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("You won! 🎉")
        break
    else:
        guess_remaining -= 1
        if guess_remaining == 0:
            print("You lost! 😢")
        else:
            print(f"You have {guess_remaining} guesses left")
    

'''
Write a Python program to check if a number is prime 
'''

number = int(input("Enter a number: "))

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not a prime number")
        break
else: print(f"{number} is a prime number")
  