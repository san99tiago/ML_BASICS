# SCRIPT TO TEST THE EXECUTION OF GENERAL TREE
# Santiago Garcia Arango

import general_tree

# ----------------------------CREATE NODES--------------------------------
# Create main root (LEVEL 0)
root = general_tree.TreeNode("UNIVERSITY EIA")

# Create nodes (LEVEL 1)
a1 = general_tree.TreeNode("MECHATRONICS")
b1 = general_tree.TreeNode("MANAGEMENT")
c1 = general_tree.TreeNode("MECHANICS")
d1 = general_tree.TreeNode("BIOMEDICS")

# Create nodes (LEVEL 2)
a11 = general_tree.TreeNode("ROBOTICS")
a12 = general_tree.TreeNode("CONTROL")
a13 = general_tree.TreeNode("ELECTRONICS")

b11 = general_tree.TreeNode("BUSSINESS")
b12 = general_tree.TreeNode("ECONOMICS")
b13 = general_tree.TreeNode("RISKS")

c11 = general_tree.TreeNode("THERMODYNAMICS")
c12 = general_tree.TreeNode("MECHANISMS")
c13 = general_tree.TreeNode("WELDING")

d11 = general_tree.TreeNode("BIOSIGNALS")
d12 = general_tree.TreeNode("BIOMATERIALS")
d13 = general_tree.TreeNode("ANATOMY")

# Create nodes (LEVEL 3) ... only a few
a111 = general_tree.TreeNode("prof: Juan Camilo Tejada")
a112 = general_tree.TreeNode("prof: Gustavo Moreno")

a121 = general_tree.TreeNode("prof: Dolly Tatiana")
a122 = general_tree.TreeNode("prof: Sebastian Jimenez")

a131 = general_tree.TreeNode("prof: Yeison Javier Montagut")
a132 = general_tree.TreeNode("prof: Camilo Buritica")
a133 = general_tree.TreeNode("prof: Dario Jaramillo")

b121 = general_tree.TreeNode("prof: Elmer Algo")
b122 = general_tree.TreeNode("prof: Robert Ng")

c131 = general_tree.TreeNode("prof: Elizabeth Hoyos")
c132 = general_tree.TreeNode("prof: Luis V. Wilches")

# ------------------------ADD NODES RELATIONSHIPS-------------------------
# Add children (LEVEL 2-->3)
a11.add_child(a111)
a11.add_child(a112)

a12.add_child(a121)
a12.add_child(a122)

a13.add_child(a131)
a13.add_child(a132)
a13.add_child(a133)

b12.add_child(b121)
b12.add_child(b122)

c13.add_child(c131)
c13.add_child(c132)


# Add children (LEVEL 1-->2)
a1.add_child(a11)
a1.add_child(a12)
a1.add_child(a13)

b1.add_child(b11)
b1.add_child(b12)
b1.add_child(b13)

c1.add_child(c11)
c1.add_child(c12)
c1.add_child(c13)

d1.add_child(d11)
d1.add_child(d12)
d1.add_child(d13)

# Add children (LEVEL 0-->1)
root.add_child(a1)
root.add_child(b1)
root.add_child(c1)
root.add_child(d1)


# ---------------------PRINTING TREE BY LEVELS-----------------------------
print("\n---------TREE LEVEL 0:-----------")
root.print_tree(0)
print("\n---------TREE LEVEL 1:-----------")
root.print_tree(1)
print("\n---------TREE LEVEL 2:-----------")
root.print_tree(2)
print("\n---------TREE LEVEL 3:-----------")
root.print_tree(3)