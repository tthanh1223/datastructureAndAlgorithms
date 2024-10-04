def selection_sort(arrange:list[int]):
    for fill_slot in range(len(arrange) - 1, 0, -1):
        pos_of_max = 0
        #find the highest in the remain list
        for location in range(1,fill_slot+1):
            if arrange[location] > arrange[pos_of_max]:
                pos_of_max = location
        #exchange the position
        arrange[fill_slot], arrange[pos_of_max] = arrange[pos_of_max] , arrange[fill_slot]

arr = [54,26,91,17,11,31,33,44,55,20]
selection_sort(arr)
print(arr)