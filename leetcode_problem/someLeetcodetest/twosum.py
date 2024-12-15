from typing import List


def binary_search(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def twoSum(numbers: List[int], target: int) -> List[int]:
    num_to_index = {}  # Dictionary to store number and its index
    result = []

    for i, num in enumerate(numbers):
        need = target - num
        if need in num_to_index:
            result.append(num_to_index[need] + 1)  # Append the 1-based index of the complement
            result.append(i + 1)  # Append the 1-based index of the current number
            return result

        # Store the index of the current number
        num_to_index[num] = i

    return result  # Return an empty list if no solution found
