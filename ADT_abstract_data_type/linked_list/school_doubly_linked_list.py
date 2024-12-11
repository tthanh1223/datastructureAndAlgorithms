from asyncio import current_task


class DNode:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Node({self.data})" if self.data else "None"

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        cur = self.head
        result = []
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        return " <-> ".join(result) + " -> None" if result else "None"

    def add_head(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1


    def add_tail(self, data):
        if self.head is None:
            self.add_head(data)
        else:
            new_node = DNode(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1

    def remove_head(self):
        if self.head is None:
            return
        elif self.size == 1:
            self.head = self.head.next
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def remove_tail(self):
        if self.tail is None:
            return
        elif self.size == 1:
            self.tail = self.tail.prev
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def remove_all(self):
        self.__init__()

    def find_node(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def remove_before(self, val):
        cur = self.head
        while cur and cur.next:
            if cur.next.data == val:
                # if the node before the val is head
                if cur.prev is None:
                    self.head = cur.next
                    self.head.prev = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                return
            cur = cur.next

    def remove_after(self, val):
        cur = self.head
        while cur:
            if cur.data == val:
                # the node after the val is tail
                if cur.next is None:
                    return
                elif cur.next.next is None:
                    self.tail = cur
                    cur.next = None
                else:
                    cur.next = cur.next.next
                return
            cur = cur.next

    def add_pos(self, data, pos):
        if pos == 0:
            self.add_head(data)
            return
        cur = self.head
        c_pos = 0
        while cur is not None and c_pos < pos - 1:
            cur = cur.next
            c_pos += 1
        if cur is None:
            print("Out of index")
            return
        new_node = DNode(data)
        new_node.next = cur.next
        new_node.prev = cur
        if cur.next:
            cur.next.prev = new_node
        cur.next = new_node
        self.size += 1

    def remove_pos(self, pos):
        if pos == 0:
            self.remove_head()
            return
        cur = self.head
        cur_pos = 0
        while cur and cur_pos < pos - 1:
            cur = cur.next
            cur_pos += 1
        if cur is None:
            print("Out of index")
            return
        node_to_remove = cur.next
        cur.next = node_to_remove.next
        if node_to_remove.next:
            node_to_remove.next.prev = cur
        if node_to_remove == self.tail:
            self.tail = cur

    def add_before(self, data, val):
        cur = self.head
        while cur:
            if cur.data == val:
                if cur == self.head:
                    self.add_head(data)
                    return
                new_node = DNode(data)
                cur.prev.next = new_node
                new_node.prev = cur.prev
                new_node.next = cur
                cur.prev = new_node
                self.size += 1
                return
            cur = cur.next
        print(f"No found value: {val}")

    def add_after(self, data, val):
        cur = self.head
        while cur:
            if cur.data == val:
                if cur == self.tail:
                    self.add_tail(data)
                    return
                new_node = DNode(data)
                new_node.next = cur.next
                cur.next.prev = new_node
                new_node.prev = cur
                cur.next = new_node
                self.size += 1
                return
            cur = cur.next
        print(f"No found value: {val}")

    def count_elements(self, head):
        pass
    def count_appearance(self, value):
        count = 0
        cur = self.head
        while cur:
            if cur.data == value:
                count += 1
            cur = cur.next
        return count

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            cur.next, cur.prev, prev, cur = cur.prev, cur.next, cur, cur.next
        self.tail, self.head = self.head, self.tail
        return self


    def remove_duplicates(self):
        pass
    def remove_element(self, key):
        pass

if __name__ == "__main__":
    a = DoublyLinkedList()
    a.add_head(5)
    a.add_head(10)
    a.add_pos(9,1)
    a.add_pos(6,2)
    print(a)


