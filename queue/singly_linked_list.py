
class Node: # node class
    def __init__(self, value=None, next_node=None): # initializer constructor method
        self.value = value # set the value node
        self.next_node = next_node # set the next node

    def get_value(self): # method to get current value
        return self.value

    def get_next(self): #  method to get next value
        return self.next_node

    def set_next(self, new_next): #method the set the next value
        self.next_node = new_next

class LinkedList: # linked list class
    def __init__ (self): # initialize constructor method
        self.head = None # set the head
        self.tail = None # set the tail
        self.length = 0 # set the length

    def get_length(self): # method to get length
        return self.length

    def add_to_head(self, value): # method to add to head
        new_node = Node(value, self.head) # create a new_node with Node class
        self.head = new_node # set the head as the new_node
        if self.length == 0: # if length is 0
            self.tail = new_node # set tail to new_node
        self.length += 1 # add 1 to the length

    def add_to_tail(self, value): # add value to the tail
        new_node = Node(value) # create a new_node with the Node class
        if self.head is None and self.tail is None: # if empty
            self.head = new_node # set the head as the new_node
        else:
            self.tail.set_next(new_node) # set the tail with the new_node using the set_next method
        self.tail = new_node # set te tail to the new_node
        self.length += 1 # add 1 to the length

    def remove_head(self): # method to remove the head
        if self.head is None: # if no head
            return None

        elif self.head == self.tail: # if the head = is the tail
            value = self.head.get_value() # store the head value with get_value method
            self.head = None # set head to None
            self.tail = None # set tail to None
            self.length -= 1 # remove 1 from the length
            return value

        else:
            value = self.head.get_value() # store the head value with get_value method
            self.head = self.head.get_next() # set the head as the next value with the get_next method
            self.length -= 1 # remove 1 from the length
            return value

    def remove_tail(self): # method to remove the tail
        if self.tail is None: # if empty
            return None

        elif self.tail == self.head: # if length is 1, tail = head
            value = self.tail.get_value() # store the tail value with get_value method
            self.head = None # set the head to to None
            self.tail = None # set the tail to None
            self.length -= 1 # remove 1 from the length
            return value

        else:
            value = self.tail.get_value() # store the tail value with get_value method
            self.tail = self.tail.get_next() # set the tail as the next value with the get_next method
            self.length -= 1 # remove 1 from the length
            return value
            ''' option
            cur_node = self.head
            while cur_node.get_next() is not self.tail:
                cur_node = cur_node.get_next()
            cur_node.set_next(None)
            self.tail = current_node
            self.length -= 1
            return value
            '''

    def contains(self, value): # method to see if list contains value
        if self.head is None: # if empty
            return False

        cur = self.head # store the head as cur
        while cur is not None: # loop if cur value is None
            if cur.value == value: # if cur value = a value in list
                return True

            cur = cur.get_next() # set the cur value to the next value
        return False

    def get_max(self): # method to get the max value
        if self.head is None: # if empty
            return None

        cur = self.head # store the head as the cur value
        max = self.head.value # set the max value as the head
        while cur is not None: # loop if cur is not empty
            if cur.value > max: # if cur value is more than max
                max = cur.value # set max to the new cur value
            cur = cur.get_next() # set the cur value to the next value
        return max
