class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.is_empty() else None  # Added safety for empty stack

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def rev_string(string):
    """Use stack to reverse a string"""
    stack = Stack()
    for char in string:
        stack.push(char)
        print(stack)  # This will print the stack state after each push
    new_string = ''
    for _ in range(stack.size()):
        new_string += str(stack.pop())
    return new_string

if __name__ == '__main__':
    print(rev_string("hello world"))  # Outputs: "dlrow olleh"

    # Avoid shadowing built-in list type
    my_list = [1, 2, 3, 4]
    for i in range(len(my_list)):
        print(my_list.pop())  # Print popped item
        print(my_list)  # Print current list state
