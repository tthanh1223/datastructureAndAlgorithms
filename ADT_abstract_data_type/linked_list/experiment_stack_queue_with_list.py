import time
import random
from node import Node
from unordered_list import UnorderedList  # Ensure your UnorderedList class is in this module

# Define the number of elements for testing
NUM_ELEMENTS = 1000
ITERATIONS = 100  # Number of iterations for averaging

# Stack using a Python list
class StackWithList:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

# Queue using Python list
class QueueWithList:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front

    def is_empty(self):
        return len(self.items) == 0

# Experiment to compare performance
def performance_experiment():
    # Measure Stack Performance
    stack_list = StackWithList()
    stack_linked = UnorderedList()

    start_time = time.time()
    for i in range(NUM_ELEMENTS):
        stack_list.push(i)
    list_push_time = time.time() - start_time

    start_time = time.time()
    for i in range(NUM_ELEMENTS):
        stack_linked.append(i)  # Use appending as your stack's push
    linked_push_time = time.time() - start_time

    start_time = time.time()
    for _ in range(NUM_ELEMENTS):
        stack_list.pop()
    list_pop_time = time.time() - start_time

    start_time = time.time()
    for _ in range(NUM_ELEMENTS):
        stack_linked.pop()  # Implement pop method in UnorderedList
    linked_pop_time = time.time() - start_time

    print(f"Stack Performance:")
    print(f"Python List Push: {list_push_time:.5f} seconds")
    print(f"Linked List Push: {linked_push_time:.5f} seconds")
    print(f"Python List Pop: {list_pop_time:.5f} seconds")
    print(f"Linked List Pop: {linked_pop_time:.5f} seconds")

    # Measure Queue Performance
    queue_list = QueueWithList()
    queue_linked = UnorderedList()

    start_time = time.time()
    for i in range(NUM_ELEMENTS):
        queue_list.enqueue(i)
    list_enqueue_time = time.time() - start_time

    start_time = time.time()
    for i in range(NUM_ELEMENTS):
        queue_linked.append(i)  # Use append as your queue's enqueue
    linked_enqueue_time = time.time() - start_time

    start_time = time.time()
    for _ in range(NUM_ELEMENTS):
        queue_list.dequeue()
    list_dequeue_time = time.time() - start_time

    start_time = time.time()
    for _ in range(NUM_ELEMENTS):
        queue_linked.pop(0)  # Remove from the front for the linked list queue
    linked_dequeue_time = time.time() - start_time

    print(f"\nQueue Performance:")
    print(f"Python List Enqueue: {list_enqueue_time:.5f} seconds")
    print(f"Linked List Enqueue: {linked_enqueue_time:.5f} seconds")
    print(f"Python List Dequeue: {list_dequeue_time:.5f} seconds")
    print(f"Linked List Dequeue: {linked_dequeue_time:.5f} seconds")

if __name__ == "__main__":
    performance_experiment()
