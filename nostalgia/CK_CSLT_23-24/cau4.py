# day con dong tri la day gom 2 hay nhieu phan tu lien tiep cung gia tri.
def dem_day_dong_tri(arr: list):
    count = 0
    index = 0
    while index < len(arr) - 1:
        sub_index = index + 1
        if arr[sub_index] == arr[index]:
            while sub_index < len(arr - 1) and arr[sub_index] == arr[index]:
                sub_index += 1
            count += 1
        index = sub_index
    return count


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    print("Số dãy đồng trị: ", dem_day_dong_tri(arr))