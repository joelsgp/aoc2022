from itertools import product


def solve(lines):
    total_visible = 0

    grid_height = len(lines)
    grid_width = len(lines[0])

    for x in range(grid_width):
        for y in range(grid_height):
            # for each tree
            current_height = lines[y][x]
            ok = False
            for deltax, deltay in (
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            ):
                # for each line of sight
                searchx = x + deltax
                searchy = y + deltay
                while 0 <= searchx < grid_width and 0 <= searchy < grid_height:
                    search_height = lines[searchy][searchx]
                    if current_height <= search_height:
                        break
                    searchx += deltax
                    searchy += deltay
                else:
                    ok = True

                if ok:
                    total_visible += 1
                    print(x, y)
                    break

    return total_visible
