def duplicate_zeros(arr):
    before_n = len(arr)
    index = 0
    #dùng hàm while hay hơn
    while index < before_n:
        if arr[index] == 0:
            arr.insert(index,0)
            arr.pop()
            index += 1
        index += 1
    return arr

def duplicate_zeros2(arr):
    n = len(arr)
    zeros_to_duplicate = arr.count(0)
    new_length = n + zeros_to_duplicate

    for i in range(n - 1, -1, -1):
        if i + zeros_to_duplicate < n:
            arr[i + zeros_to_duplicate] = arr[i]
        if arr[i] == 0:
            zeros_to_duplicate -= 1
            if i + zeros_to_duplicate < n:
                arr[i + zeros_to_duplicate] = 0

    return arr
arr = [1,0,1,0,2]
duplicate_zeros(arr)
print(arr)