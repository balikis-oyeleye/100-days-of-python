from packages.queue import Queue

#   #  Basic Data Structures

#   #  Queues: FIFO-First In First Out

'''
- Queue(): Creates an empty queue
- enqueue(): Adds an item to the back of the queue
- dequeue(): Removes an item from the front of the queue
- isEmpty(): Returns True if the queue is empty. Return a boolean     value
- size(): Returns the number of items in the queue
'''

q = Queue()
q.dequeue()
q.enqueue(1)
print(q.size())


