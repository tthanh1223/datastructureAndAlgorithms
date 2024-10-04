import stack
from ADT_abstract_data_type.stack import Stack
from infix_to_postfix import do_math
PRECEDENCE = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4}
def process_operator(operators_stack:Stack, operands_stack:Stack) -> None:
    """Pops the operator from the operators_stack and applies
    it to the top two operands.
    Push the result back to the operands_stack"""
    operator = operators_stack.pop()
    operand_2 = operands_stack.pop()
    operand_1 = operands_stack.pop()
    result = do_math(operator, operand_1, operand_2)
    operands_stack.push(result)

def preprocess_expression(expr: str) -> str:
    """Adds spaces around operators and parentheses in an expression."""
    operators = set('+-*/^()')
    processed = []

    for char in expr:
        if char in operators:
            processed.append(f' {char} ')
        else:
            processed.append(char)

    return ''.join(processed).strip()


def infix_evaluate(infix_expression:str):
    """Calculate infix expression like a casio one"""
    if not infix_expression:
        raise ValueError("infix_expression cannot be empty")
    infix_expression = preprocess_expression(infix_expression)
    right_associative = {'^'}
    operators_stack = stack.Stack()
    operands_stack = stack.Stack()

    token_list = infix_expression.split()
    open_parenthesis_count = 0

    for token in token_list:
        if token.isdigit(): #numbers
            operands_stack.push(int(token))

        elif token == '(': #Open parenthesis
            operators_stack.push(token)
            open_parenthesis_count += 1

        elif token == ')': #Close parenthesis
            if open_parenthesis_count == 0:
                raise ValueError("Unmatched parentheses")
            while not operators_stack.is_empty() and operators_stack.peek() != '(':
                process_operator(operators_stack, operands_stack)
            operators_stack.pop() # Remove '(' from the stack
            open_parenthesis_count -= 1

        elif token in PRECEDENCE:
            while (not operators_stack.is_empty() and operators_stack.peek() != '(' and
                   (PRECEDENCE[operators_stack.peek()] > PRECEDENCE[token] or
                    (PRECEDENCE[operators_stack.peek()] == PRECEDENCE[token]
                     and token not in right_associative))):
                process_operator(operators_stack, operands_stack)
            operators_stack.push(token)

        else:
            raise ValueError(f"Invalid character {token} in expression.")

    #Process remaining operators
    while not operators_stack.is_empty():
        if operators_stack.peek() == '(':
            raise ValueError("Unmatched parentheses")
        process_operator(operators_stack, operands_stack)

    # The final result should be the only value on the operands stack
    if operands_stack.size() != 1:
        raise ValueError("Invalid infix expression: Too many operands left")

    return operands_stack.pop()


if __name__ == '__main__':
    infix_expression_1 = '( 3 + 5 * ( 2 - 8 ) ) / 4 + ( 6 / 3 ) ^ 2 - ( ( 4 * 5 ) + ( 10 - 2 ) / ( 3 + 1 ) ) + 7 * ( 8 + ( 5 - 2 ) * 3 ) - ( 12 / 3 + 2 ) * ( 3 ^ 2 - 1 ) + ( 9 * 5 - ( 7 + 2 ) * 4 / 2 ) ^ 2 - 10'
    infix_expression_2 = '5*3 - 3 ^ ( 9 - 2 )'
    try :
        print(infix_evaluate(infix_expression_1))
        print(infix_evaluate(infix_expression_2))
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

