class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    res = ListNode()
    dummy = res
    carry = 0
    while l1 or l2 or carry != 0:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum1 = x + y + carry
        carry = sum1 // 10
        sum1 = sum1 % 10
        dummy.next = ListNode(sum1)
        dummy.next.next = None
        dummy = dummy.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return res.next



