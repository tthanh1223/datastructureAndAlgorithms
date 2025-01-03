#Given a 0-indexed string word and a character ch,
# reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.
#For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive).
# The resulting string will be "dcbaefd".
#Return the resulting string.

def reverse_prefix(text: str, target: str):
    if target not in text:
        return text
    indx = text.index(target)
    return text[:indx+1][::-1] + text[indx+1:]

if __name__ == '__main__':
    text = "abcdef"
    print(reverse_prefix(text, target="d"))
    print(reverse_prefix(text, target="e"))