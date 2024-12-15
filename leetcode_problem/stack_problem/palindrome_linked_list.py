# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
     self.val = val
     self.next = next
def check_palindrome_with_stack(head: ListNode):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    fast = head
    stack = []
    while slow:
        stack.append(slow.val)
        slow = slow.next
    while stack:
        if fast.val != stack.pop():
            return False
        fast = fast.next
    return True

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    lst = create_linked_list([1,2,2,1])
    print(check_palindrome_with_stack(lst))
    lst = create_linked_list([1,2,2,1,2])
    print(check_palindrome_with_stack(lst))