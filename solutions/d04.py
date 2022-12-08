import re


PAIR = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')


def slice_encompass(x: slice, y: slice) -> bool:
    for a, b in (x, y), (y, x):
        if a.start >= b.start and a.step <= b.stop:
            return True
    return False


def solve(lines):
    total = 0
    for li in lines:
        m = PAIR.fullmatch(li)
        x = slice(int(m[1]), int(m[2]))
        y = slice(int(m[3]), m[4])
        if slice_encompass(x, y):
            total += 1
    return total
