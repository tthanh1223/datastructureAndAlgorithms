# Function to check if a state is valid
def is_valid(state, initial_max):
    missionaries, cannibals = state[0], state[1]
    return (0 <= missionaries <= initial_max and 0 <= cannibals <= initial_max and
            (missionaries == 0 or missionaries >= cannibals) and
            (initial_max - missionaries == 0 or initial_max - missionaries >= initial_max - cannibals))

# Recursive function to find the solution
def solve(state: tuple, path: list[tuple], initial_max: int):
    if state == (0, 0, 0):  # Goal state: all on the other side
        return path

    missionaries, cannibals, boat = state

    # Define possible moves based on boat position
    if boat == 1:  # Boat is on the initial side (left)
        possible_moves = [
            (-1, 0, -1),  # One missionary crosses
            (0, -1, -1),  # One cannibal crosses
            (-2, 0, -1),  # Two missionaries cross
            (0, -2, -1),  # Two cannibals cross
            (-1, -1, -1)  # One missionary and one cannibal cross
        ]
    else:  # Boat is on the other side (right)
        possible_moves = [
            (1, 0, 1),  # One missionary returns
            (0, 1, 1),  # One cannibal returns
            (2, 0, 1),  # Two missionaries return
            (0, 2, 1),  # Two cannibals return
            (1, 1, 1)   # One missionary and one cannibal return
        ]

    for move in possible_moves:
        next_state = (missionaries + move[0], cannibals + move[1], boat + move[2])
        if is_valid(next_state, initial_max) and next_state not in path:
            result = solve(next_state, path + [next_state], initial_max)
            if result:
                return result

    return None

# Function to print the solution in a more readable format
def print_solution(solution, initial_max):
    if solution:
        for state in solution:
            left_m, left_c, boat = state
            right_m = initial_max - left_m
            right_c = initial_max - left_c
            if boat == 1:
                print(f"{left_m}, {left_c} boat ............ {right_m}, {right_c}")
            else:
                print(f"{left_m}, {left_c} ............ boat {right_m}, {right_c}")
    else:
        print("No solution found.")

# Main function
if __name__ == '__main__':
    # Initial state: user-defined number of missionaries and cannibals, boat on the left side
    def get_inputs():
        missionaries = int(input("How many missionaries do you want? "))
        cannibals = int(input("How many cannibals do you want? "))
        return missionaries, cannibals

    # Get input from user
    missionaries, cannibals = get_inputs()
    initial_max = max(missionaries, cannibals)
    initial_state = (missionaries, cannibals, 1)

    # Solve the problem
    solution = solve(initial_state, [initial_state], initial_max)

    # Print the solution
    print("Solution found:")
    print_solution(solution, initial_max)
