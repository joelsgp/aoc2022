import re
from itertools import permutations


PAIR = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')


def slice_encompass(*s: slice) -> bool:
    return any(a.start >= b.start and a.stop <= b.stop for a, b in permutations(s, 2))


def solve(lines):
    total = 0
    for li in lines:
        m = PAIR.fullmatch(li)
        x = slice(int(m[1]), int(m[2]))
        y = slice(int(m[3]), int(m[4]))
        if slice_encompass(x, y):
            total += 1
    return total
