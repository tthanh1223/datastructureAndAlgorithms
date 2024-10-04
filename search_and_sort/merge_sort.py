import random
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        left_p = 0
        right_p = 0
        main_p = 0
        while left_p < len(left_half) and right_p < len(right_half):
            if left_half[left_p] < right_half[right_p]:
                arr[main_p] = left_half[left_p]
                left_p += 1
            else:
                arr[main_p] = right_half[right_p]
                right_p += 1
            main_p += 1

        while left_p < len(left_half):
            arr[main_p] = left_half[left_p]
            main_p += 1
            left_p += 1

        while right_p < len(right_half):
            arr[main_p] = right_half[right_p]
            main_p += 1
            right_p += 1
    return arr
if __name__ == "__main__":
    lst = list(random.randint(1, 1000000) for _ in range(10000))
    merge_sort(lst)
    print(lst)
