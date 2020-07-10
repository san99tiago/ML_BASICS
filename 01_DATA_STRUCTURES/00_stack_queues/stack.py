# STRUCTURE INFORMATION WITH A SIMPLE STACK METHOD
# Santiago Garcia Arango, July 2020

"""
Stacks are simple data-structures that work really well, when
we have a problem that involves adding or removing elements
but following the concept of LIFO(Last-In, First-Out).
This means that the operations affect always the "top-item"
that is currently on the stack.
We usually create methods to:
    PUSH  --> Add item on top of the stack.
    POP   --> Remove top item of the stack.
    CLEAR --> Delete all items on the stack.
    UNDO  --> Let us "go back" in the stack operations once.
"""


class Stack():
    """
    --------STACK CLASS HELP--------
    -->Parameters:
    :param name: string for the name of stack.\n
    -->Methods:
    :push(): add element on top of stack.
    :pop(): delete top element of stack.
    :look_last_item(): return last element of stack.
    :clear_stack(): delete all stack elements.
    :__str__(): return stack.
    """
    def __init__(self, name="No name"):
        self.stack = []
        self.name = name

    def push(self, item):
        """:param item: object or item to be added to stack."""
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            # ".pop()" is a Python method to remove last element of list.
            return self.stack.pop()
        else:
            return None

    def look_last_item(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def clear_stack(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)


# Check test in script < test_stack.py >
