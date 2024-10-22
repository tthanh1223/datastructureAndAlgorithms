from ADT_abstract_data_type.stack import Stack
# compute the factorial of a number
def factorial(number:int):
    if number <= 1:
        return 1
    return number*factorial(number-1)
def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [list[-1]] + reverse_list(lst[:-1])

def fibonacci(n: int, memo: list) -> int:
    if memo[n] is not None:  # Check if result is already calculated
        return memo[n]
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)  # Store result in the list
    return memo[n]

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def main_towerHN():
    def move_disk(from_stack, to_stack):
        if from_stack.is_empty():
            print("Error: Trying to move from an empty stack.")
            return
        disk = from_stack.pop()
        to_stack.push(disk)
        print(f"Moved disk {disk} from {from_stack} to {to_stack}")

    def move_tower(height, from_stack, to_stack, aux_stack):
        if height >= 1:
            # Move the top n-1 disks from from_stack to aux_stack
            move_tower(height - 1, from_stack, aux_stack, to_stack)
            # Move the nth disk from from_stack to to_stack
            move_disk(from_stack, to_stack)
            # Move the n-1 disks from aux_stack to to_stack
            move_tower(height - 1, aux_stack, to_stack, from_stack)

    # Initialize the stacks
    A = Stack()
    B = Stack()
    C = Stack()

    # Number of disks
    num_disks = 3

    # Fill the first stack (A) with disks
    for disk in range(num_disks, 0, -1):
        A.push(disk)

    # Solve the Tower of Hanoi
    print(f"Initial Stacks: A: {A}, B: {B}, C: {C}")
    move_tower(num_disks, A, C, B)
    print(f"Final Stacks: A: {A}, B: {B}, C: {C}")

if __name__ == '__main__':
    main_towerHN()