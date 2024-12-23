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

#4.Find all pairs in an array with a given sum:




if __name__ == '__main__':
    string = 'abcbaa'
    print(check_palindrome(string))
