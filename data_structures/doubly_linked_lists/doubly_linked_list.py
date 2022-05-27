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

    def remove_last(self):
        assert self.len != 0, "Cannot remove last from empty list"
        if self.len == 1:
            value = self.head.value
            self.head = None
            self.tail = self.head
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
        self.len -= 1
        return value
    
    def prepend(self, value):
        if self.len == 0:
            return self.append(value)
        else:
            self.head = Node(value, None, self.head)
            self.head.next.prev = self.head
        self.len += 1
        return True
    
    def remove_first(self):
        assert self.len != 0, "Cannot remove first from empty list"
        if self.len == 1:
            return self.remove_last()
        else:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None
        self.len -= 1
        return value
    
    def set_by_index(self, index, value):
        assert 0 <= index < self.len, "Index out of bounds"
        middle = int(self.len/2)
        if index <= middle:
            cursor = self.head
            for i in range(index):
                cursor = cursor.next
            cursor.value = value
        else:
            cursor = self.tail
            for i in range(self.len-index-1):
                cursor = cursor.prev
            cursor.value = value
        return True
    
    def get_by_index(self, index):
        assert 0 <= index < self.len, "Index out of bounds"
        middle = int(self.len/2)
        if index <= middle:
            cursor = self.head
            for i in range(index):
                cursor = cursor.next
            value = cursor.value
        else:
            cursor = self.tail
            for i in range(self.len-index-1):
                cursor = cursor.prev
            value = cursor.value
        return value       
    
    def insert_after_index(self, index, value):
        assert 0 <= index < self.len, "Index out of bounds"
        if self.len == 0:
            return self.append(value)
        middle = int(self.len/2)
        if index <= middle:
            cursor = self.head
            for i in range(index):
                cursor = cursor.next
            cursor.next = Node(value, cursor, cursor.next)
            cursor.next.next.prev = cursor.next
        else:
            cursor = self.tail
            for i in range(self.len-index-1):
                cursor = cursor.prev
            cursor.next = Node(value, cursor, cursor.next)
            cursor.next.next.prev = cursor.next
        self.len += 1
        return True      
    
    def remove_index(self, index):
        assert 0 <= index < self.len, "Index out of bounds"
        assert self.len != 0, "Cannot remove index from empty list"
        if index == self.len-1:
            return self.remove_last()
        if index == 0:
            return self.remove_first()
        middle = int(self.len/2)
        if index <= middle:
            cursor = self.head
            for i in range(index):
                cursor = cursor.next
            value = cursor.value
            cursor.prev.next = cursor.next
            cursor.next.prev = cursor.prev
        else:
            cursor = self.tail
            for i in range(self.len-index-1):
                cursor = cursor.prev
            value = cursor.value
            cursor.prev.next = cursor.next
            cursor.next.prev = cursor.prev
        self.len -= 1
        return value

    def __repr__(self):
        strg = ""
        cursor = self.head
        for i in range(self.len):
            strg = strg + str(cursor.value) + "->"
            cursor = cursor.next
        return strg
