# Modify the Tower of Hanoi program using turtle graphics to animate the movement of the disks.
# Hint: you can make multiple turtles and have them shaped like rectangles
from ADT_abstract_data_type.stack import Stack


from turtle import Turtle, Screen
def move_to(turtle,x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
# Define a class for the Tower of Hanoi with Turtle graphics
class TowerOfHanoiGraphic:
    def __init__(self, num_disks, screen:Screen):
        self.towers = [Stack(),Stack(),Stack()]
        self.screen = screen if screen else Screen()
        self.turtle = Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.num_disks = num_disks
        self.disk_turtles = []

    def draw_the_background(self):
        self.turtle.penup()
        self.turtle.goto(-750, -200)
        color_down = 'light green'
        color_up = 'light blue'
        # Fill the lower part
        self.turtle.fillcolor(color_down)
        self.turtle.begin_fill()
        for _ in range(4):
            if _ % 2 == 0:
                self.turtle.forward(1500)
            else:
                self.turtle.forward(250)
            self.turtle.right(90)
        self.turtle.end_fill()

        # Fill the upper part
        self.turtle.goto(-750, -200)
        self.turtle.fillcolor(color_up)
        self.turtle.begin_fill()
        for _ in range(4):
            if _ % 2 == 0:
                self.turtle.forward(1500)
            else:
                self.turtle.forward(650)
            self.turtle.left(90)
        self.turtle.end_fill()

    def draw_tower1(self):
        rod_height = 400
        rod_width = 10
        base_height = 20
        base_width = 810

        # Draw the base for the towers
        self.turtle.fillcolor('saddlebrown')
        self.turtle.penup()
        self.turtle.goto(-400, -200)
        self.turtle.begin_fill()
        for _ in range(2):
            self.turtle.forward(base_width)
            self.turtle.left(90)
            self.turtle.forward(base_height)
            self.turtle.left(90)
        self.turtle.end_fill()

        # Draw each rod
        rod_positions = [-375, 0, 375]
        for pos in rod_positions:
            self.turtle.fillcolor('saddlebrown')
            self.turtle.penup()
            self.turtle.goto(pos, -200)
            self.turtle.begin_fill()
            self.turtle.forward(rod_width)
            self.turtle.left(90)
            self.turtle.forward(rod_height)
            self.turtle.left(90)
            self.turtle.forward(rod_width)
            self.turtle.left(90)
            self.turtle.forward(rod_height)
            self.turtle.left(90)
            self.turtle.end_fill()
            self.turtle.penup()

    def init_disks(self):
        disk_height = 20
        max_disk_width = 100
        disk_decrement = max_disk_width // self.num_disks

        # Create disk turtles and position them on the first rod
        for i in range(self.num_disks):
            disk_turtle = Turtle()
            disk_turtle.shape('square')
            disk_turtle.color('black', 'orange')  # Black outline, orange fill
            disk_turtle.shapesize(stretch_wid=1, stretch_len=(max_disk_width - i * disk_decrement) / 20)
            disk_turtle.penup()
            disk_turtle.goto(-250, -100 + i * disk_height)  # Start on the first rod
            self.towers[0].push(disk_turtle)  # Add the disk to the first tower's stack
            self.disk_turtles.append(disk_turtle)

    def move_disk(self, from_tower, to_tower):
        disk = self.towers[from_tower].pop()
        target_x = -250 + (to_tower * 250)  # Adjust x-position for target rod
        target_y = -100 + len(self.towers[to_tower].items) * 20

        # Animate the movement
        move_to(disk, disk.xcor(), 150)  # Move up to a height of 150
        move_to(disk, target_x, 150)  # Move horizontally to the destination rod
        move_to(disk, target_x, target_y)  # Move down to the new position on the rod

        # Add the disk to the target tower stack
        self.towers[to_tower].push(disk)

    def solve_hanoi(self, n, from_tower, to_tower, aux_tower):
        if n == 1:
            self.move_disk(from_tower, to_tower)
        else:
            self.solve_hanoi(n - 1, from_tower, aux_tower, to_tower)
            self.move_disk(from_tower, to_tower)
            self.solve_hanoi(n - 1, aux_tower, to_tower, from_tower)
if __name__ == '__main__':
    # Set the number of disks (feel free to change this value)
    window = Screen()
    window.setup(width=1500, height=900)

    # Create the TowerOfHanoiGraphic instance with 3 disks
    num_disks = 10
    hanoi_graphic = TowerOfHanoiGraphic(num_disks=num_disks, screen=window)
    hanoi_graphic.draw_the_background()
    hanoi_graphic.draw_tower1()
    hanoi_graphic.init_disks()
    # Solve the Tower of Hanoi problem with animation
    hanoi_graphic.solve_hanoi(num_disks, 0, 2, 1)

    # Exit when the user clicks on the screen
    window.exitonclick()


