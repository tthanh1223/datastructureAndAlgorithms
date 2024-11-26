#Given an array as follows:
#array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
#Let convert to
#array([ 0, 4, 8, 1, 5, 9, 2, 6, 10, 3, 7, 11])
import numpy as np
def ex1():
    import numpy as np
    a = np.arange(12).reshape(3,4)
    print(a)
    a = a.T
    print(a.flatten())

def ex2():
    """Create a random NxM matrix. Set all positive values x to 2x,
and -2 for negative values"""
    n,m = map(int, input().split())
    a = np.random.randint(low = -n*m,high = n*m,size = n*m).reshape((n,m))
    print(a)
    mask1 = a > 0
    mask2 = a < 0
    a = np.where(mask1,a*2, np.ones((n,m), dtype = np.int32) * (-2))
    print(a)

def ex3():
    """Create the following array with n inputted from keyboard.
    ▪ Ex: n = 10
    [[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
    [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]]"""
    n = int(input())
    if n % 2 == 0:
        a = np.concatenate((np.arange(n).reshape((2,-1)), np.ones(n).reshape(2,-1).astype(np.int32)), axis = 1)
    else:
        a = np.concatenate(np.arange(n))
    print(a)

def ex4():
    """▪ Given a = np.array([1,2,3])
    ▪ Create a following array without using iteration and array initialization:
    [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]"""
    a = np.array([1, 2, 3])
    b = a.repeat(3)
    c = np.tile(a, 3)
    print(np.concatenate((b, c)))

def ex5():
    arr = np.arange(9).reshape(3, 3)
    print(arr[::-1])

def ex6():
    """create_interleaved_array(n)"""
    n = int(input())
    while n % 2 != 0 or n <= 0:
        n = int(input())
    arr1 = np.arange(n*n//2).reshape(2,-1)
    arr2 = -np.arange(n*n//2,n**2).reshape(2,-1)
    res = np.empty((2, n * n//2),dtype=int)
    for i in range(n*n//4):
        # index theo cột,trên hàng, cột nào lẻ thì cho nó
        res[:, i * 2] = arr1[:, i]
        res[:, i * 2 + 1] = arr2[:, i]
    print(res)

def ex6_1():
    n = int(input())
    a = np.arange(n**2).reshape(-1,n*n//2).T.reshape(2,-1)
    b = np.where(a >= n*n//2, -a ,a)
    print(b)

def ex6_2():
    n = int(input())
    i = 0
    than = False
    while than is False:
        if i > n:
            return False
        elif i == n:
            than = True
        else:
            i += 3
    return True

if __name__ == '__main__':
    print(ex6_2())
