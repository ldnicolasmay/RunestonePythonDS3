import turtle

PART_OF_PATH = "0"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"


class Maze(object):

    def __init__(self, maze_filename):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_filename, "r")
        for line in maze_file:
            row_list = []
            column = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == "S":
                    self.start_row = rows_in_maze
                    self.start_column = column
                column = column + 1
            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)

        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = -columns_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.window = turtle.Screen()
        self.window.setworldcoordinates(
            -(columns_in_maze - 1) / 2 - 0.5,
            -(rows_in_maze - 1) / 2 - 0.5,
            (columns_in_maze - 1) / 2 + 0.5,
            (rows_in_maze - 1) / 2 + 0.5,
        )

    def __getitem__(self, idx):
        return self.maze_list[idx]

    def draw_maze(self):
        self.t.speed(10)
        self.window.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate, -y + self.y_translate, "orange"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.window.update()
        self.window.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, column, val=None):
        if val:
            self.maze_list[row][column] = val
        self.move_turtle(column, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def is_exit(self, row, column):
        return (
            row == 0 or
            row == self.rows_in_maze - 1 or
            column == 0 or
            column == self.columns_in_maze - 1
        )
