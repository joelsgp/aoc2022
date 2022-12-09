def solve(lines):
    total_visible = 0

    grid_height = len(lines)
    grid_width = len(lines[0])
    visibility_grid = [[None] * grid_width for _ in range(grid_height)]
    for i in (0, -1):
        visibility_grid[i] = [True] * grid_width
        for row in visibility_grid:
            row[i] = True
    total_visible += grid_height * 2 + grid_width * 2 - 4

    for step in 1, -1:
    for x in range(grid_width):
        for y in range(1, grid_height, 1):


    return total_visible
