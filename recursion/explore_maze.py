import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

def search_from(maze, start_row, start_column):
    maze.update_position(start_row, start_column)
    # Check for base cases:
    # 1. We have run into an obstacle, return False.
    if maze[start_row][start_column] == OBSTACLE:
        return False
    # 2. We have found a square that has already been explored.
    if maze[start_row][start_column] == TRIED:
        return False
    # 3. Success, an outside edge not occupied by an obstacle.
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True

    maze.update_position(start_row, start_column, TRIED)

    # Otherwise, use logical short-circuiting to try each direction in turn (if needed)
    found = search_from(maze, start_row - 1, start_column) or \
            search_from(maze, start_row + 1, start_column) or \
            search_from(maze, start_row, start_column - 1) or \
            search_from(maze, start_row, start_column + 1)

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)

    return found

class Maze:
    def __init__(self, maze_file_name):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_file_name, 'r')

        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == "S":
                    self.start_row = rows_in_maze
                    self.start_col = col
                col += 1
            rows_in_maze += 1
            self.maze_list.append(row_list)

        self.rows_in_maze = rows_in_maze
        self.cols_in_maze = len(row_list)
        self.x_translate = -self.cols_in_maze / 2
        self.y_translate = -self.rows_in_maze / 2
        self.t = turtle.Turtle(shape='turtle')
        turtle.setup(width=600, height=600)
        turtle.setworldcoordinates(-(self.cols_in_maze - 1) / 2 - 0.5,
                                   -(self.rows_in_maze - 1) / 2 - 0.5,
                                   (self.cols_in_maze - 1) / 2 + 0.5,
                                   (self.rows_in_maze - 1) / 2 + 0.5)

    def draw_maze(self):
        for y in range(self.rows_in_maze):
            for x in range(self.cols_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate, -y + self.y_translate, 'tan')
        self.t.color('black', 'blue')

    def draw_centered_box(self, x, y, color):
        turtle.tracer(0)
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        turtle.update()
        turtle.tracer(1)

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)
        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = 'black'

        if color:
            self.drop_bread_crumb(color)

    def is_exit(self, row, col):
        return (row == 0 or
                row == self.rows_in_maze - 1 or
                col == 0 or
                col == self.cols_in_maze - 1)

    def __getitem__(self, idx):
        return self.maze_list[idx]

if __name__ == '__main__':
    my_maze = Maze('maze2.txt')
    my_maze.draw_maze()
    my_maze.update_position(my_maze.start_row, my_maze.start_col)

    search_from(my_maze, my_maze.start_row, my_maze.start_col)
    turtle.done()
