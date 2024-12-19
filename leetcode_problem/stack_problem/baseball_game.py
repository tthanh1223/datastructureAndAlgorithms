def calPoints(operations: list[str]) -> int:
    stack = []
    for i in operations:
        if i.isnumeric() or i[1:].isnumeric():
            stack.append(int(i))
        elif i == "C":
            stack.pop()
        elif i == "D":
            stack.append(stack[-1] * 2)
        elif i == "+":
            stack.append(stack[-1] + stack[-2])
    return sum(stack)

if __name__ == "__main__":
    operations = ["5","-2","4","C","D","9","+","+"]
    print(calPoints(operations))