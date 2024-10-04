def moveZeroes(nums: list[int]):
    """
    Do not return anything, modify nums in-place instead.
    """
    # use another list for better understand
    # Create a list to hold non-zero elements
    non_zero_elements = []

    # Iterate through the input list and collect non-zero elements
    for num in nums:
        if num != 0:
            non_zero_elements.append(num)

    # Calculate the number of zeros to be added
    zeros_count = len(nums) - len(non_zero_elements)

    # Fill the original list with non-zero elements
    for i in range(len(non_zero_elements)):
        nums[i] = non_zero_elements[i]

    # Fill the remaining positions with zeros
    for i in range(len(non_zero_elements), len(nums)):
        nums[i] = 0

def moveZeroes1(nums: list[int]):
    index = 0  # Pointer for the position to place non-zero elements

    # First pass: Move non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1

    # Second pass: Fill the remaining positions with zeros
    for i in range(index, len(nums)):
        nums[i] = 0

