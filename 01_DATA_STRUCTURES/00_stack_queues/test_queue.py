# TEST QUEUE SCRIPT
# Santiago Garcia Arango, July 2020

import queue

# Create queue object
q = queue.Queue("\nMY COOL MOVIES queue")

# Add elements to queue
q.enqueue("The godfather")
q.enqueue("The scent of a woman")
q.enqueue("The handmaiden")
q.enqueue("Chapie")
q.enqueue("Harry Potter")
q.enqueue("Batman")
q.enqueue("Inception")
q.enqueue("El hoyo")
q.enqueue("Lord of the rings")
q.enqueue("Beautiful mind")

# See complete queue (first check)
print("\nFIRST QUEUE CHECK:\n", q)

# Remove some elements of queue
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

# See complete queue (second check)
print("\nSECOND QUEUE CHECK:\n", q)

# See front item of queue at this point
print("\FRONT QUEUE ITEM NOW:\n", q.look_front_item())

# Clear all queue
q.clear()

# Check queue now
print("\nQUEUE AFTER CLEAR METHOD:\n", q)

# Add elements again
q.enqueue("The hobbit")
q.enqueue("Fast and furious")
q.enqueue("Titanic")
q.enqueue("The imitation game")

# Check queue now
print("\nNEW QUEUE:\n", q)
