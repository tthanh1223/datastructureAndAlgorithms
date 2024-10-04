from ADT_abstract_data_type.my_queue import Deque
def palindrome(a_string):
    char_deque = Deque()
    for ch in a_string:
        char_deque.add_rear(ch)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False
    return still_equal

print(palindrome("radar"))


