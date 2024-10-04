def findMin(nums: list[int]) -> int:
    n = len(nums)
    if n == 0: return -1
    left, right = 0, n - 1
    while left  < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right -= 1
    return nums[left]
lst = [3,3,1,3,3]
print(findMin(lst))