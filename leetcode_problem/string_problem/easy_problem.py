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

def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
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


if __name__ == '__main__':
    s = "zabx"
    print(get_lucky(s, 2))
