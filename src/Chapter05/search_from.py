from maze import Maze


PART_OF_PATH = "0"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"


def search_from(maze: Maze, start_row: int, start_column: int):
    # Try each of four directions from this point until we find a way out.
    maze.update_position(start_row, start_column)
    # Base case return values:
    # 1. We have run into an obstacle, return False
    if maze[start_row][start_column] == OBSTACLE:
        return False
    # 2. We have found a square that has already been explored
    if (
        maze[start_row][start_column] == TRIED or
        maze[start_row][start_column] == DEAD_END
    ):
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True

    maze.update_position(start_row, start_column, TRIED)
    # Otherwise, use logical short circuiting to try
    # each direction in turn (if needed)
    found = (
        search_from(maze, start_row, start_column - 1) or
        search_from(maze, start_row, start_column + 1) or
        search_from(maze, start_row - 1, start_column) or
        search_from(maze, start_row + 1, start_column)
    )
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)

    return found


my_maze = Maze("src/Chapter05/maze2.txt")
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_column)

search_from(my_maze, my_maze.start_row, my_maze.start_column)
