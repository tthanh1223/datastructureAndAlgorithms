#Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Maybe we should store list into 2 dictionaries then check if value of key are the same if yes add to the list the number "value" of the key.
from typing import List


def intersect(nums1:List[int], nums2:List[int])->List[int]:
    #create a hash map
    hash_map = {}
    result = []
    for num in nums1:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1
    #find intersection with nums2
    for num in nums2:
        if num in hash_map and hash_map[num] > 0:
            result.append(num)
            hash_map[num] -= 1
    return result
#O(n+m)
#What if the given array is already sorted? How would you optimize your algorithm?
def binary_search1(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def intersect1(nums1, nums2):
    # Step 1: Initialize the result array
    result = []

    # Step 2: Iterate through the smaller array (nums2)
    for num in nums2:
        if binary_search1(nums1, num):
            result.append(num)
            # Optionally, you can remove the found element from nums1 or mark it as used

    # Step 3: Return the result
    return result
nums1 = [1,2,2,1,3,3]
nums2 = [2,2,2]
print(intersect1(nums1, nums2))


