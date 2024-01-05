
#   #  Functions

#  Exercise

'''
Write a Python function to check if a string is a palindrome
'''

def isPalindrome(string: str) -> bool:
    if string == string[::-1]:
        return True
    else:
        return False
    

print(isPalindrome("level"))

'''
Write a Python function to find the factorial of a large number using recursion
'''

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

'''
Write a Python function to check if a number is a palindrome using recursion.
'''



def isNumPalindrome(x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        
print(isNumPalindrome(121))