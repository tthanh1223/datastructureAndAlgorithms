from heapq import merge


def merge_sorted_array(arr1: list[int], m:int, arr2: list[int], n:int):
    new_1 = arr1[:m]
    new_2 = arr2[:n]
    pos = 0
    result = [0] * ( m + n)
    pos1, pos2 = 0,0
    while pos1 < len(new_1) and pos2 < len(new_2):
        if new_1[pos1] < new_2[pos2]:
            result[pos] = new_1[pos1]
            pos1 += 1
            pos += 1
        else:
            result[pos] = new_2[pos2]
            pos2 += 1
            pos += 1
    while pos1 < m:
        result[pos] = new_1[pos1]
        pos1 += 1
        pos += 1
    while pos2 < n:
        result[pos] = new_2[pos2]
        pos2 += 1
        pos += 1
    return result
a = [1,2,3,4,5,6,7,8]
b = [9,10,11,12,13,14]
print(merge_sorted_array([1,2,3,0,0,0],3,[2,5,6],3))

def merge_sorted_array_return_nums1(nums1, m:int, nums2, n:int):
    nums1 = nums1[:m+n]
    pos1 = m - 1
    pos2 = n - 1
    merge_pos = m + n - 1
    while pos2 >= 0:
        if pos2 >= 0 and nums1[pos1] > nums2[pos2]:
            nums1[merge_pos] = nums1[pos1]
            pos1 -= 1
        else:
            nums1[merge_pos] = nums2[pos2]
            pos2 -= 1
        merge_pos -= 1
    return nums1
    #get the code - we insert from first of the list
print(merge_sorted_array_return_nums1([1,2,3,0,0,0],3,[2,5,6],))