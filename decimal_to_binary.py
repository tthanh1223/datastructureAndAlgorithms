from stack import Stack
def convert_to_binary(dec_num):
    s = Stack()
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    binary_string = ''
    while not s.is_empty():
        binary_string += str(s.pop())

    return binary_string

def base_converter(dec_number,base):
    digits = '0123456789ABCDEF'
    rem_stack = Stack()
    while dec_number > 0:
        remainder = dec_number % base
        rem_stack.push(remainder)
        dec_number = dec_number // base

    new_string = ''
    while not rem_stack.is_empty():
        new_string += digits[rem_stack.pop()]
    return new_string

if __name__ == '__main__':
    print(base_converter(22135,10))
    