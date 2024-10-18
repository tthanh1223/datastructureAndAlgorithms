# compute the factorial of a number
def factorial(number:int):
    if number <= 1:
        return 1
    return number*factorial(number-1)
def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [list[-1]] + reverse_list(lst[:-1])

