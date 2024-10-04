# A radix sort for base 10 integers is a mechanical sorting technique
    # that uses a collection of bins, one main bin and 10 digit bins.
# Each bin acts like a "queue" and maintains its "values" in the order that they arrive.
# The algorithm begins by
#   - placing each number in the main bin. Then it considers each value digit by digit.
#   - The first value is removed and placed in a digit bin corresponding to the digit being considered.
#   - For example, if the one's digit is being considered, 534 is placed in digit bin 4 and 667 is placed in digit bin 7.
#   - Once all the values are placed in the corresponding digit bins, the values are collected from bin 0 to bin 9 and placed back in the main bin.
# The process continues with the ten digits, the hundreds, and so on. After the last digit is
# processed, the main bin contains the values in order.
from ADT_abstract_data_type.my_queue import CustomQueue
import random
def counting_sort(nums: list[int], exp):
    """
   Perform counting sort on the input array based on the digit represented by exp.

   Parameters:
   arr (List[int]): The array of integers to sort. This will be modified in place.
   exp (int): The exponent representing the current digit to sort by.
               For example, exp = 1 sorts by the units place,
               exp = 10 sorts by the tens place, and so on.

   Returns:
   None: The function modifies the input array in place to be sorted based on the specified digit.
   """
    # Initialize queues for each digit (0-9)
    queues = [CustomQueue() for _ in range(10)]
    # Enqueue numbers into corresponding queues based on the current digit
    for number in nums:
        index = (number // exp) % 10
        queues[index].enqueue(number)
    #Collect numbers from queues in order
    index = 0
    for queue in queues:
        while not queue.is_empty():
            nums[index] = queue.dequeue()
            index += 1


def radix_sort(nums: list[int]):
    # Find the maximum number to know the number of digits
    max_num = max(nums)
    # Perform counting sort for each digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(nums, exp)
        exp *= 10 # Move to the next digit

if __name__ == '__main__':
    numbers = random.sample(range(10000), 1000)
    print("Original array:", numbers)
    radix_sort(numbers)
    print("Sorted array:", numbers)