from re import compile


RE_ADDX = compile(r'addx (?P<v>-?\d+)')
CYCLES_NOOP = 1
CYCLES_ADDX = 2
RELEVANT_CYCLES = list(range(20, 260, 40))
SCREEN_WIDTH = 40
SCREEN_SIZE = 240
PIXEL_DARK = ord('.')
PIXEL_LIT = ord('#')


# todo: decode crt output to get string
#       would require asking others for their result to get a full character set?


def tick(clock: int, x: int, framebuffer: bytearray):
    clock -= 1
    pen = clock % SCREEN_WIDTH
    if abs(pen - x) <= 1:
        framebuffer[clock] = PIXEL_LIT


def draw(framebuffer: bytearray) -> str:
    lines = []
    for i in range(0, len(framebuffer), SCREEN_WIDTH):
        li = framebuffer[i: i + SCREEN_WIDTH]
        str_li = li.decode('utf-8')
        lines.append(str_li)
    frame = '\n'.join(lines)
    return frame


def solve(lines):
    framebuffer = bytearray(PIXEL_DARK for _ in range(SCREEN_SIZE))
    x = 1
    clock = 0

    for li in lines:
        if li == 'noop':
            clock += CYCLES_NOOP
            tick(clock, x, framebuffer)
        elif m := RE_ADDX.fullmatch(li):
            v = int(m['v'])
            for _ in range(CYCLES_ADDX):
                clock += 1
                tick(clock, x, framebuffer)
            x += v

    frame = draw(framebuffer)
    return frame
