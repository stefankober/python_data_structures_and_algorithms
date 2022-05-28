class Node:
    
    """
    Node for queue
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:

    """
    Queue sll style
    """
    def __init__(self, first=None, last=None):
        self.len = 0
        self.first = first
        self.last = last

    def enqueue(self, value):
        if self.len == 0:
            self.last = Node(value)
            self.first = self.last
        else:
            self.last.next = Node(value)
            self.last = self.last.next
        self.len += 1
        return True

    def dequeue(self):
        if self.len == 0:
            return None
        if self.len == 1:
            value = self.first.value
            self.first = None
            self.last = self.first
        else:
            value = self.first.value
            self.first = self.first.next
        self.len -= 1
        return value
