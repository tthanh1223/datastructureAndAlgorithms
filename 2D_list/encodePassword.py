# cho tin nhắn "anhyeuemnhieulam" -> chuyển mật mã về dạng với chiều cao = 3
# a u e e u
# n e m i
# h y n h
# -> aueeunemilhynham
#Input: anhyeuemnhieulam, height
#Output: aueeunemilhynham

def encode_password(string, rows):
    length = len(string)
    cols = length // rows if length % rows == 0 else length // rows + 1
    matrix = [["" for _ in range(cols)] for _ in range(rows)]
    #raversal the matrix
    row, col = 0, 0
    for index in range(length):
        matrix[row][col] = string[index]
        if row < rows - 1 and col % 2 == 0:
            row = row + 1
        elif row == rows - 1 and col % 2 == 0:
            col += 1
        elif col % 2 == 1 and row > 0:
            row = row - 1
        elif row == 0 and col % 2 == 1:
            col += 1
    #get the password
    password = ""
    for row in range(rows):
        for col in range(cols):
            password += matrix[row][col]
    return password

def decode_password(password, rows):
    length = len(password)
    cols = length // rows if length % rows == 0 else length // rows + 1
    matrix = [["" for _ in range(cols)] for _ in range(rows)]
    empty_pos = 0 if length % rows == 0 else rows - length % rows
    if cols % 2 == 0:
        index = 0
        for row in range(rows):
            for col in range(cols):
                if col == cols - 1 and empty_pos > 0:
                    empty_pos -= 1
                    continue
                matrix[row][col] = password[index]
                index += 1
    else:
        index = 0
        for row in range(rows):
            for col in range(cols):
                if col == cols - 1 and row >= empty_pos - 1 and empty_pos > 0:
                    continue
                matrix[row][col] = password[index]
                index += 1
    # Traversal in the matrix to get the real message
    row, col = 0, 0
    message = str()
    for index in range(length):
        message += matrix[row][col]
        if row < rows - 1 and col % 2 == 0:
            row += 1
        elif row == rows - 1 and col % 2 == 0:
            col += 1
        elif col % 2 == 1 and row > 0:
            row -= 1
        elif row == 0 and col % 2 == 1:
            col += 1
    return message

if __name__ == '__main__':
    string = "traicamcomaucamngot"
    height = 3
    a = encode_password(string, height)
    print("password: ", a)
    ori = decode_password(a, height)
    print("original message: ", ori)