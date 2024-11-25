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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')


def merge_two_linked_list(l1, l2):
    result = SinglyLinkedList()
    p1 = l1.head
    p2 = l2.head
    while p1 and p2 is not None:
        if p1.data < p2.data:
            result.insert_node(p1.data)
            p1 = p1.next
        else:
            result.insert_node(p2.data)
            p2 = p2.next
    while p1 is not None:
        result.insert_node(p1.data)
        p1 = p1.next
    while p2 is not None:
        result.insert_node(p2.data)
        p2 = p2.next
    return result.head

if __name__ == '__main__':
    list1_count, list2_count = map(int, input().split())
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()
    list1_item = list(map(int, input().split()))
    list2_item = list(map(int, input().split()))
    for i in range(list1_count):
        list1.insert_node(list1_item[i])
    for i in range(list2_count):
        list2.insert_node(list2_item[i])

    head_node =  merge_two_linked_list(list1, list2)
    print_singly_linked_list(head_node, " ")