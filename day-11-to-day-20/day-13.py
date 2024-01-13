
#   # Linked Lists

'''
• List(): creates a new list that is empty.
• add(item): adds a new item to the list
• remove(item): removes the item from the list.
• search(item): searches for the item in the list and returns a boolean value
• is_empty() : checks whether the list is empty and returns a boolean value.
• size(): returns the number of items in the list
• append(item): adds a new item to the end of the list
• index(item): returns the position of item in the list.
• insert(pos,item): adds a new item to the list at position pos.
• pop(): removes and returns the last item in the list.
• pop(pos): removes and returns the item at position pos.
'''

# The Nod Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data
    
    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self): # O(1)
        if self.head is None:
            print("The list is empty")
        else: print("The list is not empty")

    def add(self, item): # O(1)
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self): # O(n)
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    
    def remove(self, item): # O(n)
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item): # O(n)
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True


list = LinkedList()
list.add(1)
print(list.is_empty())