import random

# Generate a large nums2 file
def create_nums2_file(filename, size):
    with open(filename, 'w') as f:
        for _ in range(size):
            f.write(f"{random.randint(1, 10)}\n")  # Random integers between 1 and 10

create_nums2_file('nums2.txt', 50)  # Create a file with 10,000 numbers


def load_nums1():
    # Load nums1 into memory (example)
    return [1, 2, 2, 3,2,1,2,3,4,1,2,3,1,2,3,4]  # Replace with actual loading logic


def process_chunk(chunk, count_map, result):
    # Sort the chunk
    chunk.sort()
    for num in set(chunk):  # Use set to avoid processing duplicates in the chunk
        if num in count_map and count_map[num] > 0:
            occurrences = min(count_map[num], chunk.count(num))  # Count how many times to add
            result.extend([num] * occurrences)  # Add the number based on occurrences
            count_map[num] -= occurrences  # Decrease count for duplicates


def stream_intersection(nums1, nums2_file):
    count_map = {}
    result = []

    # Step 1: Count occurrences of each element in nums1
    for num in nums1:
        count_map[num] = count_map.get(num, 0) + 1

    # Step 2: Read nums2 in chunks and process
    chunk_size = 1000  # Define a suitable chunk size
    with open(nums2_file, 'r') as file:
        while True:
            chunk = []
            # Read a chunk from the file
            for _ in range(chunk_size):
                line = file.readline()
                if not line:
                    break
                chunk.append(int(line.strip()))

            if not chunk:
                break  # End of file

            # Process the chunk
            process_chunk(chunk, count_map, result)

    return result


# Example usage
nums1 = load_nums1()
nums2_file = 'nums2.txt'  # Replace with your actual file path
intersection_result = stream_intersection(nums1, nums2_file)
print(intersection_result)
