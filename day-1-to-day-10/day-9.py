from packages.stack import Stack

#   #  Basic Data Structures
#   #  Stacks: LIFO-Last In First Out

'''
The stack operations are: 
- Stack(): Creates an empty stack
- push(): Adds an item to the top of the stack
- pop(): Removes an item from the top of the stack
- peek(): Returns the item at the top of the stack
- isEmpty(): Returns True if the stack is empty
- size(): Returns the number of items in the stack
'''

#   #  Exercise: Simple Balance Parenthesis Checker - using Stack class

def parenthesis_checker(symbol_string):
    stack = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            stack.push(symbol)
        elif symbol == ")":
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    return stack.isEmpty()

print(parenthesis_checker("((()))"))