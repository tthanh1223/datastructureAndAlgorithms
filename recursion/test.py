import turtle
from turtle import Screen, Turtle
from ADT_abstract_data_type.stack import Stack

def move_to(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

class TowerOfHanoiGraphic:
    def __init__(self, num_disks, screen: Screen):
        self.num_disks = num_disks
        self.towers = [Stack(), Stack(), Stack()]
        self.screen = screen if screen else Screen()
        self.disk_turtles = []
        self.turtle = Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.init_disks()

    def draw_the_background(self):
        self.screen.bgcolor('white')
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

    def init_disks(self):
        disk_height = 20
        max_disk_width = 100
        disk_decrement = max_disk_width // self.num_disks

        # Create disk turtles and position them on the first rod
        for i in range(self.num_disks):
            disk_turtle = Turtle()
            disk_turtle.shape('square')
            disk_turtle.shapesize(stretch_wid=1, stretch_len=(max_disk_width - i * disk_decrement) / 20)
            disk_turtle.penup()
            disk_turtle.goto(-100, -100 + i * disk_height)
            self.towers[0].push(disk_turtle)  # Push the disk turtle onto the first tower stack
            self.disk_turtles.append(disk_turtle)

    def move_disk(self, from_tower, to_tower):
        disk = self.towers[from_tower].pop()
        target_x = -100 + (to_tower * 200)  # Calculate the target x position for the destination rod
        target_y = -100 + len(self.towers[to_tower].items) * 20

        # Animate the movement
        move_to(disk, disk.xcor(), 150)  # Move up
        move_to(disk, target_x, 150)     # Move horizontally to the destination rod
        move_to(disk, target_x, target_y)  # Move down

        # Place the disk on the target rod stack
        self.towers[to_tower].push(disk)

    def solve_hanoi(self, n, from_tower, to_tower, aux_tower):
        if n == 1:
            self.move_disk(from_tower, to_tower)
        else:
            self.solve_hanoi(n - 1, from_tower, aux_tower, to_tower)
            self.move_disk(from_tower, to_tower)
            self.solve_hanoi(n - 1, aux_tower, to_tower, from_tower)

if __name__ == '__main__':
    # Set up the screen and number of disks
    window = Screen()
    window.setup(width=1500, height=900)

    # Create the TowerOfHanoiGraphic instance with 3 disks
    num_disks = 3
    hanoi_graphic = TowerOfHanoiGraphic(num_disks=num_disks, screen=window)
    hanoi_graphic.draw_the_background()

    # Solve the Tower of Hanoi problem with animation
    hanoi_graphic.solve_hanoi(num_disks, 0, 2, 1)

    # Exit when the user clicks on the screen
    window.exitonclick()
