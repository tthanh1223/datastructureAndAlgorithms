#Write a function that takes a string as a parameter and returns a new string that is the reverse of
#the old string.
def reverse(my_str):
    #Base case:
    if len(my_str) <= 1:
        return my_str
    return my_str[-1] + reverse(my_str[:-1])
print(reverse("hello safjk tsifjwsjf asf iwfajs ksfkwr iwfsif wwri"))
#Write a function that takes a string as a parameter and returns True if the string is a palindrome,
#False otherwise.
def check_palindrome1(my_str):
    if reverse(my_str) == my_str:
        return True
    return False


def check_palindrome(my_str):
    # Normalize the string: remove spaces and convert to lowercase
    normalized_str = my_str.replace(" ", "").lower()

    # Recursive helper function to check palindrome
    def is_palindrome_recursive(s):
        # Base case: if the string is empty or has one character
        if len(s) <= 1:
            return True
        # Check if the first and last characters are the same
        if s[0] != s[-1]:
            return False
        # Recur with the substring excluding the first and last characters
        return is_palindrome_recursive(s[1:-1])

    return is_palindrome_recursive(normalized_str)

