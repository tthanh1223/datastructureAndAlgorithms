import time
from unordered_list import UnorderedList  # Assuming your list implementation is in 'unordered_list.py'

def experiment():
    n = 10000  # Number of elements

    # Python list
    py_list = []
    unordered_list = UnorderedList()

    # Insert at beginning
    print("Insert at beginning:")
    start = time.time()
    for i in range(n):
        py_list.insert(0, i)
    end = time.time()
    print(f"Python list: {end - start:.5f} seconds")

    start = time.time()
    for i in range(n):
        unordered_list.add(i)
    end = time.time()
    print(f"UnorderedList: {end - start:.5f} seconds")

    # Insert at the end
    print("\nInsert at end:")
    py_list = []
    unordered_list = UnorderedList()

    start = time.time()
    for i in range(n):
        py_list.append(i)
    end = time.time()
    print(f"Python list: {end - start:.5f} seconds")

    start = time.time()
    for i in range(n):
        unordered_list.append(i)
    end = time.time()
    print(f"UnorderedList: {end - start:.5f} seconds")

    # Access by index
    print("\nAccess by index:")
    start = time.time()
    for i in range(n):
        _ = py_list[i]
    end = time.time()
    print(f"Python list: {end - start:.5f} seconds")

    start = time.time()
    for i in range(n):
        _ = unordered_list[i]
    end = time.time()
    print(f"UnorderedList: {end - start:.5f} seconds")

    # Delete it from the beginning
    print('Delete beginning:')
    start = time.time()
    for i in range(n):
        del py_list[0]
    end = time.time()
    print(f"Python list: {end - start:.5f} seconds")

    start = time.time()
    for i in range(n):
        unordered_list.pop(0)
    end = time.time()
    print(f"UnorderedList: {end - start:.5f} seconds")


if __name__ == "__main__":
    experiment()
