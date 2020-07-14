# GENERAL TREE STRUCTURE SETUP
# Santiago Garcia Arango, July 2020


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

    def print_tree(self):
        # Access the information of this specific TreeNode
        print(self.data)

        if len(self.children) > 0:
            # For each child, do a recursive approach of <print_tree> method
            for c in self.children:
                c.print_tree()
                
# Tests are in < test_general_tree.py >
