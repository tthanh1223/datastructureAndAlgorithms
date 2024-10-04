def arrayRankTransform(arr: list[int]) -> list[int]:
    # sort the arr and then return the rank of it to the hash map then get the key in the hash map but we need to keep the rank at the same position of the number in the lists
    # không thể vừa pass qua list vừa xác định rank được
    # no linear time
    # O(n log n ) or n ^ 2 is the best.
    # sort the list then give the list the order of it in the new list.
    # khong handle trường hợp có cái element bằng nhau
    # dùng hashmap là tuyệt nhất nhưng vẫn phải sorted cái này
    sorted_unique = sorted(set(arr))
    rank_map = {num:rank+1 for rank,num in enumerate(sorted_unique)}
    return [rank_map[num] for num in arr]

arr = [40,10,20,30,30]
print(arrayRankTransform(arr))

