# the next greater element of some element x in an array is the first greater element
# that is to the right of x in the same way.
# input: 2 arrays: nums1 and nums2 , where nums1 is a subset of nums2
# for 0 <= i < nums1.length find j such that nums1[i] = nums2[j]
# and determine the next greater element of nums2[j] in nums2.
# if there is no next greater element then print -1.
# OUTPUT: ans []

def find_next_greater_element(nums1, nums2):
    ans = []
    for i in nums1:
        index = nums2.index(i)
        found = False
        j = index + 1
        while not found and j <= len(nums2) - 1:
            if nums2[j] > i:
                ans.append(nums2[j])
                found = True
            j += 1
        if not found:
            ans.append(-1)
    return ans

def next_greater_element_with_stack(nums1, nums2):
    map = {}
    stack = []
    for num in nums2:
        if not stack or stack[-1] > num:
            stack.append(num)
        else:
            while stack and stack[-1] < num:
                map[stack.pop()] = num
            stack.append(num)
    while stack:
        map[stack.pop()] = -1
    res = []
    for num in nums1:
        res.append(map[num])
    return res

if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(find_next_greater_element(nums1, nums2))