import turtle
import random


def draw_tree(t, branchLen, thickness):
    thickness = max(1, thickness)
    if branchLen > 5:
        t.pensize(thickness)

        # Color gradient from brown to green
        if branchLen > 30:
            t.color("#382710")  # Darker brown for trunk
        elif branchLen > 15:
            t.color("#4B3619")  # Medium brown
        else:
            t.color("#0B4B2D")  # Darker green for small branches

        t.forward(branchLen)

        # Draw leaves at the end of smaller branches
        if branchLen <= 20:
            # Quick draw of leaf cluster using small filled circles
            saved_color = t.color()
            saved_heading = t.heading()
            t.color("#115522", "#115522")  # Dark green
            t.pensize(1)

            # Draw just 2 leaves for better performance
            for _ in range(2):
                t.right(random.uniform(0, 360))
                t.begin_fill()
                t.circle(branchLen / 5)  # Smaller circles for better performance
                t.end_fill()

            t.setheading(saved_heading)
            t.color(saved_color[0])

        angle = random.uniform(15, 45)  # Random angle between 15 and 45 degrees

        # Right branch
        t.right(angle)
        draw_tree(t, branchLen - random.uniform(5, 15), thickness - 1)

        # Left branch (twice the angle to mirror)
        t.left(angle * 2)
        draw_tree(t, branchLen - random.uniform(5, 15), thickness - 1)

        # Return to original angle and position
        t.right(angle)
        t.backward(branchLen)


def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("#87CEEB")  # Light blue sky
    screen.setup(800, 800)
    screen.tracer(0)  # Turn off animation

    # Set up the turtle
    t = turtle.Turtle()
    t.hideturtle()

    # Draw ground
    t.penup()
    t.goto(-400, -200)
    t.pendown()
    t.color("#90EE90")  # Light green
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

    # Position for tree
    t.penup()
    t.goto(0, -200)
    t.left(90)
    t.pendown()

    # Draw the tree
    draw_tree(t, 100, 10)

    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()