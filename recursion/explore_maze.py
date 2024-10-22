import turtle
from typing import List, Optional
import os


class MazeCell:
    PART_OF_PATH = 'O'
    TRIED = '.'
    OBSTACLE = '+'
    DEAD_END = '-'
    START = 'S'
    EMPTY = ' '


class Maze:
    def __init__(self, maze_file_name: str):
        self.maze_list: List[List[str]] = []
        self.rows_in_maze = 0
        self.cols_in_maze = 0
        self.start_row = 0
        self.start_col = 0
        self.screen = None
        self.t = None

        # Load and validate maze file
        self._load_maze(maze_file_name)
        self._setup_graphics()

    def _load_maze(self, maze_file_name: str) -> None:
        """Safely load and validate maze file."""
        if not os.path.exists(maze_file_name):
            raise FileNotFoundError(f"Maze file {maze_file_name} not found")

        with open(maze_file_name, 'r') as maze_file:
            for line in maze_file:
                row = list(line.strip())  # Remove newline and convert to list
                if not row:  # Skip empty lines
                    continue

                # Validate characters
                for ch in row:
                    if ch not in [MazeCell.OBSTACLE, MazeCell.EMPTY, MazeCell.START]:
                        raise ValueError(f"Invalid character '{ch}' in maze file")

                if MazeCell.START in row:
                    self.start_row = self.rows_in_maze
                    self.start_col = row.index(MazeCell.START)

                self.maze_list.append(row)
                self.rows_in_maze += 1

        if not self.maze_list:
            raise ValueError("Maze file is empty")

        self.cols_in_maze = len(self.maze_list[0])

        # Validate maze dimensions
        if not all(len(row) == self.cols_in_maze for row in self.maze_list):
            raise ValueError("Maze rows have inconsistent lengths")

    def _setup_graphics(self) -> None:
        """Initialize the turtle graphics system."""
        self.screen = turtle.Screen()
        self.screen.title("Maze Solver")
        self.screen.setup(width=600, height=600)

        # Calculate coordinate system
        self.x_translate = -self.cols_in_maze / 2
        self.y_translate = self.rows_in_maze / 2

        # Set up the coordinate system
        margin = 1.0  # Add margin around maze
        self.screen.setworldcoordinates(
            self.x_translate - margin,
            -self.y_translate - margin,
            -self.x_translate + margin,
            self.y_translate + margin
        )

        # Create and configure turtle
        self.t = turtle.Turtle(shape='turtle')
        self.t.speed(0)  # Fastest speed
        self.screen.tracer(0)  # Turn off animation for faster drawing

    def draw_maze(self) -> None:
        """Draw the maze with improved visuals."""
        for y in range(self.rows_in_maze):
            for x in range(self.cols_in_maze):
                if self.maze_list[y][x] == MazeCell.OBSTACLE:
                    self._draw_cell(x, y, 'gray20')
                elif self.maze_list[y][x] == MazeCell.START:
                    self._draw_cell(x, y, 'green')

        self.t.color('black', 'blue')
        self.screen.update()

    def _draw_cell(self, x: int, y: int, color: str) -> None:
        """Draw a single cell of the maze."""
        self.t.up()
        screen_x = x + self.x_translate
        screen_y = -y + self.y_translate
        self.t.goto(screen_x - 0.5, screen_y - 0.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x: int, y: int) -> None:
        """Move the turtle to a new position."""
        self.t.up()
        screen_x = x + self.x_translate
        screen_y = -y + self.y_translate
        self.t.goto(screen_x, screen_y)
        self.screen.update()

    def drop_bread_crumb(self, color: str) -> None:
        """Mark the current position with a colored dot."""
        self.t.dot(10, color)
        self.screen.update()

    def update_position(self, row: int, col: int, val: Optional[str] = None) -> None:
        """Update the maze state and visual representation."""
        if not (0 <= row < self.rows_in_maze and 0 <= col < self.cols_in_maze):
            return  # Ignore invalid positions

        if val:
            self.maze_list[row][col] = val

        self.move_turtle(col, row)

        color_map = {
            MazeCell.PART_OF_PATH: 'light green',
            MazeCell.TRIED: 'gray70',
            MazeCell.DEAD_END: 'red',
            None: 'gray50'
        }

        color = color_map.get(val, 'black')
        self.drop_bread_crumb(color)

    def is_exit(self, row: int, col: int) -> bool:
        """Check if the given position is an exit."""
        return (row == 0 or row == self.rows_in_maze - 1 or
                col == 0 or col == self.cols_in_maze - 1)

    def __getitem__(self, idx):
        return self.maze_list[idx]


def search_from(maze: Maze, start_row: int, start_col: int) -> bool:
    """Search for a path through the maze using recursive backtracking."""
    # Check bounds
    if not (0 <= start_row < maze.rows_in_maze and 0 <= start_col < maze.cols_in_maze):
        return False

    maze.update_position(start_row, start_col)

    # Base cases
    if maze[start_row][start_col] == MazeCell.OBSTACLE:
        return False
    if maze[start_row][start_col] == MazeCell.TRIED:
        return False
    if maze.is_exit(start_row, start_col):
        maze.update_position(start_row, start_col, MazeCell.PART_OF_PATH)
        return True

    maze.update_position(start_row, start_col, MazeCell.TRIED)

    # Try each direction
    directions = [
        (start_row - 1, start_col),  # up
        (start_row + 1, start_col),  # down
        (start_row, start_col - 1),  # left
        (start_row, start_col + 1)  # right
    ]

    for next_row, next_col in directions:
        if search_from(maze, next_row, next_col):
            maze.update_position(start_row, start_col, MazeCell.PART_OF_PATH)
            return True

    maze.update_position(start_row, start_col, MazeCell.DEAD_END)
    return False


def main():
    try:
        my_maze = Maze('maze2.txt')
        my_maze.draw_maze()
        my_maze.update_position(my_maze.start_row, my_maze.start_col)

        if search_from(my_maze, my_maze.start_row, my_maze.start_col):
            print("Path found!")
        else:
            print("No path exists!")

        turtle.done()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()