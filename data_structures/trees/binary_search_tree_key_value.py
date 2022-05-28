class Node:
    
    """
    Node of a binary search tree where the values are keys for other values
    exposes
    * key
    * value
    * left
    * right
    """
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    
