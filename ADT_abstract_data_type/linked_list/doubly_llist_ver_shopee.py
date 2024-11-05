class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_head(self, data):
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def add_tail(self, data):
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def delete_head(self):
        if self.head is None: return
        elif self.head.next is None:
            self.head = None
            self.size -= 1
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

    def delete_tail(self):
        if self.head is None: return
        elif self.head.prev is None:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

    def delete_tail_without_tail(self):
        if self.head is None: return
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = None
            self.tail = cur
            self.size -= 1

if __name__ == '__main__':
    l1 = DoublyLinkedList()
    l1.add_head(1)
    l1.add_head(2)
    l1.add_head(3)
    l1.add_tail(4)
    l1.display()
