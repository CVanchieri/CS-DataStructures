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
class Stack: # stack class
    def __init__(self): # initializer constructor method
        self.size = 0 # set size to 0
        self.items = [] # set storage items to empty list

    def __len__(self): # method to show the length
        return self.size

    def push(self, value): # method to add a value
        self.items.append(value) # append the value to items list
        self.size += 1 # add 1 to the length

    def pop(self): # method to remove a value
        if self.items != []: # if items list is not empty
            self.size -= 1 # remove 1 from the length
            return self.items.pop()
