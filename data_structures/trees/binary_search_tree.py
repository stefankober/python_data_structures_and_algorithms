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
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return True
        else:
            return self.recursive_insert(self.root, value)

    def recursive_insert(self, node, value):
        if value == node.value:
            return None
        if value < node.value and node.left == None:
            node.left = Node(value)
            return True
        elif  value < node.value and node.left != None:
            return self.recursive_insert(node.left, value)
        elif value > node.value and node.right == None:
            node.right = Node(value)
            return True
        elif  value > node.value and node.right != None:
            return self.recursive_insert(node.right, value)

    def contains(self, value, return_parent=False):
        if self.root == None:
            return False
        elif value == self.root.value and not return_parent:
            return True
        elif value == self.root.value and return_parent:
            return None
        else:
            return self.recursive_contains(value, self.root, return_parent=return_parent)

    def recursive_contains(self, value, node, return_parent):
        if not node.left and value < node.value:
            return False
        elif not node.right and value > node.value:
            return False
        elif node.left and value == node.left.value and not return_parent:
            return True
        elif node.right and value == node.right.value and not return_parent:
            return True
        elif node.left and value == node.left.value and return_parent:
            return node
        elif node.right and value == node.right.value and return_parent:
            return node
        elif value < node.value:
            return self.recursive_contains(value, node.left, return_parent=return_parent)
        elif value > node.value:
            return self.recursive_contains(value, node.right, return_parent=return_parent)
