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

    def find_node(self, value):
        cur = self.head
        while cur is not None:
            if cur.data == value:
                return True
            cur = cur.next
        return False

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

def remove_duplicates(lst):
    result = SinglyLinkedList()
    pointer = lst.head
    while pointer:
        if not result.find_node(pointer.data):
            result.insert_node(pointer.data)
        pointer = pointer.next
    return result.head
if __name__ == '__main__':
    list1_count = int(input().strip())
    list1 = SinglyLinkedList()
    list1_item = list(map(int, input().split()))
    for i in range(list1_count):
        list1.insert_node(list1_item[i])
    new_list = remove_duplicates(list1)
    print_singly_linked_list(new_list, sep=' ')
