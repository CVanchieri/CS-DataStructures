class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self): # get current value
        return self.value

    def get_next(self): # get next node method
        return self.next_node

    def set_next(self, new_next): # set next node method
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__ (self):
        self.head = None # unique to empty list, change if known
        self.tail = None # unique to empty list, change if known
        self.length = 0 # unique to empty list, change if known

    def add_to_head(self, value):
        new_node = Node(value, self.head) # new node attribute
        self.head = new_node # set the new node ad the head
        if self.length == 0: # or, if self.head is None and self.tail is None
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value) # new node attribute
        if self.head is None and self.tail is None:
            self.head = new_node

        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None

        elif self.head == self.tail: # if list is empty cant remove.
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        if self.tail is None:
            return None

        elif self.tail == self.head: # if list is empty cant remove.
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else:
            value = self.tail.get_value()
            self.tail = self.tail.get_next()
            self.length -= 1
            return value

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None

        cur_node = self.head
        cur_max = self.head.value
        while cur_node is not None:
            if cur_node.value > cur_max:
                cur_max = cur_node.value
            cur_node = cur_node.next_node
        return cur_max
