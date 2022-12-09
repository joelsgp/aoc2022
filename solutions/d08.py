from math import prod


def solve(lines):
    best_score = 0

    grid_height = len(lines)
    grid_width = len(lines[0])

    for x in range(grid_width):
        for y in range(grid_height):
            # for each tree
            current_height = lines[y][x]
            the_scores_four = []
            for deltax, deltay in (
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            ):
                # for each line of sight
                viewing_distance = 1

                searchx = x + deltax
                searchy = y + deltay
                while 0 <= searchx < grid_width and 0 <= searchy < grid_height:
                    search_height = lines[searchy][searchx]
                    if current_height <= search_height:
                        break
                    searchx += deltax
                    searchy += deltay
                    viewing_distance += 1
                the_scores_four.append(viewing_distance)

            current_score = prod(the_scores_four)
            if best_score < current_score:
                best_score = current_score

    return best_score
