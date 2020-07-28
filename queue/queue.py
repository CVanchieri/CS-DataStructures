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

from singly_linked_list import LinkedList # import the LinkedList class

class Queue: # queue class
    def __init__(self): # initialize constructor method
        self.size = 0 # set size to 0
        self.storage = LinkedList() # set storage to LinkedList class

    def __len__(self): # method to show length
        return self.storage.get_length()

    def enqueue(self, value): # method to add a value to the que
        self.storage.add_to_tail(value) # append value to items list
        self.size += 1 # add to length

    def dequeue(self): # method to remove a value from the que
        value = self.storage.remove_head() # remove the head value with remove_head method and store it as a value
        if value is not None: # if value is not empty
            self.size -= 1 # remove 1 from the length
        return value
