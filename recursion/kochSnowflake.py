import turtle


def koch_curve(t: turtle.Turtle, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)


def koch_snowflake(t: turtle.Turtle, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)


def main():
    # Set up turtle screen
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.tracer(0)
    # Create turtle
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.hideturtle()
    my_turtle.penup()
    my_turtle.goto(-200, 100)  # Adjust starting position
    my_turtle.pendown()

    # Get the level of recursion from the user
    level = int(input("Enter the level of the Koch snowflake (e.g., 3 or 4): "))
    length = 400  # Length of one side of the initial equilateral triangle

    # Draw the Koch snowflake
    koch_snowflake(my_turtle, length, level)
    screen.update()
    # Close the window on click
    screen.exitonclick()


if __name__ == '__main__':
    main()
