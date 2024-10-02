import turtle
import random


def tree(branch_len):
    # Set the thickness of the branch, minimum thickness is 1
    turtle.pensize(max(1, branch_len / 10))  # Thinner branches as length decreases

    if branch_len < 5:  # Base case for very short branches
        turtle.color("green")  # Color for leaves
    else:
        turtle.color("brown")  # Color for branches

    if branch_len > 5:  # Only draw branches if length is sufficient
        turtle.forward(branch_len)  # Draw the branch

        # Random angle between 15 and 45 degrees for the right branch
        right_angle = random.randint(15, 45)
        turtle.right(right_angle)  # Turn right

        # Random subtraction for the branch length
        next_branch_len = branch_len - random.randint(10, 20)
        tree(next_branch_len)  # Recursive call for the right branch

        # Turn left with the same angle to draw the left branch
        turtle.left(right_angle * 2)  # Turn left

        tree(next_branch_len)  # Recursive call for the left branch

        # Restore the original orientation
        turtle.right(right_angle)  # Return to original right angle
        turtle.backward(branch_len)  # Go back to the trunk


# Setup the turtle environment
turtle.left(90)  # Start with the trunk pointing up
turtle.speed(0)  # Fastest drawing speed
turtle.color("brown")  # Initial color for the trunk
tree(100)  # Initial call to draw the tree
turtle.exitonclick()  # Wait for user to click to exit
