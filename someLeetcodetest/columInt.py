# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
from collections import Counter


def convertTitle(columnNumber:int) -> str:
    result = ''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while columnNumber > 0:
        columnNumber -= 1
        remainder = columnNumber%26
        columnNumber //= 26
        result += letters[remainder]
    return result[::-1]


def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    # Dictionary to map characters from s to t
    map_s_to_t = dict()
    # Keep track of already mapped char in t
    mapped_chars = set()
    for char_s, char_t in zip(s, t):
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t: return False
        else:
            if char_t in mapped_chars:
                return False
            map_s_to_t[char_s] = char_t
            mapped_chars.add(char_t)
    return True

def isAnagram( s1: str, s2: str) -> bool:
    if len(s1) != len(s2): return False
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    return c1 == c2

def isAnagram_v2(s1: str, s2: str) -> bool:
    c1 = Counter(s1)
    c2 = Counter(s2)
    return c1 == c2
if __name__ == '__main__':
     a = isAnagram('rat','cat')
     print(a)