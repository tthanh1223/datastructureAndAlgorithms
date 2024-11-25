#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
    def reverse(self):
        result = SinglyLinkedList()
        current = self.head
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        result.head = previous
        return result
def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

def check_palindrome(lst):
    reverse_lst = lst.reverse()
    p1 = lst.head
    p2 = reverse_lst.head
    while p1 and p2 is not None:
        if p1.data != p2.data:
            return False
        p1 = p1.next
        p2 = p2.next
    return True



if __name__ == '__main__':
    list1_count = int(input().strip())
    list1 = SinglyLinkedList()
    list1_item = list(map(int, input().split()))
    for i in range(list1_count):
        list1.insert_node(list1_item[i])
    print(check_palindrome(list1))
