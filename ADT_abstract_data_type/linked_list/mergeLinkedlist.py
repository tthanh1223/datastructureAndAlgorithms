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

    def delete_head_second_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        if self.head.next is not None:
            self.head.next = self.head.next.next
        return

    def sum(self):
        """
        Count the sum of the node
        @return: int
        """
        s = 0
        cur = self.head
        if cur is None:
            return 0
        if cur.next is None:
            return cur.data
        while cur is not None:
            s += cur.data
            cur = cur.next
        return s

    def check_balance(self):
        """
        a list is balance only if abs of the sum of k first nodes - sum of the others < 1/2 sum of the list.
        @return: index or -1
        """
        sum_of_list = self.sum()
        # | a - b | < 1/2 ( a + b) <=> - 1/2 (a + b) < (a-b) < 1/2 ( a + b)
        # <=> -a - b < 2a - 2b and 2a - 2b < a + b
        # <=> b < 3a and a < 3b
        # viet b = s - a ta co: s -a < 3a and a < 3(s-a) hay s < 4a and 4a < 3s
        sum_traversal = 0
        result = -1
        is_balance = False
        cur = self.head
        index = 0
        while cur is not None and is_balance is False:
            index = index + 1
            result = index
            sum_traversal += cur.data
            if abs(sum_traversal - (sum_of_list - sum_traversal)) < 1/2 * sum_of_list:
                is_balance = True
            cur = cur.next
        return result


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
    # Base case - l1 is empty
    if not cur1:
        l1.head = cur2
        return
    # Base case - l2 is empty
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
        cur2 = cur2.next
    return l1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    dummy = result
    while list1 and list2 is not None:
        if list1.val <= list2.val:
            result.next = list1
            list1, result = list1.next, list1
        else:
            result.next = list2
            list2, result = list2.next, list2
    while list1 is not None:
        result.next = list1
        list1, result = list1.next, list1
    while list2 is not None:
        result.next = list2
        list2, result = list2.next, list2
    return dummy.next

if __name__ == "__main__":
    l1 = LinkedList()
    l1.add_tail(1)
    l1.add_tail(3)
    l1.add_tail(5)
    l1.add_tail(3)
    print(l1.check_balance())



