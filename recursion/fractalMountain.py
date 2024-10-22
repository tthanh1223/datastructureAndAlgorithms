# find or invent an algorithm for drawing fractal mountain. Use triangular.
import turtle
import random
import math

def draw_mountain(t, x1, y1, x2, y2, displacement, roughness, depth):
    if depth == 0:
        # Draw a straight line when we reach the base case
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)
    else:
        # Calculate the midpoint
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2 + random.uniform(-displacement, displacement)

        # Reduce displacement for finer details
        new_displacement = displacement * roughness

        # Recursively draw the left and right segments
        draw_mountain(t, x1, y1, mid_x, mid_y, new_displacement, roughness, depth - 1)
        draw_mountain(t, mid_x, mid_y, x2, y2, new_displacement, roughness, depth - 1)

# Set up the turtle screen and drawing parameters
def main1():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()
    screen.tracer(0)

    # Initial line endpoints and displacement parameters
    x_start, y_start = -300, 0
    x_end, y_end = 300, 0
    initial_displacement = 100  # Controls initial height of mountains
    roughness = 0.5  # Controls how much displacement decreases with each step (0 < roughness < 1)
    depth = 8  # Depth of recursion (controls the level of detail)

    # Draw the fractal mountain
    draw_mountain(t, x_start, y_start, x_end, y_end, initial_displacement, roughness, depth)

    # Keep the window open until clicked
    screen.update()
    screen.exitonclick()
def main2():
    def random_disp(low, high):
        """Generates a random displacement between low and high."""
        return random.uniform(low, high)

    def subdivide(t, x1, x2, y1, y2, r, disp, epsilon):
        """
        Recursive midpoint displacement for generating a fractal line using Turtle graphics.

        Parameters:
            t (turtle.Turtle): The Turtle instance for drawing.
            x1, y1 (float): Start coordinates of the segment.
            x2, y2 (float): End coordinates of the segment.
            r (float): Roughness parameter (higher values = smoother line).
            disp (float): Initial displacement range.
            epsilon (float): Minimum segment length before stopping recursion.
        """
        if x2 - x1 > epsilon:
            # Calculate the midpoint
            xmid = 0.5 * (x1 + x2)
            ymid = 0.5 * (y1 + y2) + random_disp(-disp, disp)

            # Reduce displacement
            disp *= math.pow(2, -r)

            # Recursively subdivide the left and right halves
            subdivide(t, x1, xmid, y1, ymid, r, disp, epsilon)
            subdivide(t, xmid, x2, ymid, y2, r, disp, epsilon)
        else:
            # Draw a line segment between (x1, y1) and (x2, y2)
            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.goto(x2, y2)

    # Setup for Turtle graphics
    screen = turtle.Screen()
    screen.title('Fractal Mountain Range using Midpoint Displacement')
    screen.setup(width=800, height=600)
    screen.tracer(0)  # Disable automatic updates for faster drawing

    # Create a Turtle instance
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Parameters
    initial_disp = 150  # Initial displacement range
    roughness = 1.2  # Roughness parameter
    epsilon = 5  # Minimum segment length before stopping
    num_lines = 5  # Number of fractal lines to draw

    # Draw multiple fractal lines with varying positions and randomness
    for i in range(num_lines):
        # Vary the starting y-position slightly for each line to create depth
        y_start = -200 + i * 30  # Adjust the vertical spacing between lines
        y_end = y_start + random_disp(-50, 50)  # Randomize the end point for more variation

        # Call the subdivide function with different starting points
        subdivide(t, -300, 300, y_start, y_end, roughness, initial_disp, epsilon)

    # Update the screen to show all drawings at once
    screen.update()

    # Keep the window open until closed by the user
    turtle.done()
if __name__ == '__main__':
    main2()