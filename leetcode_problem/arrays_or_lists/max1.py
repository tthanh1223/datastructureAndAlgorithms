def longest_consecutive_1s(nums:list[int]) -> int:
    n = len(nums)
    longest = 0
    # each time meet 0 save the length we of consecutive 1 and compare it to the longest
    length = 0
    for i in range(n):
        if nums[i] == 1:
            length += 1
        elif nums[i] == 0:
            longest = max(longest, length)
            length = 0
            continue
    return max(longest, length)

print(longest_consecutive_1s([1,1, 0, 1, 1,1,  0,1,1,1,1]))