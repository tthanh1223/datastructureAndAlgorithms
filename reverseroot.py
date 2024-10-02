import sys
import math


def main():
    # Read the entire input stream
    input_data = sys.stdin.read()

    # Split the input by whitespace (spaces, newlines, etc.)
    numbers = input_data.split()

    # Convert each item to an integer
    numbers = [int(num) for num in numbers]

    # Reverse the list
    numbers.reverse()

    # Calculate the square root for each number and print the result
    for num in numbers:
        sqrt_value = math.sqrt(num)
        print(f"{sqrt_value:.4f}")


if __name__ == "__main__":
    main()
