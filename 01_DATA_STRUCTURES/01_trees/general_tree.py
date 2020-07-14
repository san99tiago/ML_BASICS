# GENERAL TREE STRUCTURE SETUP
# Santiago Garcia Arango, July 2020
"""
The goal is to create a tree structure to organize better the information.
The final result should be able to create a tree and print it like this:
(from the "root", be able to go deep in a tree structure)

UNIVERITY (level 0)
    |__MANAGEMENT (level 1)
    |   |__BUSSINESS (level 2)
    |   |__ECONOMICS
    |   |__RISKS
    |__MECHATRONICS
    |   |__ROBOTICS
    |   |__CONTROL
    |   |__ELECTRONICS
    |__MECHANICS
    |   |__THERMODYNAMICS
    |   |__MECHANISMS
    |   |__WELDING
    |__BIOMEDICS
    |   |__SIGNALS
    |   |__BIOMATERIALS
    |   |__BIOLOGY
"""

class TreeNode:
    """
    --------TREENODE HELP--------
    This is the general node for building any tree general structure.
    :param data: any information, data or object to be stored.
    """
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        # Before adding the "child" to the tree, we give it the instance...
        # ... of the main parent (which is the upper TreeNode class)
        child.parent = self
        self.children.append(child)

    def get_level(self):
        # The idea of this method is to be able to se de "depth" of this...
        # ... specific node in the tree, to use it the print_tree() method
        level = 0
        current_parent = self.parent
        while current_parent != None:
            # Add levels by recursive accessing each parent (until None)
            level += 1
            current_parent = current_parent.parent
        return level

    def print_tree(self, levels_to_show=5):
        # Extra printing setup for organizing visual tree
        setup = "    |" * self.get_level() + "__"

        # Access the information of this specific TreeNode
        print(setup + self.data)

        if len(self.children) > 0:
            # For each child, do a recursive approach of <print_tree> method
            for c in self.children:
                # Extra condition to only show levels given by the user
                if self.get_level() < levels_to_show:
                    c.print_tree(levels_to_show)

# Tests are in < test_general_tree.py >
