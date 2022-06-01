class Node:
    
    """
    Node of a binary search tree
    exposes
    * key
    * left
    * right
    """
    def __init__(self, tup, left=None, right=None):
        self.key = tup[0]
        self.value = tup[1]
        self.left = left
        self.right = right

class BST:
    
    """
    Node implementation of a BST
    """
    def __init__(self):
        self.root = None
    
    def insert(self, tup_or_node):
        if type(tup_or_node) is not Node:
            node = Node(tup_or_node)
        else:
            node = key_or_node
        if self.root == None:
            self.root = node
            return True
        else:
            temp = self.root
            while True:
                if node.key == temp.key:
                    return False
                elif node.key < temp.key: 
                    if temp.left == None:
                        temp.left = node
                        return True
                    else: 
                        temp = temp.left
                elif node.key > temp.key:
                    if  temp.right == None:
                        temp.right = node
                        return True
                    else:
                        temp = temp.right

    def contains(self, key):
        if self.root == None:
            return False
        temp = self.root
        while temp != None:
            if temp.key == key:
                return True
            elif key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right
        return False

    def remove(self, key):
        if key == self.root.key:
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
                if key == temp.key:
                    if key < before.key:
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
                    elif key > before.key:
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
                elif key < temp.key:
                    before = temp
                    temp = temp.left
                elif key > temp.key:
                    before = temp
                    temp = temp.right
            return False

    def get(self, key):
        if self.root == None:
            return False
        temp = self.root
        while temp != None:
            if temp.key == key:
                return temp.value
            elif key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right
        return None
