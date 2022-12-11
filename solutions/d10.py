from re import compile


RE_NOOP = r'(noop)'
RE_ADDX = r'(addx) (-?\d+)'
# todo: fix
RE_LINE = compile(f'{RE_NOOP}|{RE_ADDX}')
CYCLES = {
    'noop': 1,
    'addx': 2,
}
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
        m = RE_LINE.fullmatch(li)
        op = m[1]
        for _ in range(CYCLES[op]):
            clock += 1
            tick(clock, x, framebuffer)

        if op == 'noop':
            pass
        elif op == 'addx':
            v = int(m[2])
            x += v

    frame = draw(framebuffer)
    return frame
