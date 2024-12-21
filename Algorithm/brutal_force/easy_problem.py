# 1.Find the maximum product of two numbers in an array
def max_product(arr: list):
    max_prod = 0
    x1, y1 = 0,0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > max_prod:
                max_prod = arr[i] * arr[j]
                x1, y1 = i, j
    return max_prod, (x1,y1)

# 2.Find the sum of all subsets of an array:
def sum_subsets(arr: list):
    res = []


if __name__ == '__main__':
    arr = [1,5,6,7234,64,3]
    print(max_product(arr))
