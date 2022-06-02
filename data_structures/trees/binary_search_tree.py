class Node:
    
    """
    Node of a binary search tree
    exposes
    * value
    * left
    * right
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    
    """
    Node implementation of a BST
    """
    def __init__(self):
        self.root = None
    
    def insert(self, value_or_node):
        if type(value_or_node) is not Node:
            node = Node(value_or_node)
        else:
            node = value_or_node
        if self.root == None:
            self.root = node
            return True
        else:
            temp = self.root
            while True:
                if node.value == temp.value:
                    return False
                elif node.value < temp.value: 
                    if temp.left == None:
                        temp.left = node
                        return True
                    else: 
                        temp = temp.left
                elif node.value > temp.value:
                    if  temp.right == None:
                        temp.right = node
                        return True
                    else:
                        temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp != None:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return False

    def remove(self, value):
        if value == self.root.value:
            if self.root.right == None and self.root.left == None:
                self.root = None
                return True
            if self.root.right != None and self.root.left == None:
                self.root = self.root.right
                return True
            if self.root.right == None and self.root.left != None:
                self.root = self.root.left
                return True
            else:
                temp = self.root.left
                self.root = self.root.right
                self.insert(temp)
                return True
        else:
            temp = self.root
            before = None
            while temp != None:
                if value == temp.value:
                    if value < before.value:
                        if temp.left == None and temp.right == None:
                            before.left = None
                            return True
                        elif  temp.left == None and temp.right != None:
                            before.left = temp.right
                            return True
                        elif temp.left != None and temp.right == None:
                            before.left = temp.left
                            return True
                        else:
                            before.left = temp.right
                            self.insert(temp.left)
                            return True
                    elif value > before.value:
                        if temp.left == None and temp.right == None:
                            before.right = None
                            return True
                        elif  temp.left == None and temp.right != None:
                            before.right = temp.right
                            return True
                        elif temp.right != None and temp.right == None:
                            before.left = temp.left
                            return True
                        else:
                            before.right = temp.right
                            self.insert(temp.left)
                            return True
                elif value < temp.value:
                    before = temp
                    temp = temp.left
                elif value > temp.value:
                    before = temp
                    temp = temp.right
            return False

