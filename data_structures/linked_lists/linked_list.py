class Node:
    
    """
    Node in a single linked list
    """
    def __init__(self, value, next):
        self.value = value
        self.next = next
    def __repr__(self):
        return str(self.value)
        
class LinkedList:
    
    """
    Single linked list data structure as described in text file.
    Creates an empty linked list
    """
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.len = 0

    def append(self, value):
        if self.len == 0:
            self.head = Node(value, next=None)
            self.tail = self.head
            self.len += 1
        else:
            self.tail.next = Node(value, next=None)
            self.tail = self.tail.next
            self.len += 1
        return True

    def remove_last(self):
        assert not self.len == 0, "Cannot remove last item from empty list"
        value = self.tail.value
        if self.len == 1:
            self.head = None
            self.tail = self.head
        elif self.len == 2:
            self.tail = self.head
            self.head.next = None
        else:
            cursor = self.head.next
            while cursor.next.next is not None:
                cursor = cursor.next
            self.tail = cursor
            self.tail.next = None
        self.len -= 1
        return value

    def prepend(self, value):
        self.head = Node(value, self.head)
        self.len += 1

    def remove_first(self):
        assert not self.len == 0, "Cannot remove first item from empty list"
        value = self.head.value
        self.head = self.head.next
        self.len -= 1
        if self.len == 0:
            self.tail = self.head
        return value
        
    def remove_by_index(self, index):
        assert self.len > index >= 0, "Index out of bounds" # indexing starts at 0
        if index == 0:
            return self.remove_first()
        elif index == self.len-1:
            return self.remove_last()
        else:
            i = 0
            cursor = self.head
            while i != index-1:
                cursor = cursor.next
                i += 1
            value = cursor.next.value
            cursor.next = cursor.next.next
            self.len -= 1
            return value
        
    def remove_by_value(self, value):
        index = self.lookup_by_value(value)
        if index >= 0:
            self.remove_by_index(index)
            return True
        else:
            return False
        
    def lookup_by_index(self, index):
        assert self.len > index >= 0, "Index out of bounds" # indexing starts at 0
        cursor = self.head
        for _ in range(-1, index-1):
            cursor = cursor.next
        return (cursor.value)

    def lookup_by_value(self, value):
        cursor = self.head
        for i in range(self.len):
            if value == cursor.value:
                return i
            cursor = cursor.next
        return -1
    
    def set_by_index(self, index, value):
        assert self.len > index >= 0, "Index out of bounds" # indexing starts at 0
        cursor = self.head
        for _ in range(index):
            cursor = cursor.next
        cursor.value = value
        return True
    
    def insert_after(self, index, value):
        assert self.len > index >= 0, "Index out of bounds" # indexing starts at 0
        if index == self.len-1:
            return self.append(value)
        else:
            cursor = self.head
            for _ in range(index):
                cursor = cursor.next
            cursor.next = Node(value, cursor.next)
            self.len += 1
            return True
    
    def reverse(self):
        self.head, self.tail = self.tail, self.head
        cursor = self.tail
        after = cursor.next
        before = None
        cursor.next = before
        while cursor != self.head:
            before, cursor, after = cursor, after, after.next
            cursor.next = before
        
    def __repr__(self):
        strg = ""
        cursor = self.head
        for i in range(self.len):
            strg = strg + str(cursor.value) + "->"
            cursor = cursor.next
        return strg
