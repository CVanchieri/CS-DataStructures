"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# queue class
class Queue:
    def __init__(self): # initialize constructor
        self.size = 0 # set size to 0
        self.storage = [] # set storage to empty list

    def __len__(self): # show length method
        return self.size

    def enqueue(self, value): # add value method
        self.storage.append(value) # append value to items list
        self.size += 1 # add to length

    def dequeue(self): # remove value method
        if self.storage != []: # if items list is not empty
            self.size -= 1 # subtract from length
            return self.storage.pop(0)
