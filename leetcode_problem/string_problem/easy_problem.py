def are_occurrences_equal(s: str) -> bool:
    counts = {}
    for i in s:
        counts[i] = counts.get(i, 0) + 1
    return len(set(counts.values()))==1

def get_lucky(s: str, k: int) -> str:
    def sum_digit(number: str, k: int) -> int:
        if k == 0:
            return int(number)
        num = 0
        for i in number:
            num += int(i)
        return sum_digit(str(num), k - 1)

    checked = ""
    for i in s:
        checked += str(ord(i) - ord('a') + 1)
    return sum_digit(checked, k)

def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    def dfs(node, path, paths):
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            paths.append("->".join(path))
        else:
            dfs(node.left, path, paths)
            dfs(node.right, path, paths)
        path.pop()

    paths = []
    dfs(root, [], paths)
    return paths

def is_subsequence(s: str, t: str) -> bool:
    if len(s) > len(t): return False
    if len(s) == 0: return True
    subsequence = 0
    for i in range(len(t)):
        if subsequence <= len(s) - 1 and s[subsequence] == t[i]:
            subsequence += 1
    return subsequence == len(s)

from collections import Counter
def longest_palindrome(s: str) -> str:
    a = Counter(s)
    longest = 0
    has_odd = False
    for i in a:
        if a[i] % 2 == 0:
            longest += a[i]
        else:
            longest += a[i] - 1
            has_odd = True
    if has_odd:
        longest += 1
    return longest

if __name__ == '__main__':
    s = "zabx"
    print(get_lucky(s, 2))
