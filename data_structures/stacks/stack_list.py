class Stack:

    """
    List implementation of a stack
    """
    def __init__(self):
        self.lst = []

    def height(self):
        return len(self.lst)

    def push(self, value):
        self.lst.append(value)

    def pop(self):
        return self.lst.pop()
