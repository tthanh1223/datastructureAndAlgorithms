def sortArrayByParity(nums: list[int]) -> list[int]:
    if len(nums) == 0:
        return nums
    end = len(nums) - 1
    i = 0
    while i < end:
        if nums[i] % 2 != 0:
            while nums[end] % 2 != 0 and end > i:
                end -= 1
            nums[end],nums[i] = nums[i], nums[end]
        i += 1
    return nums

array = [0,1,3]
print(sortArrayByParity(array))