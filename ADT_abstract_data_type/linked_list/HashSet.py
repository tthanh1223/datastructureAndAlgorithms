# design a HashSet with linked_list
# A hashSet is a data structure that stores a collection of unique elements, and it does
# not maintain any specific order of the elements.
# It's based on the concept of hashing, which allows for very fast insertion, deletion
# and lookup operations.
#   - Uniqueness
#   - Unordered
#   - Hashing
#   - Set Operations
# Examples: set data-type built-in python
class MyHashSet:
    def __init__(self):
        self.linked_list = []

    def add(self, key:int) -> None:
        if key not in self.linked_list:
            self.linked_list.append(key)
        else:
            return

    def remove(self, key: int) -> None:
        if key not in self.linked_list:
            return
        self.linked_list.remove(key)

    def contains(self, key:int) -> bool:
        return key in self.linked_list
#O(1) time complexity

class MyHashSet2:
    def __init__(self):
        self.hash = {}

    def add(self, key: int) -> None:
        self.hash[key] = True

    def remove(self, key:int) -> None:
        self.hash.pop(key, None)

    def contains(self, key: int) -> None:
        return key in self.hash
# O(1) better than list


class ListNode:
    """For my HashSet"""
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class MyHashSetWithSLL:
    def __init__(self):
        self.size = 10**6
        self.buckets = [None] * self.size

    def _hash(self, key):
        """Hash function to map keys to bucket indices"""
        return key % self.size

    def add(self, key: int) -> None:
        """Add a key to the HashSet"""
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key)
        else:
            current = self.buckets[index]
            while current:
                if current.value == key:
                    self.buckets[index] = ListNode(key)
                if current.next is None:
                    current.next = ListNode(key)
                    return
                current = current.next

    def contains(self, key: int) -> bool:
        """Check if the key exists in the HashSet"""
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.value == key:
                return True
            current = current.next
        return False

    def remove(self, key: int) -> None:
        """Remove a key from the HashSet if it exists"""
        index = self._hash(key)
        current = self.buckets[index]
        prev = None
        while current:
            if current.value == key:
                if prev is None:
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
