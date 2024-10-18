import turtle
import random
import colorsys

def draw_tree(t, branchLen, thickness):
    if branchLen > 5:
        t.pensize(thickness)
        t.forward(branchLen)
        angle = random.uniform(15, 45)  # Random angle between 15 and 45 degrees
        t.right(angle)
        draw_tree(t, branchLen - random.uniform(5, 15), thickness - 1)  # Randomly adjust branch length and thickness
        t.left(2 * angle)
        draw_tree(t, branchLen - random.uniform(5, 15), thickness - 1)  # Randomly adjust branch length and thickness
        t.right(angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.speed(0)  # Set the turtle's drawing speed (0 is fastest)
    turtle.bgcolor("white")  # Background color

    # Move turtle to start drawing position
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    # Draw tree with initial branch length and thickness
    draw_tree(t, 75, 10)

    my_win.exitonclick()

if __name__ == "__main__":
    main()
