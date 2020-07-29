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
        if self.left: # if self.left
            self.left.for_each(fn) # use the fn function on self.left with the for_each method
        fn(self.value) # use the fn function on self.value
        if self.right: # if self.right
            self.right.for_each(fn) # use the fn function on self.right with the for_each method

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

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

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
