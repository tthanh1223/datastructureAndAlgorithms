from stack import Stack

def infix_to_postfix(infix_expr):
    precedence = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '(': 1}
    right_associative = {'^'}  # Right associative operators
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()  # Tokenize input

    for token in token_list:
        if token.isalnum():  # Operand
            postfix_list.append(token)
        elif token == '(':  # Left parenthesis
            op_stack.push(token)
        elif token == ')':  # Right parenthesis
            while not op_stack.is_empty() and op_stack.peek() != '(':
                postfix_list.append(op_stack.pop())
            op_stack.pop()  # Pop the '('
        else:  # Operator
            while (not op_stack.is_empty() and
                   (precedence[op_stack.peek()] > precedence[token] or
                    (precedence[op_stack.peek()] == precedence[token] and token not in right_associative))):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    # Pop all the operators from the stack
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return ' '.join(postfix_list)  # Return the postfix expression as a string


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token.isdigit():
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(token, operand1, operand2):
    if token == '+':
        return operand1 + operand2
    elif token == '-':
        return operand1 - operand2
    elif token == '*':
        return operand1 * operand2
    elif token == '/':
        return operand1 / operand2




if __name__ == '__main__':
    print(infix_to_postfix('10 + 3 * 5 / ( 16 - 4 )'))
    print(infix_to_postfix('5 * 3 ^ ( 4 - 2 )'))  # Output: A B * C D * +
    print(infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )'))  # Output: A B + C * D E - F G + * -
    print(postfix_eval('7 8 + 3 2 + /'))
    print(postfix_eval('10 3 5 * 16 4 - / +'))