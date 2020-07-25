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

from singly_linked_list import LinkedList

# queue class
class Queue:
    def __init__(self): # initialize constructor
        self.size = 0 # set size to 0
        self.storage = LinkedList() # set storage to LinkedList class

    def __len__(self): # show length method
        return self.storage.get_length()

    def enqueue(self, value): # add value method
        self.storage.add_to_tail(value) # append value to items list
        self.size += 1 # add to length

    def dequeue(self): # remove value method
        value = self.storage.remove_head()
        if value is not None:
            self.size -= 1 # subtract to length
        return value



## Notes ##
