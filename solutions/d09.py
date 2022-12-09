from re import compile


VisitedCache = dict[int, dict[int, bool]]
Coord = tuple[int, int]

RE_STEP = compile(r'([UDLR]) (\d+)')
DIRECTION_VECTORS = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


def cache_visited(t: Coord, cache: VisitedCache):
    cache.setdefault(t[0], {})
    cache[t[0]].setdefault(t[1], True)


# my fav vampire
def count_visited(cache: VisitedCache) -> int:
    return sum(len(v) for v in cache.values())


def add_coords(a: Coord, b: Coord) -> Coord:
    result = (a[0] + b[0], a[1] + b[1])
    return result


def snake(h: Coord, t: Coord) -> Coord:
    """Return the new Coord of t."""
    diffx = h[0] - t[0]
    diffy = h[1] - t[1]

    diff_abs = [abs(diffx), abs(diffy)]
    diff_abs.sort()
    # linear
    if diff_abs == [0, 2]:
        move = (diffx // 2, diffy // 2)
    # diagonal
    elif diff_abs == [1, 2]:
        move = (diffx // abs(diffx), diffy // abs(diffy))
    else:
        move = (0, 0)

    t = add_coords(t, move)
    return t


def draw(h: Coord, t: Coord) -> str:
    start = (0, 0)

    offset_x = -min(start[0], h[0], t[0])
    offset_y = -min(start[1], h[1], t[1])
    offset = (offset_x, offset_y)

    start = add_coords(start, offset)
    h = add_coords(h, offset)
    t = add_coords(t, offset)

    charset = {
        's': start,
        'T': t,
        'H': h,
    }

    width = max(start[0], h[0], t[0])
    height = max(start[1], h[1], t[1])

    grid = [['.'] * (width + 1) for _ in range(height + 1)]
    for char, coord in charset.items():
        grid[coord[1]][coord[0]] = char

    drawn = '\n'.join(''.join(line) for line in grid)
    return drawn


def solve(lines):
    cache = {}

    h = (0, 0)
    t = (0, 0)
    cache_visited(t, cache)

    for step in lines:
        m = RE_STEP.fullmatch(step)
        direction = DIRECTION_VECTORS[m[1]]
        distance = int(m[2])

        for _ in range(distance):
            # print(draw(h, t))
            # print('-----')
            # input()
            h = add_coords(h, direction)
            t = snake(h, t)
            cache_visited(t, cache)

    visited = count_visited(cache)
    return visited
