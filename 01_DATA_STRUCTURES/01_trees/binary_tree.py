# INTRODUCTION TO BINARY SEARCH TREE STRUCTURE
# Santiago Garcia Arango, July 2020
# This script is based on an online lecture given by:
# Joe James (Python Data Structures Tutorial --> Youtube: "Learn {to} Code")

"""
Trees are one of the most important structures in computational world.
They give us the advantage of great speed, performance and even a new
way of solving problems with easier solutions.

In this script, we will program a simple binary search tree.
BINARY SEARCH TREE:
1) Each node is greater than every node in its left subtree.
2) Each node is less than every node in its right subtree.

Example:
                15
                |
        ---------------
        8              24
        |               |
    ---------       ---------
    5      11       19      28
    |       |                |
--------    -----            -----
2       6       13              25
"""

class Tree:
    def __init__(self, data, left=None, right=None):
        """"
        -------TREE STRUCTURE HELP------
        -->Methods...
        insert(data): add data to the tree, based on BST structure.
        find(data): find data in the tree, else return False.
        get_size(): return size of BST based on standards.
        preorder(): return tree in <preorder()> convention.
        inorder(): return tree sorted from low to high values.
        """
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        """insert new <node> to the tree"""
        if self.data == data:
            return False  # Duplicate value given
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True

    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1
    def preorder(self):
        if self is not None:
            print (self.data, end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print (self.data, end=' ')
            if self.right is not None:
                self.right.inorder()
