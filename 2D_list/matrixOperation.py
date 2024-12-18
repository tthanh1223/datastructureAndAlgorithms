def input_matrix(length):
    result = []
    for i in range(length):
        result.append(list(map(int, input().split())))
    return result

def output_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def transform_matrix_ver1(matrix):
    # chuyển thành array 1D
    flatten_array = []
    length = len(matrix)
    for i in range(length):
        for j in range(len(matrix[0])):
            flatten_array.append(matrix[i][j])
    flatten_array.sort()
    diagonal_start_points = []
    for i in range(length):
        diagonal_start_points.append((0, i))
    for i in range(1, length):
        diagonal_start_points.append((i, length - 1))
    print(diagonal_start_points)
    new_matrix = [[0] * length for _ in range(length)]
    index = 0
    for start in diagonal_start_points:
        i, j = start
        diagonal_elements = []
        # lấy mấy vị trí trên đường chéo đang xét
        while i < length and j >= 0:
            diagonal_elements.append((i, j))
            i += 1
            j -= 1
        for i, j in diagonal_elements:
            new_matrix[i][j] = flatten_array[index]
            index += 1
    return new_matrix

# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
#into
# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7
# a a a a b
# b a a b a
# a b a a a
# a b a b a
# b a a a b
# turning-point_4 = 0,3 -> 3,3 -> 3,0 -> 1,0 -> 1,2 -> 2,2 -> 2,1
# turning point_3 = 0,2 -> 2,2 -> 2,0 -> 1,0 -> 1,1
# turning-point_5 = 0,4 -> 4,4 -> 4,0 -> 1,0 -> 1,3 -> 3,3 -> 3,1 -> 2,1 -> 2,2
def transform_into_spiral_matrix_ver1(matrix): # spiral transformation
    flatten_array = []
    length = len(matrix)
    for i in range(length):
        flatten_array.extend(matrix[i])
    print(flatten_array)
    spiral_matrix = [[0] * length for _ in range(length)]
    #limits for spiral
    top, bottom, left, right = 0, length - 1, 0, length - 1
    index = 0
    while top <= bottom and left <= right:
        #Traverse from left to right along the top row
        for i in range(left, right + 1):
            spiral_matrix[top][i] = flatten_array[index]
            index += 1
        top += 1
        # Traverse from top to bottom along the rightmost column
        for i in range(top, bottom + 1):
            spiral_matrix[i][right] = flatten_array[index]
            index += 1
        right -= 1
        # Traverse from right to left along the bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral_matrix[bottom][i] = flatten_array[index]
                index += 1
            bottom -= 1
        # Traverse from the bottom to top along the leftmost column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral_matrix[i][left] = flatten_array[index]
                index += 1
            left += 1
    return spiral_matrix

def transform_into_spiral_matrix_ver2(matrix):
    n = len(matrix)
    flatten_array = []
    for row in matrix:
        flatten_array.extend(row)
    # flatten_array.sort()  #only needed if sorted order is required in spiral
    spiral_matrix = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    #define movement directions and rotate-flag
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction = 0  # start by moving "right"
    row, col = 0, 0  # Starting position
    for value in flatten_array:
        spiral_matrix[row][col] = value
        visited[row][col] = True
        #next cell in the current direction
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]
        # check if we need to rotate (out of bounds or visited cell)
        if not (0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]):
            #rotate to the next direction
            direction = (direction + 1) % 4
            next_row = row + directions[direction][0]
            next_col = col + directions[direction][1]
        row, col = next_row, next_col
    return spiral_matrix

if __name__ == '__main__':
    n = int(input())
    matrix = input_matrix(n)
    print("Original matrix: ")
    output_matrix(matrix)
    transformed_matrix = transform_into_spiral_matrix_ver2(matrix)
    print("\nTransformed matrix:")
    output_matrix(transformed_matrix)
