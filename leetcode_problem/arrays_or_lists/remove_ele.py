def remove_element(nums:list[int], val:int) -> int:
    left = 0
    right = len(nums)
    while left < right:
        if nums[left] == val:
            #Swap with the last element that is not val
            right -= 1
            nums[left],nums[right] =nums[right] ,nums[left]
        else:
            left += 1
    print(nums)
    return right

print(remove_element([3,2,2,3],3))
def remove_element1(nums: list[int], val: int) -> int:
    # Pointer for the next position to insert non-val elements
    new_length = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is not equal to val, write it at the new_length position
        if nums[i] != val:
            nums[new_length] = nums[i]
            new_length += 1

    return new_length  # Return the new length of the array