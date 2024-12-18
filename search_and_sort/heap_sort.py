from ADT_abstract_data_type.trees.heap import heapify
def heap_sort(arr: list):
    # heapify sau đó lấy phần tử max - extract rồi heapify lại lấy max .....
    n = len(arr)
    # build a max-heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Swap root (largest element) with the last element
        arr[0], arr[i] = arr[i], arr[0]
        # Rebuild the heap with reduced size
        heapify(arr, i, 0)

# Time Complexity: O(nlog(n))
# Space Complexity: O(1)

if __name__ == "__main__":
    import numpy as np
    arr = np.random.randint(-100000, 10000, 1000000)
    heap_sort(arr)
    print(arr)

