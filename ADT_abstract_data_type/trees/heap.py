# heap is a complete binary tree that satisfies heap priority.
# but we can apply the function heapify() of the heap to work with array like this

#operation max_heap
def heapify(arr: list,size: int, i: int):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)

def insert(arr: list, element:int):
    arr.append(element)
    current = len(arr) - 1
    while current > 0:
        parent = (current - 1)//2
        if arr[parent] < arr[current]:
            arr[parent], arr[current] = arr[current], arr[parent]
            current = parent
        else:
            break

def delete(arr:list, element: int):
    size = len(arr)
    i = 0
    # tìm index của element
    for i in range(size):
        if arr[i] == element:
            break
    arr[i], arr[-1] = arr[-1], arr[i]
    arr.pop()

    if i < len(arr):
        heapify(arr, len(arr), i)

if __name__ == "__main__":
    arr = []
    insert(arr, 10)
    insert(arr, 2)
    insert(arr, 8)
    insert(arr, 19)
    insert(arr, 22)
    insert(arr, 1)
    insert(arr, 7)
    print("Max-heap array:", arr)
    delete(arr, 22)
    print("Max_heap array:", arr)


