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
        self.head = None
        self.len = 0
    
    def push(self, value):
        if len == 0:
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.len += 1

    def pop(self):
        if self.len == 0:
            return None
        elif self.len == 1:
            value = self.head.value
            self.head = None
        else:
            value = self.head.value
            selfhead = self.head.next
        self.len -=1
        return value
