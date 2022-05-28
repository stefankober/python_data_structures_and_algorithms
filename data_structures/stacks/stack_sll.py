class Node:

    """
    Node for singly linked list:
    - value 
    - next
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    
    """
    SLL implementation of a stack
    """
    def __init__(self):
        self.top = None
        self.len = 0
    
    def push(self, value):
        if len == 0:
            self.top = Node(value)
        else:
            self.top = Node(value, self.top)
        self.len += 1

    def pop(self):
        if self.len == 0:
            return None
        elif self.len == 1:
            value = self.top.value
            self.head = None
        else:
            value = self.top.value
            self.top = self.top.next
        self.len -=1
        return value
