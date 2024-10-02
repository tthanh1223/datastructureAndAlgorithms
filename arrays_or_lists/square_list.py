def sortedSquares(nums: list[int]) -> list[int]:
    #turn negative into positive ( n step)
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] *= -1
        print(nums[i])
    # sort it it by sort() built in function ( O(n log n )
    nums.sort()
    #print the array (n step)
    sq_lst = list(nums[i]**2 for i in range(len(nums)))
    return sq_lst
    #total: O(n log n) for time and O(n) for space
def sorted_squares(nums: list[int]) -> list[int]:
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)
    pos = len(nums) - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left]**2
            left += 1
        else:
            result[pos] = nums[right]**2
            right -= 1
        pos -= 1
    return result
nums = [1,2,-1,-2,-3]
print(sortedSquares(nums))
print(sorted_squares(nums))