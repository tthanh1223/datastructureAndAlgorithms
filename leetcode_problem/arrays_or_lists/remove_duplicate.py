def remove_duplicates(nums:list[int]) -> int:
    if not nums:
        return 0
    #pointer to the last unique element found
    index = 0
    for i in range(len(nums)):
        #nếu số này khác số unique đầu tiên thì khi
        # đó có 2 số unique - sửa lại thành cái này)
        #good algorithms because only take time
        # complexity: O(n) instead of normal brutal force O(n^2)
        if nums[i] != nums[index]:
            index += 1
            nums[index] = nums[i]
    print(nums)
    return index + 1
remove_duplicates([1,1,2,3,4,4,4])
