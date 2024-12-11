from debugpy.common.timestamp import current


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head
        self.tail = None
        self.size = 0

    def add_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_tail(self ,data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def size(self):
        return self.size

    def __str__(self):
        cur = self.head
        dis = ""
        while cur is not None:
            dis += f"{cur.data} -> "
            cur = cur.next
        dis += "None"
        return dis

    def remove_head(self):
        if self.head is None:
            return
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def remove_tail(self):
        if self.head is None:
            return
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            cur = self.head
            while cur.next != self.tail:
                cur = cur.next
            cur.next = None
            self.tail = cur
        self.size -= 1
#1(head) -> 2 -> 3(tail) -> None
    def clear_all(self):
        self.__init__()

    def find_node(self, data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def remove_before(self, data):
        if self.size <= 1:
            return
        else:
            if self.find_node(data):
                cur = self.head
                previous = None
                while cur.next.data != data:
                    previous = cur
                    cur = cur.next
                    print("Previous :",previous)
                    print("Cur :", cur)
                if previous is None:
                    self.head = cur.next
                else:
                    previous.next = cur.next
                self.size -= 1

    def remove_after(self, data):
        if self.size <= 1:
            return
        else:
            if self.findNode(data):
                cur = self.head
                while cur.data != data:
                    cur = cur.next
                    print("Cur :", cur)
                if cur.next.next is None:
                    cur.next = None
                    self.tail = cur
                else:
                    cur.next = cur.next.next
        self.size -= 1

    def add_pos(self, data, pos):
        if pos < 0 or pos > self.size-1:
            return
        if pos == 0:
            self.add_head(data)
        cur = self.head
        for _ in range(pos-1):
            cur = cur.next
        new_node = Node(data)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def remove_pos(self, pos):
        cur = self.head
        if pos < 0 or pos > self.size-1:
            return
        if pos == 0:
            self.remove_head()
        elif pos == self.size-1:
            self.remove_tail()
        else:
            for _ in range(pos-1):
                previous,cur = cur, cur.next
            previous.next = cur.next
            self.size -= 1

    def add_before(self, data, val):
        if self.find_node(val):
            cur = self.head
            if cur.data == val:
                self.add_head(data)
            else:
                while cur.next.data != val:
                    cur = cur.next
                new_node = Node(data)
                new_node.next = cur.next
                cur.next = new_node
        self.size += 1

    def add_after(self, data, val):
        if self.find_node(val):
            cur = self.head
            while cur.data != val:
                cur = cur.next
            new_node = Node(data)
            new_node.next = cur.next
            cur.next = new_node
            if new_node.next is None:
                self.tail = new_node
            self.size += 1

    def count_appearance(self, value):
        if self.find_node(value):
            return 0
        count = 0
        cur = self.head
        while cur is not None:
            if cur.data == value:
                count += 1
        return count

    def get_elements(self):
        cur = self.head
        result = []
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result

    def reverse_list_with_new(self):
        # khong co prev nen chi co the lay data va lam mot cai day moi
        # tao list moi
        result = self.getElements()[::-1]
        print(result)
        index = 0
        new_list = SinglyLinkedList()
        while index < len(result):
            new_list.add_tail(result[index])
            index += 1
        return new_list

    def reverse_list(self):
        prev = None
        cur = self.head
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        result = SinglyLinkedList(prev)
        return result

    def remove_duplicate(self):
        if not self.head:
            return
        seen = set()
        current = self.head
        prev = None
        while current:
            if current.data in seen:
                if current.next is None:
                    self.tail = prev
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def remove_element(self, value):
        """Remove all key value in the linked list"""
        if not self.find_node(value):
            return
        prev = None
        current = self.head
        while current:
            if current.data == value:
                if current.next is None:
                    self.tail = prev
                prev.next = current.next
            else:
                prev = current
            current = current.next

if __name__ == '__main__':
    lst = SinglyLinkedList()
    lst.add_head(10)
    lst.add_tail(20)
    lst.add_pos(14,1)
    lst.add_pos(13,2)
    lst.add_pos(12,3)
    lst.remove_pos(3)
    lst.add_after(9,20)
    lst.add_pos(10,3)
    lst.add_pos(20,2)
    lst.add_pos(9,1)
    print(lst)
    lst.remove_element(9)
    print(lst)
    print(lst.tail)
