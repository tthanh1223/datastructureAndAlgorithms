from ADT_abstract_data_type.linked_list.node import DoubleNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Reference to the first node
        self.tail = None  # Reference to the last node
        self.node_count = 0  # Count of nodes in the list

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def add(self, item):
        """Add an item to the front of the list."""
        new_node = DoubleNode(item)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
        self.node_count += 1

    def append(self, item):
        """Append an item to the end of the list."""
        new_node = DoubleNode(item)
        if self.tail is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node
        self.node_count += 1

    def remove(self, item):
        """Remove the first occurrence of an item in the list."""
        current = self.head
        while current is not None:
            if current.get_data() == item:
                if current.get_prev() is not None:  # Not the head
                    current.get_prev().set_next(current.get_next())
                else:  # Current is the head
                    self.head = current.get_next()

                if current.get_next() is not None:  # Not the tail
                    current.get_next().set_prev(current.get_prev())
                else:  # Current is the tail
                    self.tail = current.get_prev()

                self.node_count -= 1
                return
            current = current.get_next()

    def __str__(self):
        """Return a string representation of the list."""
        items = []
        current = self.head
        while current is not None:
            items.append(current.get_data())
            current = current.get_next()
        return "Lists: " + " -> ".join(map(str, items))

    def size(self):
        """Return the number of nodes in the list."""
        return self.node_count

    def search(self, item):
        """Search for an item in the list."""
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def pop(self, position=None):
        """Remove and return the item at the specified position."""
        if position is None:
            position = self.size() - 1  # Default to remove the last item
        if position < 0 or position >= self.size():
            raise ValueError("Index out of range")

        current = self.head
        index = 0
        while index < position:
            current = current.get_next()
            index += 1

        if current.get_prev() is not None:
            current.get_prev().set_next(current.get_next())
        else:
            self.head = current.get_next()

        if current.get_next() is not None:
            current.get_next().set_prev(current.get_prev())
        else:
            self.tail = current.get_prev()

        self.node_count -= 1
        return current.get_data()

    def reverse(self):
        """Reverse the linked list in place."""
        current = self.head
        temp = None
        self.tail = self.head  # Update tail to the current head
        while current is not None:
            temp = current.get_prev()
            current.set_prev(current.get_next())
            current.set_next(temp)
            current = current.get_prev()  # Move to the next node (previously next)
        if temp is not None:
            self.head = temp.get_prev()  # Update head

    def __iter__(self):
        """Return an iterator for the linked list."""
        current = self.head
        while current is not None:
            yield current.get_data()
            current = current.get_next()
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add(10)
    dll.add(20)
    dll.append(30)
    dll.append(40)
    print("Doubly Linked List:", dll)  # Output: [20, 10, 30, 40]

    dll.remove(10)
    print("After removing 10:", dll)  # Output: [20, 30, 40]

    print("List size:", dll.size())  # Output: 3

    dll.pop(1)  # Remove the second element
    print("After popping index 1:", dll)  # Output: [20, 40]

    dll.reverse()
    print("Reversed list:", dll)  # Output: [40, 20]
