class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def all_list(self):
        arr = []
        current = self.head
        while current:
            arr.insert(0,current.data)
            current = current.next
        return arr
        
    def is_empty(self):
        if self.head == None:
            return True
        else: return False
        
    def append(self, item):
        current = Node(item)
        current.next = self.head
        self.head = current
        
    def delete(self, item):
        if self.head == None:
            return []
            
        if self.head.data == item:
            self.head = self.head.next
            return
        elif self.head.next == None:
            return "Item doesn't exist"
        
        current = self.head
        previous = None
        is_found = False
        
        while not is_found:
            if current.data == item:
                is_found = True
            else:
                previous = current
                current = current.next
            
        if current == None:
            return "Item not found"
        else: previous.next = current.next
        
    def reverse(self):
        current = self.head
        previous = None
        
        while current:
            next_node = current.next 
            current.next = previous 
            previous = current 
            current = next_node 
        self.head = previous
        
    def search(self, item):
        if self.head == None:
            return False
        current = self.head
        found = False
       
        while not found:
            if current.data == item:
                found = True
                return found
            else: 
                if current.next == None:
                    return False
                else: current = current.next
    
       

        
list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(5)

print(list.all_list())
list.delete(5)
print(list.all_list())


