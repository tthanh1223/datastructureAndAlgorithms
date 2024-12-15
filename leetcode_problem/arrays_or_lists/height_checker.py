from search_and_sort.merge_sort import merge_sort
def height_checker(array):
    merge = array
    merge_sort(merge)
    different = 0
    for k in range(0,len(array)):
        if array[k] != merge[k]:
            different += 1
    return different

array = [1,1,4,2,1,3]
print(height_checker(array))
