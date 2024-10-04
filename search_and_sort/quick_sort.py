import random

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)

def quick_sort_helper(arr, left, right):
    if left < right:
        split_point = partition(arr, left, right)
        quick_sort_helper(arr, left, split_point - 1)
        quick_sort_helper(arr, split_point + 1, right)

def partition(arr, left, right):
    pivot_value = arr[left]
    left_mark = left + 1
    right_mark  = right
    done = False
    while not done:
        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark += 1
        while arr[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]
    arr[left], arr[right_mark] = arr[right_mark], arr[left]
    return right_mark

if __name__ == '__main__':
    a_list = list(random.sample(range(1, 10001), 10000))
    print(a_list)
    quick_sort(a_list)
    print(a_list)
