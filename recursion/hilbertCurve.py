import turtle


def hilbert(t: turtle.Turtle, level, angle, step):
    # Input Parameters are numeric
    # Return Value: None
    if level == 0:
        return

    t.right(angle)
    hilbert(t,level - 1, -angle, step)

    t.forward(step)
    t.left(angle)
    hilbert(t,level - 1, angle, step)

    t.forward(step)
    hilbert(t,level - 1, angle, step)

    t.left(angle)
    t.forward(step)
    hilbert(t,level - 1, -angle, step)
    t.right(angle)


def main():
    level = int(input())
    size = 800
    screen = turtle.Screen()
    screen.tracer(0)
    # Create a turtle
    my_turtle = turtle.Turtle()
    my_turtle.hideturtle()
    # Set the speed of drawing
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(-size / 2.0, size / 2.0)
    my_turtle.pendown()

    # For positioning turtle
    hilbert(my_turtle, level, 90,  size / (2 ** level - 1))
    screen.update()
    screen.exitonclick()


if __name__ == '__main__':
    main()