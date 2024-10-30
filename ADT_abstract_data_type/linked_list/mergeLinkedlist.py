class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next

    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.data, "-> ", end = "")
            cur = cur.next
        print("None")

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def delete_tail(self):
        if self.head is None: return
        cur = self.head
        # ds co 1 node
        if cur.next is None:
            self.head = None
        else:
            # co it nhat 2 node tro len
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None
    def find_node_first(self, key):
        # 5 ==> Node(data = 5, next = Node(3))
        cur = self.head
        while cur is not None:
            if cur.data == key:
                return cur
            else:
                cur = cur.next
        return None

    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count
def merge_two_linkedlist_ver1(l1: LinkedList, l2: LinkedList) -> LinkedList:
    # Cho 2 ds l1, l2 tăng dần
    # trộn 2 ds này lại sao cho
    # thu được ds tăng dần
    # l1: 1 -> 5 -> 9 -> None
    # l2: 3 -> 10 -> None
    # return: l3: 1 -> 3 -> 5 -> 9 -> 10 -> None
    # version 1: được tạo danh sách mới
    result = LinkedList()
    cur1 = l1.head
    cur2 = l2.head
    while cur1 and cur2 is not None:
        if cur1.data <= cur2.data:
            result.add_tail(cur1.data)
            cur1 = cur1.next
        else:
            result.add_tail(cur2.data)
            cur2 = cur2.next
    while cur1 is not None:
        result.add_tail(cur1.data)
        cur1 = cur1.next
    while cur2 is not None:
        result.add_tail(cur2.data)
        cur2 = cur2.next
    return result


def merge_two_linkedlist_ver2(l1: LinkedList, l2: LinkedList) -> LinkedList:
    # version 2: merging l2 into l1 without creating a new list
    cur1 = l1.head
    cur2 = l2.head
    if not cur1:
        l1.head = cur2
        return
    if not cur2:
        return
    # If l1's first node should be replaced
    if cur1.data > cur2.data:
        l1.head, cur2.next, cur1 = cur2, cur1, cur2.next
        cur2 = l1.head  # Update cur2 to the new head of l1
    # Merge nodes
    prev1 = None
    while cur1 and cur2:
        if cur2.data < cur1.data:
            if prev1:
                prev1.next = cur2
            temp = cur2.next
            cur2.next = cur1
            prev1 = cur2
            cur2 = temp
        else:
            prev1 = cur1
            cur1 = cur1.next

    # If there are remaining nodes in l2
    if cur2:
        prev1.next = cur2
    return l1
if __name__ == "__main__":
    l1 = LinkedList()
    l1.add_tail(1)
    l1.add_tail(3)
    l1.add_tail(5)
    l1.add_tail(7)
    l2 = LinkedList()
    l2.add_tail(2)
    l2.add_tail(4)
    a = merge_two_linkedlist_ver2(l1, l2)
    a.display()



