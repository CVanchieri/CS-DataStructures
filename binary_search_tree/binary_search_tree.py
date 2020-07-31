"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue

class BSTNode: # BSTNode class
    def __init__(self, value): # initializer constructor method
        self.value = value # set value to the value
        self.left = None # set the left to None
        self.right = None # set the right to None

    # Insert the given value into the tree
    def insert(self, value): # method to insert value
        if self.value <= value: # if self.value is <= the new value
            if self.right is None: # if self.right is None
                self.right = BSTNode(value) # set self.right to the new value with the BSTNode class
            else:
                self = self.right # set self to self.right
                self.insert(value) # instert the new value with the instert method
        else:
            if self.left is None: # if self.left is None
                self.left = BSTNode(value) # set self.left to the new value with the BSTNode class
            else:
                self = self.left # set the self to self.left
                self.insert(value) # inser the new value with the insert method

    # Return True if the tree contains the value, False if it does not
    def contains(self, target): # method to see i the value is in the tree
        if target < self.value: # if the target is less than the self.value
            if self.left is None: # if self.left is None
                return False
            return self.left.contains(target) # return self.left target value with the contains method
        elif target > self.value: # else if the target is great than the self.value
            if self.right is None: # if the self.right is None
                return False
            return self.right.contains(target) # return self.right target value with the contains method
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self): # method to get the max value
        while self.right: # while loop through self.right
            self = self.right # set self to self.right
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn): # method to call a function on each value
        if self.left: # if self.left, or if self.left is None:
            self.left.for_each(fn) # use the fn function on self.left with the for_each method
        fn(self.value) # use the fn function on self.value
        if self.right: # if self.right
            self.right.for_each(fn) # use the fn function on self.right with the for_each method

    # Delete a value from the tree
    def delete(self): # method to delete a value
        # search like we did in contains() method
        # different cases
        # if node at bottom level
            # update parent lef or right to = None
        # if node has only one child
            # udate parent.left or right to = node.left or right
        # if node has 2 children
            # 'larger' child becomes the parent of its sibling
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    ''' not working yet '''
    def in_order_print(self): # method to print tree in value order
        if self: # if self is not None
            if self.left: # if self.left is not None
                # make left child root of tree
                self.left.in_order_print() # set self.left with in_order_print method
            print(self.value)
            # if there is a right child
            if self.right: # if self.right is not None
                return self.right.in_order_print() # set self.right with in_order_print method
            print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self): # method to print iterative breadth first traversal approach
        q = Queue() # set the Queue
        q.enqueue(self) # insert the value
        while q.size > 0: # while loop if length is > 0
            front = q.dequeue() # remove from top
            print(front.value)

            if front.left: # if self.left is not None
                # add left child to queue
                q.enqueue(front.left) # insert value to queue

            if front.right: # if self.right is not None
                q.enqueue(front.right) # insert value to queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self): # method to print iterative depth first traversal approach
        if self: # if self is not None
            print(self.value)

        if self.left: # if self.left is not None
            self.left.dft_print() # set self.left with dft_print method

        if self.right:# if self.right is not None
            self.right.dft_print() # set self.left with dft_print method

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
print("in_order_print")
bst.in_order_print()
print("bft_print:")
bst.bft_print()
print("dft_print")
bst.dft_print()
