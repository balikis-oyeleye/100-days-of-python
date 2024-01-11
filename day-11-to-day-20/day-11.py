from packages.deque import Deque

#   #  Basic Data Structures

#   #  Deque pronounced as "deck"

'''
items are added and removed from either end, either front or rear

operations:
- Deque() creates a new deque that is empty
- add_front(item) adds a new item to the front of the deque. 
- add_rear(item) adds a new item to the rear of the deque
- remove_front() removes the item at the front of the deque
- remove_rear() removes the item at the rear of the deque
- is_empty() returns True if the deque is empty
- size() returns the number of items in the deque
'''

# Exercise: Palindrome Checker - using Deque

def palindrome_checker(string):
    char_deque = Deque()

    for ch in string:
        char_deque.add_rear(ch)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal

print(palindrome_checker("madam"))