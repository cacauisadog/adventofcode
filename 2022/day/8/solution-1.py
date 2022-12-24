def _generate_grid():
    grid = []

    with open("input.txt", "r") as input:
        for line in input:
            sline = [*line.strip()]
            grid.append(sline)

    return grid

grid = _generate_grid()


def _check_up(i, j):
    global grid

    tree = grid[i][j]

    i -= 1
    while i >= 0:
        if grid[i][j] >= tree:
            return False
        i -= 1

    return True


def _check_right(i, j):
    global grid

    tree = grid[i][j]
    line_size = len(grid[i]) 

    j += 1
    while j < line_size:
        if grid[i][j] >= tree:
            return False
        j += 1

    return True


def _check_down(i, j):
    global grid

    tree = grid[i][j]
    column_size = len(grid[i])

    i += 1
    while i < column_size:
        if grid[i][j] >= tree:
            return False
        i += 1

    return True


def _check_left(i, j):
    global grid

    tree = grid[i][j]

    j -= 1
    while j >= 0:
        if grid[i][j] >= tree:
            return False
        j -= 1

    return True

    
def get_outer_trees(grid):
    # the grid is a square, so we just multiply one side by 4 and subtract the 4
    # edges
    return (len(grid[0]) * 4) - 4 


def get_inner_visible_trees(grid):
    visible_trees = 0
    
    for i, row in enumerate(grid):
        row_size = len(row)
        if i == 0 or i == row_size - 1:
            continue

        for j, _ in enumerate(row):
            if j == 0 or j == row_size - 1:
                continue

            # __import__('ipdb').set_trace()
            if _check_up(i, j) or _check_right(i, j) or _check_down(i, j) or _check_left(i, j):
                visible_trees += 1

    return visible_trees

grid = _generate_grid()
outer_trees = get_outer_trees(grid)
inner_visible_trees = get_inner_visible_trees(grid)
# print(grid)
print(f"Number of outer trees: {outer_trees}")
print(f"Number of inner visible trees: {inner_visible_trees}")
print(f"Total visible trees: {outer_trees + inner_visible_trees}")
