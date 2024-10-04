import os

from infix_eval import *
def calculator():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print("________________________________")
    print("Welcome to the calculator!")
    print("Type your expression and hit Enter.")
    print("Type 'exit' to quit.")
    print("Type 'clear' to reset.")
    print("________________________________")
    while True:
        expression = input("Enter Expression: ").strip()
        if expression.lower() == "exit":
            print("GOODBYE - SEE YOU LATER!!!! 😊😊😊😊")
            break
        elif expression.lower() == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            print("Input cleared. You're welcome!!!! ❤️❤️❤️❤️")
            continue  # Move to the next iteration
        try:
            result = infix_evaluate(expression)  # Make sure you have this function defined
            print(f"Result: {result}")
        except ValueError as error:
            print(error)
        except ZeroDivisionError as error:
            print(error)

if __name__ == '__main__':
    calculator()