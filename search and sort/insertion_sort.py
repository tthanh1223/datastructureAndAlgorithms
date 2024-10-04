def insertion_sort(arr):
    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = current_value

a_list = [54,26,93,14,44,31,44,55,20]
insertion_sort(a_list)
print(a_list)