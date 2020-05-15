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
from doubly_linked_list import DoublyLinkedList as dll
from stack import Stack as stack 

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            elif value >= self.value:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
            else:
                self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: 
            return True 
        if target < self.value:
            #go left if left is a BST node 
            if not self.left:
                return False 
            return self.left.contains(target)
        else:
            #go right if right is a BTS node
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #if there is a right node, return it 
        if self.right:
            return self.right.get_max()
        else:
            #return node value 
            return self.value 


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        q = dll()
        q.add_to_head(node)
        while q.length > 0:
            removed_node = q.remove_from_head()
            print(f"{removed_node.value}")
            if removed_node.left is not None:
                q.add_to_tail(removed_node.left)
            if removed_node.right is not None:
                q.add_to_tail(removed_node.right)
    

        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
            return
        s = stack()
        s.push(node)
        while s.is_empty() is False:
            print(s.head.element.value)
            popped_node = s.pop()
            if popped_node.left is not None:
                s.push(popped_node.left)
            if popped_node.right is not None:
                s.push(popped_node.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
         if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
            
