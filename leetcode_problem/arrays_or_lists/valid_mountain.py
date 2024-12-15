def valid_mountain(arr):
    if len(arr) < 3:
        return False
    left = 0
    right = len(arr) - 1
    #climb from the left
    while left < len(arr) - 1 and arr[left] < arr[left + 1]:
        left += 1
    while right > 0 and arr[right] < arr[right - 1]:
        right -= 1
    return left == right and left != 0 and right != len(arr) - 1
print(valid_mountain([1,2,3,4,3,2,2,1]))