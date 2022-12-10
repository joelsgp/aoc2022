from re import compile


RE_ADDX = compile(r'addx (?P<v>-?\d+)')
CYCLES_NOOP = 1
CYCLES_ADDX = 2
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
        if li == 'noop':
            clock += CYCLES_NOOP
            total += signal_strength(clock, x)
        elif m := RE_ADDX.fullmatch(li):
            v = int(m['v'])
            for _ in range(CYCLES_ADDX):
                clock += 1
                total += signal_strength(clock, x)
            x += v

    return total
