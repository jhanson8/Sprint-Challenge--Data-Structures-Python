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
#Implement using array 
'''class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = []


    def __len__(self):
        return len(self.storage)

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        if len(self.storage) >= 1:
            popped = self.storage.pop()
            return popped '''

#Implement using linked list

class Stack:
    class Node:

        def __init__(self, element, _next):
                self.element = element
                self._next = _next

    def __init__(self):
        self.head = None 
        self.size = 0 

    def __len__(self):
        return self.size
        
    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size = self.size + 1 

    def pop(self):
        if self.is_empty():
            return None
        value = self.head.element
        self.head = self.head._next
        self.size = self.size -1 
        return value 