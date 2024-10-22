# find or invent an algorithm for drawing fractal mountain. Use triangular.
import turtle
import random
def draw_mountain(t: turtle.Turtle, x1, y1, x2, y2, displacement, roughness, depth):
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
    initial_displacement = 400  # Controls initial height of mountains
    roughness = 0.5  # Controls how much displacement decreases with each step (0 < roughness < 1)
    depth = 14  # Depth of recursion (controls the level of detail)

    # Draw the fractal mountain
    draw_mountain(t, x_start, y_start, x_end, y_end, initial_displacement, roughness, depth)
    screen.update()
    # Keep the window open until clicked
    screen.exitonclick()
if __name__ == '__main__':
    main1()