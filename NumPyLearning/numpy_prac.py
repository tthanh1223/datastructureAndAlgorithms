import numpy as np
def replace_odd_num(array1):
    array1 = np.where(array1 % 2 == 1, -1, array1)
    return array1

def reshape_1D_into_matrix():
    """Write a function to reshape a 1D array with n×n elements into an n×n matrix."""
    n = int(input())
    nar = np.arange(n**2).reshape((n,-1))
    print(nar)

def ex3():
    """Write a function to create a 1D array of n random integers. Each integer must be between i and k."""
    n = int(input())
    i = int(input("Lower bound: "))
    k = int(input("Upper bound: "))
    print(np.random.randint(i,k,(n,)))

def ex4():
    """Write a function to extract the k-th column from an n×n matrix."""
    #create a random nxn matrix
    n = int(input())
    arr = np.random.random((n,n))
    k = int(input("Extract column-th: "))
    if k > n - 1:
        k = int(input("Extract column-th: "))
    print(arr[:][k])

def ex5():
    """Given an m×n matrix with random values between 10 and 100, write a function to return an array containing
the rows where all elements are unique."""
    m,n = map(int,input().split())
    arr = np.random.randint(10,100,(m,n))
    def has_unique_values(row):
        uniques_value = np.unique(row)
        return len(uniques_value) == len(row)
    # Hàm apply_along_axis này hay nè
    mask = np.apply_along_axis(has_unique_values, axis = 1, arr = arr)
    arr = arr[mask]
    print(arr)

def ex6():
    """Write a function to compute the product of elements in each row of a matrix."""
    m, n = map(int, input().split())
    arr = np.random.randint(1, 9, (m, n))
    print(arr)
    # dùng hàm của np np.prod() nó mới gọi là dùng numpy chứ (nhưng mà phải học thuộc bài)
    row_product = np.prod(arr, axis = 1)
    print(row_product)

def ex7():
    """Given an m×n matrix with random values between 10 and 100, write a function to calculate the sum of all
numbers with values between 20 and 50."""
    m, n = map(int, input().split())
    arr = np.random.randint(10, 100, (m, n))
    #cách trẻ con
    #sum1 = 0
    #for i in range(len(arr)):
    #    for j in range(len(arr[0])):
    #        if 20 <= arr[i][j] <= 50:
    #            sum1 += arr[i][j]
    #print(sum1)
    # cách người lớn
    mask =  (arr >= 20) & (arr <= 50)
    sum1 = np.sum(arr[mask])
    print(sum1)

def ex8():
    """Write a function to reverse a 1D array or a matrix vertically."""
    flg = int(input("""
You want to reverse a 1D or a matrix? 
1. 1D
2. matrix\n"""))
    if flg == 1:
        m = int(input())
        arr = np.arange(m)
        arr = arr[::-1]
        print(arr)
    elif flg == 2:
        m,n = map(int, input().split())
        arr = np.arange(m*n).reshape((m,n))
        print(arr)
        def reverse_vertically(column):
            return column[::-1]
        ## dùng apply_along_axis( cũng hay)
        arr = np.apply_along_axis(reverse_vertically, axis = 0,arr = arr)
        print(arr)
        ## reverse kiểu bình thường
        arr = arr[::-1,:]
        print(arr)

def ex9():
    """Write a function to find the row with the maximum sum in a matrix."""
    m, n = map(int, input().split())
    arr = np.random.randint(1, 9, (m, n))
    print(arr)
    sum_arr = np.sum(arr, axis = 1)
    print(sum_arr)
    print(np.max(sum_arr))
def ex10():
    """Write a function to create a diagonal matrix from a 1D array."""
    n = int(input())
    arr = np.arange(n)
    arr = np.diag(arr, k = 0)
    print(arr)
if __name__ == "__main__":
    ex10()