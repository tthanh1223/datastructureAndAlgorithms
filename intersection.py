#Given two integer arrays nums1 and nums2, return an array of their intersection.
#Each element in the result must be unique and you may return the result in any order.
from typing import List

def binary_search(nums:List[int], target:int) -> int:
    if len(nums) == 0:
        return -1
    left , right = 0 , len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

def intersection(num1: List[int], num2: List[int]) -> List[int]:
    result = set()
    num2.sort()
    for num in num1:
        index = binary_search(num2, num)
        if index < len(num2) and num2[index] == num:
            result.add(num)
    return list(result)

num1 = [4,9,5,9]
num2 = [9,4,9,8,4]
