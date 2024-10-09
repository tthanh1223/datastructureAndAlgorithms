from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []
    hash_table = {}
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            other = -nums[i] - nums[j]
            if other in hash_table and hash_table[other] != j and hash_table[other] != i:
                triplet = sorted([nums[i], nums[j], other])
                if triplet not in result:
                    result.append(triplet)
            hash_table[nums[j]] = j
    return result

print(threeSum([1,2,-2,-1]))