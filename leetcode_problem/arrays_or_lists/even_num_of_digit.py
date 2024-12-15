def findNumbers(nums: list[int]) -> int:
    def get_num_digit(num: int) -> int:
        return len(str(num))
    count = 0
    for num in nums:
        digits = get_num_digit(num)
        if digits % 2 == 0:
            count += 1
    return count