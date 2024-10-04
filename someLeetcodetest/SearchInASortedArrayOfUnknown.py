#API : get(index) return elements at index
#You cannot directly access the array's length or its elements by indexing like arr[index].
# Define the array (for testing purposes)
from typing import Any

test_array = list(range(10000000))
# Define the get function
def get(index):
    if 0 <= index < len(test_array):
        return test_array[index]
    else:
        return None  # Simulates an out-of-bounds index

def searchInUnknownSizeArray(arr, target:int) -> int | None | Any:
    if get(0) == target: return 0
    #if get(1) == target: return 1 // No need
    find_target = False
    i = 1
    while not find_target and get(i*2) is not None:
        low = get(i)
        high = get(i*2)
        if low <= target <= high:
            find_target = True
            left = i
            right = i * 2
            if get(left) == target : return left
            if get(right) == target: return right
            while left <= right:
                mid = left + (right - left) // 2
                if get(mid) == target:
                    return mid
                elif get(mid) < target:
                    left = mid + 1
                else:
                    right = mid - 1
        i *= 2
    left = i
    right = i * 2
    while left <= right:
        mid = left + (right - left) // 2
        if get(mid) is None:
            right = mid - 1
        elif get(mid) == target:
            return mid
        elif get(mid) < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


# Let's assume you have an array [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, ...] which continues indefinitely.
print(test_array)
target = 284245
result = searchInUnknownSizeArray(test_array, target)
print(result)  # Output: 3 (because 7 is at index 3)

target = 97813811
result = searchInUnknownSizeArray(test_array, target)
print(result)  # Output: -1 (because 4 is not in the array)
