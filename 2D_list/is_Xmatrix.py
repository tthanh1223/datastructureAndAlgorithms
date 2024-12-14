# A square matrix is considered a X-matrix if it meets the following conditions:
# - The intersections of its main diagonal and anti-diagonal is zero
# - ALl elements on the main diagonal are > 0
# - anti-diagonal < 0
def is_XMatrix(mat):
    # intersection is zeros
    n = len(mat)
    if mat[n // 2][n // 2] != 0:
        return False
    for i in range(n):
        if i != (n // 2):
            if mat[i][i] <= 0:
                return False
            if mat[i][n - i -1] >= 0:
                return False
    return True
    # main diagonal --> positive
    #  > 0 ==> <= 0

def is_possible_to_convert(mat):
    if is_XMatrix(mat): return True
    else:
        # swap
        n = len(mat)
        for i in range(n):
            mat[i][i], mat[i][n - i - 1] = mat[i][n - i - 1], mat[i][i]
        if is_XMatrix(mat): return True
        else: return False

matrix = [[-1, 2, 3],
          [4, 0, 6],
          [7, 8, -9]]
print(is_XMatrix(matrix))
print(is_possible_to_convert(matrix))
print(matrix)