class Node:

    """
    Node for doubly linked list exposing
    - value
    - next
    - prev
    """
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    
    """
    Doubly linked list with all standard operations 
    """
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.len = 0

    def append(self, value):
        if self.len == 0:        
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.tail = Node(value, self.tail, None)
            self.tail.prev.next = self.tail
        self.len +=1
        return True

    def __repr__(self):
        strg = ""
        cursor = self.head
        for i in range(self.len):
            strg = strg + str(cursor.value) + "->"
            cursor = cursor.next
        return strg
