from re import compile


RE_ADDX = compile(r'addx (?P<v>-?\d+)')
RELEVANT_CYCLES = list(range(20, 260, 40))


def signal_strength(clock: int, x: int) -> int:
    if clock in RELEVANT_CYCLES:
        return clock * x
    return 0


def solve(lines):
    total = 0
    x = 1
    clock = 0

    for li in lines:
        if li == 'nop':
            clock += 1
            total += signal_strength(clock, x)
        elif m := RE_ADDX.fullmatch(li):
            v = int(m['v'])
            for _ in range(2):
                clock += 1
                total += signal_strength(clock, x)
            x += v

    return total
