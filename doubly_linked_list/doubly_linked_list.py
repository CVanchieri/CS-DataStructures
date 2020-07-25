"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
import gc

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.head = value
        self.prev = None
        self.next = self.head
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is not None:
            self.head = self.next
            self.prev = None

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.head is not None:
            self.tail = value
            self.prev = self.tail


    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 1:
            value = self.tail.value
            self.tail = None
            self.next = None
            self.length = 0
        if self.tail is not None:
            value = self.tail.value
            self.tail = self.tail.prev
            self.next = None
            self.length -= 1
        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node.prev is None:
            return
        if node.next is None:
            self.add_to_head(node)
            self.remove_from_tail()
        else:
            self.add_to_head(node)
            self.delete(node)


    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node.next is None:
            return
        if node.prev is None:
            self.add_to_tail(node.value)
            self.remove_from_head()
        else:
            self.add_to_tail(node.value)
            self.delete(node)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):

        #cur_node = self.head # only needed if its a value not a node
        #while cur_node != node: # only needed if its a value not a node
        #    cur_node = curnode.get_next

        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
        self.length -= 1

    def delete(self):
        if self.length == 0:
            self.tail = None
            self.head = None
            self.length = 0
            return

        if self.head == node:
            self.head = node.next_node
        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next
        slef.length -= 1
        gc.collet()


    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        max = 0
        node = self.head
        while node is not None:
            if node.value > max:
                max = node.get_value
            node = node.next

        return max
