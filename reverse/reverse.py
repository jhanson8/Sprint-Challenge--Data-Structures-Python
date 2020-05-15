class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #if head doesn't exist 
        if not self.head:
            return None
        #otherwise set it to the current node "node"
        node = self.head 
        while(node is not None): 
            #sets next pointer to one head of cur head 
            next = node.next_node
            #sets pointer to previous which is in other direction 
            node.next_node = prev 
            #moves pointer down list until node is not pointing to anything number 
            prev = node 
            node = next
        #sets head to what was previously the tail before loop iterations 
        self.head = prev 
