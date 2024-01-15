
#   # Recursion

arr = [1,2,3]

def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else: return num_list[0] + list_sum(num_list[1:])
    

def factorial(n):
    if n == 0:
        return 1
    else: return  n * factorial(n-1)
    
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))