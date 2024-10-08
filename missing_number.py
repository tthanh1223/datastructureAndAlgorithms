def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])
    need = 0
    for i in range(n):
        if nums[i] > 0:
            need = i + 1
            break
    return need

arr = [3,0,1]
print(missingNumber(arr))