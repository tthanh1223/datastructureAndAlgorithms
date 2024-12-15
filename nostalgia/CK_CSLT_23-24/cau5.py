def co_doi_xung_tam(matrix: list[list[int]]):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[rows - 1- i][cols - 1 - j]:
                return False
    return True

if __name__ == "__main__":
    rows = int(input("Rows: "))
    cols = int(input("Cols: "))
    matrix = []
    for i in range(rows):
        matrix.append(list(map(int, input().split())))
    flag = co_doi_xung_tam(matrix)
    print("Có đối xứng" if flag else "Không đối xứng")