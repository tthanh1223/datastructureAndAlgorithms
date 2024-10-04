from ADT_abstract_data_type.stack import Stack
def check_bar(symbol_string):
    stack = Stack()
    balance = True
    index = 0
    while index < len(symbol_string) and balance:
        symbol = symbol_string[index]
        if symbol == '(':
            stack.push(symbol)
        else:
            if stack.is_empty():
                balance = False
            else:
                stack.pop()
        index += 1

    if balance and stack.is_empty():
        return True
    else:
        return False


def matches(top, symbol):
    opens = '([{'
    closes = ')}]'
    return opens.index(top) == closes.index(symbol)

def check_bar_general(symbol_string):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbol_string) and balance:
        symbol = symbol_string[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and s.is_empty():
        return True
    else:
        return False

# Test the function
print(check_bar_general('{{([][])}()}'))  # Should print True