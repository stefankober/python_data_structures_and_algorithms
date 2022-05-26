class Node:
    
    """
    Node in a single linked list
    """
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    
    """
    Single linked list data structure as described in text file.
    Creates an empty linked list
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, value):
        if self.head == None and self.tail == None:
            self.head = Node(value, next=None)
            self.tail = self.head
            self.len += 1
        else:
            self.tail.next = Node(value, next=None)
            self.tail = self.tail.next
            self.len += 1

    def remove_last(self):
        assert not self.head == None, "Cannot remove last item from empty list"
        cursor = self.head.next
        for i in range(2, self.len):
            cursor = cursor.next
        self.tail = cursor
        self.tail.next = None
        self.len -= 1

    def prepend(self, value):
        self.head = Node(value, self.head.next)
        self.len += 1

    def remove_first(self):
        assert not self.head == None, "Cannot remove first item from empty list"
        self.head = self.head.next
        self.len -= 1

    def lookup_by_index()
