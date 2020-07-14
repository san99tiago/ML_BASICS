# SCRIPT TO TEST THE EXECUTION OF GENERAL TREE
# Santiago Garcia Arango

import general_tree

# Create main root
root = general_tree.TreeNode("UNIVERSITY EIA")

# Create nodes for the first children
management = general_tree.TreeNode("MANAGEMENT")
mechatronics = general_tree.TreeNode("MECHATRONICS")
mechanics = general_tree.TreeNode("MECHANICS")
biomedics = general_tree.TreeNode("BIOMEDICS")

#Create the second children from the first ones
management.add_child(general_tree.TreeNode("BUSSINESS"))
management.add_child(general_tree.TreeNode("ECONOMICS"))
management.add_child(general_tree.TreeNode("RISKS"))

mechatronics.add_child(general_tree.TreeNode("ROBOTICS"))
mechatronics.add_child(general_tree.TreeNode("CONTROL"))
mechatronics.add_child(general_tree.TreeNode("SIGNALS"))

mechanics.add_child(general_tree.TreeNode("THERMODYNAMICS"))
mechanics.add_child(general_tree.TreeNode("MECHANISMS"))
mechanics.add_child(general_tree.TreeNode("WELDING"))

biomedics.add_child(general_tree.TreeNode("HISTOLOGY"))
biomedics.add_child(general_tree.TreeNode("BIOMATERIALS"))
biomedics.add_child(general_tree.TreeNode("BIOLOGY"))


# Add first children children
root.add_child(management)
root.add_child(mechatronics)
root.add_child(mechanics)
root.add_child(biomedics)


root.print_tree()