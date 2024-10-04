from stack import Stack
# Some errors i can handle in this function:
# 1. Unmatch Parentheses :  There may be more opening or closing parentheses.
# 2. Invalid Characters : Input may contain characters that are not valid
# (e.g., special symbols, letters not intended as variables).
# 3. Empty Input
# 4. Consecutive Operators
def infix_to_postfix(infix_expr):
    if not infix_expr:
        raise ValueError("Input is empty")
    # determine with operators need to be done first
    precedence = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '(': 1}
    right_associative = {'^'}  # Right associative operators
    op_stack = Stack()
    # store the equation after the changes
    postfix_list = []
    # make a list for better iterating
    token_list = infix_expr.split()
    # handing unmatch parenthesis by this
    open_parens_count = 0

# 10 + 3 * 5 / ( 16 - 4 )
# 10 3 5 * 16 4 - / +
# op_stack :
    for token in token_list:
        # Check if the token is not the operators if not just append it into the list.
        if token.isalnum():
            postfix_list.append(token)
        # else check is it a left parenthesis then push it in op_stack
        elif token == '(':
            op_stack.push(token)
            open_parens_count += 1
        # if it is a right '(' - take it out the op_stack
        elif token == ')':
            # We will 'handling unmatch parenthesis here'
            if open_parens_count == 0:
                raise ValueError("Unmatched closing parenthesis.")
            # If the op_stack is not empty and the last push wasn't '(' -
                        #   it can be operator or number - or ...)
            while not op_stack.is_empty() and op_stack.peek() != '(':
                postfix_list.append(op_stack.pop())
            op_stack.pop()  # Pop the '('
        elif token in precedence:  # Operator
            # check stack is not empty and rank của cái trước lớn hiện tại hoặc =
            while (not op_stack.is_empty() and
                   (precedence[op_stack.peek()] > precedence[token] or
                    (precedence[op_stack.peek()] == precedence[token]
                     and token not in right_associative))):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
        else:
            raise ValueError(f"Invalid character {token} in expression.")
    # Pop all the operators from the stack
    while not op_stack.is_empty():
        top_token = op_stack.pop()
        if top_token == '(':
            raise ValueError("Unmatched opening parenthesis.")
        postfix_list.append(top_token)

    return ' '.join(postfix_list)  # Return the postfix expression as a string


def postfix_eval(postfix_expr):
    if not postfix_expr:
        raise ValueError("Input is empty")
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token.isdigit():
            operand_stack.push(int(token))
        elif token in ['+','-','*','/','^']:
            if operand_stack.size() < 2: # Check for sufficient operands
                raise ValueError("Insufficient operand.")
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
        #handle invalid operators
        else:
            raise ValueError(f"Invalid character {token} in expression.")
    if operand_stack.size() != 1:  # There should be exactly one result
        raise ValueError("Invalid postfix expression: Too many operands left on stack.")
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


