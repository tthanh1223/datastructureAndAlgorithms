# find or invent an algorithm for drawing fractal mountain. Use triangular.
import turtle
import random
import math
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

def main2():
    screen = turtle.Screen()
    screen.setup(1000, 1000)
    screen.title("Random Mountain Curves - PythonTurtle.Academy")

    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(2)
    turtle.color('dark green')
    MAX_SLOPE = 45
    MIN_SLOPE = -45
    MIN_HEIGHT = 0
    screen.tracer(0)

    def dist_squared(P1, P2):
        return (P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2

    def mountain(P1, P2):
        if dist_squared(P1, P2) < 9:
            turtle.goto(P2)
            return
        x1, y1 = P1
        x2, y2 = P2
        x3 = random.uniform(x1, x2)
        y3_max = min((x3 - x1) * math.tan(math.radians(MAX_SLOPE)) + y1,
                     (x2 - x3) * math.tan(-math.radians(MIN_SLOPE)) + y2)
        y3_min = max((x3 - x1) * math.tan(math.radians(MIN_SLOPE)) + y1,
                     (x2 - x3) * math.tan(-math.radians(MAX_SLOPE)) + y2)
        y3_min = max(y3_min, MIN_HEIGHT)
        y3 = random.uniform(y3_min, y3_max)
        P3 = (x3, y3)
        mountain(P1, P3)
        mountain(P3, P2)
        return

    turtle.up()

    turtle.goto(-400, MIN_HEIGHT)
    turtle.down()
    mountain((-400, MIN_HEIGHT), (400, MIN_HEIGHT))
    screen.update()
    screen.exitonclick()
if __name__ == '__main__':
    main2()