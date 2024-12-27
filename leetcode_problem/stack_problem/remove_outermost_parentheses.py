# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings,
# and + represents string concatenation.
#
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty,
# and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

def remove_outermost_parentheses(s):
    stack = []
    decomposition = []
    # find all the decomposition
    index = 0

    while index < len(s):
        if s[index] == '(':
            if len(stack) == 0:
                start = index
            stack.append(s[index])
        elif s[index] == ')':
            stack.pop()
            if len(stack) == 0:
                decomposition.append((start, index))
        index += 1
    return "".join([s[pair[0]+1:pair[1]] for pair in decomposition])

def remove_outermost(s):
    answer = ""
    count = 0
    for char in s:
        if char == '(':
            if count > 0:
                answer += char

            count += 1
        else:
            count -= 1
            if count > 0:
                answer += char
    return answer

if __name__ == '__main__':
    s = "(()())(())"
    print(remove_outermost_parentheses(s))