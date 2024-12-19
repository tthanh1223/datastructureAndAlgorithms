def makeGood(s: str) -> str:
    # two adjacent characters s[i] and s[i + 1] where:
    # 0 <= i <= s.length - 2
    # s[i] lowercase - s[i+1] == s[i].upper()' and ver-visca
    # we need to remove the string bad - return the result after removing
    # "" is good
    stack = []
    for i in range(len(s)):
        if len(stack) != 0 and abs(ord(s[i]) - ord(stack[-1])) == abs(ord('a')-ord('A')):
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)



if __name__ == "__main__":
    s = "pP"
    print(makeGood(s))