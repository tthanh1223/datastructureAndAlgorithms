#10. subset sum problem
def subset_sum(arr: list[int], target: int):
    res = []
    for i in range(1 << len(arr)):  # shift operator 1 >> n : multiple 2 but n times
        subset_sum = 0
        # For each bit in the binary number, check if the corresponding element is in the subset
        for j in range(len(arr)):
            if i & (1 << j):  # Check if the j-th bit is set
                subset_sum += arr[j]
        res.append(subset_sum)
    return target in res

#11. String matching
# Given two strings, check if the second string appears as a substring within the first string.
def check_substring(s1: str, s2: str) -> bool:
    for i in range(len(s1)):
        if s1[i:i+len(s2)] == s2: return True
    return False

#12. Find the closest pair of points
# Given an array of points on a 2D plane, find the pair of points that are closest to each other.
def calculate_distance(point1: tuple[int, int], point2: tuple[int, int]):
    return (abs(point1[0] - point2[0])**2 + abs(point1[1] - point2[1])**2)**1/2
def find_closest_pair(arr: list[tuple[int,int]]) -> tuple[int, int]:
    min_distance = float('inf')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if calculate_distance(arr[i], arr[j]) < min_distance:
                min_distance = calculate_distance(arr[i], arr[j])
                p1 = arr[i]
                p2 = arr[j]
    return p1,p2

#13. Find the longest increasing subsequence
# Given an array, find the longest subsequence where each element is greater than the previous one.
#Generate all subsequences:  Use recursion or backtracking to generate all possible subsequences of the array.
#Check for increasing subsequences:  For each subsequence, verify if the elements are in increasing order.
#Track the longest subsequence: Keep a record of the longest subsequence found so far.
def is_increasing(arr: list[int]) -> bool:
    """Check if a subsequence is strictly increasing."""
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True
def generate_subsequences(arr, index, current, subsequences):
    """Generate all subsequences using backtracking."""
    if index == len(arr):
        subsequences.append(current[:])
        return
    # Exclude the current element
    generate_subsequences(arr, index + 1, current, subsequences)
    # Include the current element
    current.append(arr[index])
    generate_subsequences(arr, index + 1, current, subsequences)
    current.pop()
def find_the_longest_subsequence(arr: list[int]) -> int:
    subs = []
    generate_subsequences(arr, 0, arr, subs)
    longest = []
    for sub in subs:
        if is_increasing(sub) and len(sub) > len(longest):
            longest = sub
    return longest
# Time: O(n.2^n)
# Space: O(2^n) va O(n)

# Dynamic Programming: O(n^2)
def longest_increasing_subsequence_dp(arr: list[int]) -> int:
    n = len(arr)
    if n == 0:
        return 0
    dp = [1] * n        # LIS length ending at each index
    prev = [-1] * n     # To reconstruct the LIS
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    max_index = dp.index(max(dp))
    lis = []
    while max_index != -1:
        lis.append(arr[max_index])
        max_index = prev[max_index]
    return lis[::-1]

# Optimized DP with Binary Search (O(n log n))
from bisect import bisect_left


def longest_increasing_subsequence_optimized_with_array(arr):
    sub = []  # Stores the last elements of increasing subsequences
    index_map = []  # Stores indices of elements in 'sub' in the original array
    parent = [-1] * len(arr)  # To reconstruct the LIS
    for i, num in enumerate(arr):
        pos = bisect_left(sub, num)  # Find the position in sub for 'num'
        if pos == len(sub):
            sub.append(num)  # Extend sub
            index_map.append(i)
        else:
            sub[pos] = num  # Replace
            index_map[pos] = i
        # Update the parent array
        if pos > 0:
            parent[i] = index_map[pos - 1]
    # Reconstruct the LIS
    lis = []
    current_index = index_map[-1]
    while current_index != -1:
        lis.append(arr[current_index])
        current_index = parent[current_index]
    return lis[::-1]  # Reverse to get LIS in the correct order

#14. Find all prime numbers up to N
def find_prime_up_to_N(N: int) -> list[int]:
    primes = []
    for num in range(2, N+1):
        is_prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if __name__ == '__main__':
    arr= [123,412,4123,12,543,29,192,492,324]
    print(longest_increasing_subsequence_dp(arr))