def nextGreatestLetter(letters: list[str], target: str):
    left ,right = 0, len(letters)-1
    if target >= letters[right]:
        return letters[0]
    while left < right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else: right = mid
    print(letters[left])
    print(letters[right])
    return letters[left]
# this is O(n) we need to optimize to O( log n)
lst = ['c','f','f','j']
target = 'c'
print(nextGreatestLetter(lst, target))