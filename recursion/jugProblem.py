# solve the problem.
# You have two jugs a 4-gallon jug and a 3-gallon jug.
# Neither of jugs have marking on them.
# There is a pump that can be used
# to fill the jugs with water.
# How can you get exactly 2 gallon of water
# in the 4-gallon jug?
from collections import deque

def water_jug_bfs(target: int):
    # Start with both jugs empty (0, 0)
    queue = deque([(0, 0)])
    visited = {(0, 0)}  # Using set literal for simplicity
    steps = []

    # Define the capacity of each jug
    jug1_capacity = 4
    jug2_capacity = 3

    # BFS loop
    while queue:
        x, y = queue.popleft()

        # If we reach the target amount in the 4-gallon jug, return the sequence of steps
        if x == target:
            steps.append((x, y))
            return steps

        # Possible next states from the current state (x, y)
        possible_states = [
            (jug1_capacity, y),        # Fill the 4-gallon jug
            (x, jug2_capacity),        # Fill the 3-gallon jug
            (0, y),                    # Empty the 4-gallon jug
            (x, 0),                    # Empty the 3-gallon jug
            (max(0, x - (jug2_capacity - y)), min(jug2_capacity, x + y)),  # Pour 4-gallon into 3-gallon
            (min(jug1_capacity, x + y), max(0, y - (jug1_capacity - x)))   # Pour 3-gallon into 4-gallon
        ]

        for state in possible_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                steps.append((x, y, "->", state))

    return "No solution found"

# Set the target to 2 gallons in the 4-gallon jug
solution = water_jug_bfs(2)
for step in solution:
    print(step)