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

# if use want to handle /* and */ then first we need to set opens and closes to list.
def matches_adv(top, symbol):
    opens = ['(','{','[','/*']
    closes = [')','}',']','*/']
    return opens.index(top) == closes.index(symbol)

def check_bar_adv(symbol_string):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbol_string) and balance:
        symbol = symbol_string[index]
        # Check for multi-char first
        if symbol == '/' and index + 1 < len(symbol_string) and symbol_string[index + 1] == '*':
            s.push('/*')
            index += 1
        elif symbol == '*' and index + 1 < len(symbol_string) and symbol_string[index+1] == '/':
            if s.is_empty() or s.pop() != '/*':
                balance = False
            index += 1

        elif symbol in '({[':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
            else:
                top = s.peek()
                if not matches_adv(top, symbol):
                    balance = False
    if not s.is_empty() and not balance:
        return False
    return True

if __name__ == "__main__":
    s = '24TNT'
    a = list(range(5))
    w = s
    # w =s
    s = a[:3]
    # s = [1,2,3]
    print(s)
    print(w)