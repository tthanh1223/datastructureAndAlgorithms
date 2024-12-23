# 1.Find the maximum product of two numbers in an array
def max_product(arr: list):
    max_prod = 0
    x1, y1 = 0,0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > max_prod:
                max_prod = arr[i] * arr[j]
                x1, y1 = i, j
    return max_prod, (x1,y1)

# 2.Find the sum of all subsets of an array
def sum_subsets_with_bitwise(arr: list):
    res = []
    for i in range(1 << len(arr)): # shift operator 1 >> n : multiple 2 but n times
        subset_sum = 0
        # For each bit in the binary number, check if the corresponding element is in the subset
        for j in range(len(arr)):
            if i & (1 << j): # Check if the j-th bit is set
                subset_sum += arr[j]
        res.append(subset_sum)
    return res

def sum_subsets_recursive(arr: list):
    def helper(index, current_sum):
        #Base case: If we've considered all elements
        if index == len(arr):
            subsets.append(current_sum)
            return
        # Recursive case: Include or exclude current element
        # Include the current element
        helper(index + 1, current_sum + arr[index])
        # Exclude the current element
        helper(index + 1, current_sum)

    subsets_sum = []
    helper(0, 0)
    return subsets_sum

def sum_subsets_without_bitwise(arr: list):
    subsets = [0]
    for num in arr:
        new_sums = []
        for current_sum in subsets:
            new_sums.append(current_sum + num)
        subsets.extend(new_sums)
    return subsets

#3.Check if a string is a palindrome
#A string is a palindrome if it reads the same forward and backward. Use brute force to check all possible character comparisons.
#Example: Input: "racecar", Output: True
def check_palindrome(string: str):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

#4.Find all pairs in an array with a given sum
def find_pair(arr: list, sum: int):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                pairs.append((arr[i], arr[j]))
    return pairs

#5.Find the first non-repeating character in a string
def find_first_non_repeating(s: str):
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        if count == 1:
            return s[i]
    return None

#6.Count the number of occurrences of each character in a string
def find_occurrences(s: str):
    counts = {}
    for i in range(len(s)):
        counts[s[i]] = counts.get(s[i], 0) + 1
    return counts

#7.Find the length of the longest common prefix in an array of strings
def find_longest_common_prefix(arr: list[str]):
    if not arr:
        return ""

    common_prefix = ''
    for i in range(len(arr[0])):
        char = arr[0][i]
        for string in arr[1:]:
            #If the current character doesn't match or exceed the length of the string
            if i >= len(string) or string[i] != char:
                return common_prefix
        #If all strings have the same character at this position, add it to the prefix
        common_prefix += char
    return common_prefix, len(common_prefix)



if __name__ == '__main__':
    arr = ['flower', 'flawless','fly']
    print(find_longest_common_prefix(arr))