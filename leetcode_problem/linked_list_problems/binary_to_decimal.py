# convert binary number in a Linked List to Integer
def merge_dicts(d1, d2):
    """Merge two nested dictionaries recursively."""
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = merge_dicts(merged[key], value)
        else:
            merged[key] = value
    return merged

def is_sorted(words, order):
    # Create a mapping from character to its rank in the custom order
    order_map = {char: i for i, char in enumerate(order)}

    def compare(word1, word2):
        # Compare two words based on the custom order
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                return order_map[c1] < order_map[c2]
        # If all characters are the same, the shorter word should come first
        return len(word1) <= len(word2)

    # Check all adjacent word pairs in the list
    for i in range(len(words) - 1):
        if not compare(words[i], words[i + 1]):
            return False
    return True




class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def get_decimal_value(head: ListNode) -> int:
    cur = head
    res = 0
    while cur:
        res = 2*res + cur.val
        cur = cur.next
    return res

if __name__ == "__main__":
    print(a)