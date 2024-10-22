matrix = [[1, 2, 2, 3],
          [4, 1, 5, 6],
          [7, 123, 8, 9],
          [4, 3, 5, 6]]

n = len(matrix)
# Adjust this value for padding
padding = 5

# Lower triangle
print("Lower Triangle:")
for i in range(0, n):
    for j in range(0, n):
        if j <= i:
            print(str(matrix[i][j]).rjust(padding), end="")
        else:
            print("".rjust(padding), end="")
    print()

# Upper triangle
print("\nUpper Triangle:")
for i in range(0, n):
    for j in range(0, n):
        if j >= i:
            print(str(matrix[i][j]).rjust(padding), end="")
        else:
            print("".rjust(padding), end="")
    print()
