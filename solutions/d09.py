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


def count_visited(cache: VisitedCache) -> int:
    return sum(len(v) for v in cache.values())


def snake(h: Coord, t: Coord) -> Coord:
    """Return the new Coord of t."""
    diffx = h[0] - t[0]
    diffy = h[1] - t[1]

    diff_abs = [abs(diffx), abs(diffy)]
    diff_abs.sort()
    # linear
    if diff_abs == [0, 2]:
        t = (t[0] + diffx//2, t[1] + diffy//2)
    # diagonal
    elif diff_abs == [1, 2]:
        t = (t[0] + diffx % 2, t[1] + diffy % 2)

    return t


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
            h = (h[0] + direction[0], h[1] + direction[1])
            t = snake(h, t)
            cache_visited(t, cache)

    visited = count_visited(cache)
    return visited
