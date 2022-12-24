from math import prod


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
    score = 0
    i -= 1
    while i >= 0:
        score += 1
        if grid[i][j] >= tree:
            break
        i -= 1

    return score


def _check_right(i, j):
    global grid

    tree = grid[i][j]
    line_size = len(grid[i]) 
    score = 0
    j += 1
    while j < line_size:
        score += 1
        if grid[i][j] >= tree:
            break
        j += 1

    return score


def _check_down(i, j):
    global grid

    tree = grid[i][j]
    column_size = len(grid[i])
    score = 0
    i += 1
    while i < column_size:
        score += 1
        if grid[i][j] >= tree:
            break
        i += 1

    return score


def _check_left(i, j):
    global grid

    tree = grid[i][j]
    score = 0
    j -= 1
    while j >= 0:
        score += 1
        if grid[i][j] >= tree:
            break
        j -= 1

    return score


def get_highest_scenic_score(grid):
    highest_scenic_score = 0
    
    for i, row in enumerate(grid):
        row_size = len(row)
        if i == 0 or i == row_size - 1:
            continue

        for j, _ in enumerate(row):
            if j == 0 or j == row_size - 1:
                continue

            # __import__('ipdb').set_trace()
            up_score = _check_up(i, j)
            right_score = _check_right(i, j)
            down_score = _check_down(i, j)
            left_score = _check_left(i, j)
            
            total_score = prod([up_score, right_score, down_score, left_score])
            if total_score > highest_scenic_score:
                highest_scenic_score = total_score

    return highest_scenic_score

grid = _generate_grid()
highest_scenic_score = get_highest_scenic_score(grid)
print(highest_scenic_score)
