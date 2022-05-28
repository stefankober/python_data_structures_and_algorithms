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
    def __init__(self, head=None, tail=None):
        self.len = 0
        self.head = head
        self.tail = tail

    def enqueue(self, value):
        if self.len == 0:
            self.tail = Node(value)
            self.head = self.tail
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.len += 1
        return True

    def dequeue(self):
        if self.len == 0:
            return None
        if self.len == 1:
            value = self.head.value
            self.head = None
            self.tail = self.head
        else:
            value = self.head.value
            self.head = self.head.next
        self.len -= 1
        return value
