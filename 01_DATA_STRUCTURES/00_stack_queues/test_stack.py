# TEST STACK SCRIPT
# Santiago Garcia Arango, July 2020

import stack

# Create Stack object
s = stack.Stack("\nMY COOL ELECTRONICS STACK")

# Add elements to stack
s.push("Raspberry Pi 3")
s.push("Arduino")
s.push("Arduino")
s.push("LED red")
s.push("LED green")
s.push("LED yellow")
s.push("PIC18F2550")
s.push("Resistor")
s.push("Multimeter")
s.push("Capacitor")

# See complete stack (first check)
print("\nFIRST STACK CHECK:\n", s)

# Remove some elements of stack
s.pop()
s.pop()
s.pop()
s.pop()

# See complete stack (second check)
print("\nSECOND STACK CHECK:\n", s)

# See last stack item at this point
print("\nLAST STACK ITEM NOW:\n", s.look_last_item())

# Clear all stack
s.clear_stack()

# Check stack now
print("\nSTACK AFTER CLEAR METHOD:\n", s)

# Add elements again
s.push("Sensor HC-SR04")
s.push("Sensor IR")
s.push("Cables")
s.push("Freescale microcontroller")

# Check stack now
print("\nNEW STACK:\n", s)
