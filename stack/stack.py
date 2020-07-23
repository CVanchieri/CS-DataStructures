"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
# stack class
class Stack:
    def __init__(self): # initialize constructor
        self.size = 0 # set size to 0
        self.items = [] # set storage to empty list

    def __len__(self): # show length method
        return self.size

    def push(self, value): # add value method
        self.items.append(value) # append value to items list
        self.size += 1 # add to length

    def pop(self): # remove value method
        if self.items != []: # if items list is not empty
            self.size -= 1 # subtract from length
            return self.items.pop()
