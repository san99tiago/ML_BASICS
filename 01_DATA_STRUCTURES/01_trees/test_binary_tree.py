# SCRIPT TO TEST THE EXECUTION OF THE BINARY TREE
# Santiago Garcia Arango, July 2020

import binary_tree

t1 = binary_tree.BinaryTree(15)

t1.insert(8)

print("\nPREORDER:")
t1.preorder()

print("\nINORDER:")
t1.inorder()

t1.insert(24)
t1.insert(5)
t1.insert(11)

print("\nPREORDER:")
t1.preorder()

print("\nINORDER:")
t1.inorder()

t1.insert(2)
t1.insert(6)
t1.insert(13)

print("\nPREORDER:")
t1.preorder()

print("\nINORDER:")
t1.inorder()
