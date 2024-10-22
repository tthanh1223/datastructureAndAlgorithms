import turtle
import random
import math
from typing import Tuple, List


class MountainScape:
    def __init__(self, width: int = 800, height: int = 600):
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.bgcolor("#87CEEB")  # Sky blue
        self.screen.tracer(0)  # Turn off animation for faster drawing

        self.mountain_turtle = turtle.Turtle()
        self.detail_turtle = turtle.Turtle()
        for t in [self.mountain_turtle, self.detail_turtle]:
            t.hideturtle()
            t.speed(0)

        self.width = width
        self.height = height
        self.mountain_points: List[Tuple[float, float]] = []

    def get_color_by_height(self, y: float, max_height: float) -> str:
        """Returns a color based on height for more realistic mountain appearance."""
        # Calculate ratio of height to max height
        ratio = (y + max_height) / (2 * max_height)

        # Define color ranges from snow to rock to grass
        if ratio > 0.8:
            return "#FFFFFF"  # Snow
        elif ratio > 0.6:
            return "#808080"  # Grey rock
        elif ratio > 0.4:
            return "#696969"  # Darker grey
        else:
            return "#4A4A4A"  # Darkest grey

    def draw_mountain(self, t: turtle.Turtle, x1: float, y1: float, x2: float, y2: float,
                      displacement: float, roughness: float, depth: int) -> List[Tuple[float, float]]:
        """Draw a mountain segment and return the points that make up the mountain."""
        points = [(x1, y1)]

        if depth == 0:
            points.append((x2, y2))
        else:
            # Calculate the midpoint with random displacement
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2 + random.uniform(-displacement, displacement)

            # Add some variation to avoid symmetry
            mid_x += random.uniform(-displacement / 4, displacement / 4)

            # Recursively draw both halves
            new_displacement = displacement * roughness
            points.extend(self.draw_mountain(t, x1, y1, mid_x, mid_y, new_displacement, roughness, depth - 1)[1:])
            points.extend(self.draw_mountain(t, mid_x, mid_y, x2, y2, new_displacement, roughness, depth - 1)[1:])

        return points

    def fill_mountain(self, points: List[Tuple[float, float]], max_height: float):
        """Fill the mountain with color gradient based on height."""
        t = self.mountain_turtle

        # Draw the mountain with gradient coloring
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            # Fill triangle between current segment and bottom
            color = self.get_color_by_height(max(y1, y2), max_height)
            t.fillcolor(color)
            t.pencolor(color)

            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.begin_fill()
            t.goto(x2, y2)
            t.goto(x2, -self.height / 2)
            t.goto(x1, -self.height / 2)
            t.goto(x1, y1)
            t.end_fill()

    def add_details(self):
        """Add ground details like trees and rocks."""
        t = self.detail_turtle

        # Add trees
        for _ in range(20):
            x = random.uniform(-self.width / 2 + 50, self.width / 2 - 50)
            size = random.uniform(20, 40)

            # Find the mountain height at this x position
            y = -self.height / 2  # Ground level
            for i in range(len(self.mountain_points) - 1):
                x1, y1 = self.mountain_points[i]
                x2, y2 = self.mountain_points[i + 1]
                if x1 <= x <= x2:
                    # Calculate height at this x using linear interpolation
                    ratio = (x - x1) / (x2 - x1)
                    y = y1 + ratio * (y2 - y1)
                    break

            if y < -self.height / 4:  # Only draw trees below certain height
                self.draw_tree(t, x, y, size)

    def draw_tree(self, t: turtle.Turtle, x: float, y: float, size: float):
        """Draw a simple pine tree."""
        t.penup()
        t.goto(x, y)
        t.pendown()

        # Draw trunk
        t.pencolor("#4B3621")
        t.fillcolor("#4B3621")
        t.begin_fill()
        t.setheading(90)
        t.forward(size * 0.4)
        t.right(90)
        t.forward(size * 0.1)
        t.right(90)
        t.forward(size * 0.4)
        t.right(90)
        t.forward(size * 0.1)
        t.end_fill()

        # Draw triangular tree top
        t.penup()
        t.goto(x - size / 2, y + size * 0.3)
        t.pendown()
        t.pencolor("#228B22")
        t.fillcolor("#228B22")

        for _ in range(3):  # Draw 3 layers of triangles
            t.begin_fill()
            for _ in range(3):
                t.forward(size)
                t.left(120)
            t.end_fill()
            # Move up for next triangle
            t.penup()
            t.goto(x - size / 2.5, t.ycor() + size * 0.3)
            size *= 0.8
            t.pendown()

    def create_landscape(self):
        """Generate the complete mountain landscape."""
        # Generate multiple mountain ranges with varying parameters
        ranges = [
            {"displacement": 150, "roughness": 0.5, "depth": 8, "start_y": -100},
            {"displacement": 200, "roughness": 0.6, "depth": 7, "start_y": -150},
            {"displacement": 100, "roughness": 0.4, "depth": 9, "start_y": -200}
        ]

        max_height = -float('inf')
        for range_params in ranges:
            points = self.draw_mountain(
                self.mountain_turtle,
                -self.width / 2, range_params["start_y"],
                self.width / 2, range_params["start_y"],
                range_params["displacement"],
                range_params["roughness"],
                range_params["depth"]
            )
            self.mountain_points.extend(points)
            max_height = max(max_height, max(y for _, y in points))

            self.fill_mountain(points, max_height)

        # Add ground details
        self.add_details()

        # Update the screen
        self.screen.update()

        # Keep the window open
        self.screen.exitonclick()


def main():
    landscape = MountainScape()
    landscape.create_landscape()


if __name__ == '__main__':
    main()