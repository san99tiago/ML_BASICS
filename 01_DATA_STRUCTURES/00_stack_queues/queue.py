# QUEUES DATA STRUCTURES
# Santiago Garcia Arango, July 2020

"""
Queues are simple data-structures that work really well, when
we have a problem that involves adding or removing elements
but following the concept of FIFO(First-In, First-Out).
This structure is commonly understood with supermarket items,
restaurant orders, customer services, etc...
We usually create methods to:
    ENQUEUE  --> Add item to the "end" of the queue.
    DEQUEUE  --> Remove item from the "front" of the queue.
    CLEAR --> Delete all items on the queue.
"""


class Queue():
    """
    --------QUEUE CLASS HELP--------
    -->Parameters:
    :param name: string for the name of queue.\n
    -->Methods:
    :enqueue(): add element on back of queue.
    :dequeue(): remove element on front of queue.
    :look_front_item(): return front element of queue.
    :clear(): delete all queue elements.
    :__str__(): return queue.
    """
    def __init__(self, name="No name"):
        self.queue = []
        self.name = name

    def enqueue(self, item):
        """:param item: object or item to be added to queue."""
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            item_0 = self.queue[0]
            del self.queue[0]
            return item_0
        else:
            return None

    def look_front_item(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def clear(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

# Check tests in < test_queue.py > script
