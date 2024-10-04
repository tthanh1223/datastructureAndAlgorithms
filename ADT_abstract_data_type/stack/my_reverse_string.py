import stack
def rev_string(string):
    """Use stack to reverse a string"""
    a_stack = stack.Stack()
    for char in string:
        a_stack.push(char)
        print(a_stack)  # This will print the stack state after each push
    new_string = ''
    for _ in range(a_stack.size()):
        new_string += str(a_stack.pop())
    return new_string