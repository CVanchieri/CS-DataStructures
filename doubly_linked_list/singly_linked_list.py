# node class
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value # the value at this linked list node
        self.next_node = next_node # reference to the next node in the list

    def get_value(self): # get current value method
        return self.value

    def get_next(self): # get next node method
        return self.next_node

    def set_next(self, new_next): # set next node method
        self.next_node = new_next

# LinkedList class
class LinkedList:
    def __init__ (self): # initialize constructor
        self.head = None
        self.tail = None
        self.length = 0

    def get_length(self): # get current value method
        return self.length

    def add_to_head(self, value): # add value to the head
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value): # add value to the tail
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node #
        self.length += 1

    def remove_head(self): # remove the head value
        if self.head is None:
            return None

        elif self.head == self.tail:
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

    def remove_tail(self): # remove the tail value
        if self.tail is None:
            return None

        elif self.tail == self.head:
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
            ''' option, while loop is not good runtime
            cur_node = self.head
            while cur_node.get_next() is not self.tail:
                cur_node = cur_node.get_next()
            cur_node.set_next(None)
            self.tail = current_node
            self.length -= 1
            return value
            '''

    def contains(self, value): # does the list contain value
        if self.head is None:
            return False

        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.get_next()
        return False

    def get_max(self): # get max value
        if self.head is None:
            return None

        cur_node = self.head
        cur_max = self.head.value
        while cur_node is not None:
            if cur_node.value > cur_max:
                cur_max = cur_node.value
            cur_node = cur_node.get_next()
        return cur_max

    def get_Middle(self): # get middle value method # big (O)n run time
        mid = self.head
        end = self.head
        if self.head is not None:
            while (end is not None and end.get_next() is not None):
                end = end.get_next().get_next()
                mid = mid.get_next()
            print("The middle element is: ", mid.value)

    def get_Middle2(self):
        temp = self.head
        count = 0
        while self.head:
            if (count & 1): # only update when count is odd
                temp = temp.get_next()
            self.head = self.head.get_next()
            count += 1 # increment count in each iteration
        print(temp.data)

ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
print(ll.get_Middle())
