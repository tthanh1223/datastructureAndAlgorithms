#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
from intersection import binary_search

#There is only one repeated number in nums, return this repeated number.

#You must solve the problem without modifying the array nums and using only constant extra space.
#brutal force : O(n^2) space is constant
#use a dict: time:O(n) need more space : O(n)
#use a binary_search: time O(n*log(n)) space is constant > brutal force
#aim: O(n) and constant space
from typing import List

def findDuplicate(nums: List[int]) -> int:
    # Step 1: Initialize the tortoise and hare
    tortoise = nums[0]
    hare = nums[0]

    # Step 2: First phase to find the intersection point
    while True:
        tortoise = nums[tortoise]  # Move tortoise one step
        hare = nums[nums[hare]]     # Move hare two steps
        print(f"Debug: Tortoise = {tortoise}, Hare = {hare}")  # Debugging output
        if tortoise == hare:
            break

    # Step 3: Second phase to find the entrance to the cycle
    tortoise = nums[0]  # Reset tortoise to the beginning
    while tortoise != hare:
        tortoise = nums[tortoise]  # Move one step
        hare = nums[hare]           # Move one step
        print(f"Debug: Tortoise = {tortoise}, Hare = {hare}")  # Debugging output

    return hare  # or tortoise, both are at the entrance

# Example usage
nums = [3, 1, 5,6,7,8,9,10,2, 4, 2]
result = findDuplicate(nums)
print(f"Repeated number: {result}")  # Output: 3
