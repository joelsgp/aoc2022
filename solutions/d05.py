import re


INSTRUCTION_RE = re.compile(r'move (\d+) from (\d+) to (\d+)')


def parse_input_bounds(lines: list[str]) -> tuple[int, int]:
    stack_count, stack_size = None, None

    for i, li in enumerate(lines):
        # 2 is the offset to the last item in the string
        last_data = li[-2]
        try:
            stack_count = int(last_data)
        except ValueError:
            pass
        else:
            stack_size = i
            break

    if None in (stack_count, stack_size):
        raise RuntimeError('Invalid input.')

    return stack_count, stack_size


def parse_stacks(stack_count: int, stack_size: int, lines: list[str]) -> list[bytearray]:
    stacks = [bytearray() for _ in range(stack_count)]
    for li in reversed(lines[:stack_size]):
        for i in range(stack_count):
            # 4 is the separation between each stack item in the string
            stack_entry = li[1 + 4*i]
            if stack_entry != ' ':
                stacks[i].append(ord(stack_entry))

    return stacks


def get_puzzle_output(stacks: list[bytearray]) -> str:
    out_list = []
    for s in stacks:
        top = s.pop()
        out_list.append(chr(top))

    out = ''.join(out_list)
    return out


def CrateMover9000(num: int, source: int, dest: int, stacks: list[bytearray]):
    for _ in range(num):
        hold = stacks[source - 1].pop()
        stacks[dest - 1].append(hold)


def solve(lines):
    stack_count, stack_size = parse_input_bounds(lines)
    stacks = parse_stacks(stack_count, stack_size, lines)

    for li in lines[stack_size + 2:]:
        m = INSTRUCTION_RE.fullmatch(li)
        num, source, dest = (int(g) for g in m.groups())
        CrateMover9000(num, source, dest, stacks)

    out = get_puzzle_output(stacks)
    return out
