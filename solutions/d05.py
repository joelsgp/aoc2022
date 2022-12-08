def parse_input_bounds(lines: list[str]) -> tuple[int, int]:
    stack_count, stack_size = None, None

    for i, li in enumerate(lines):
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
    for li in lines[:stack_size]:
        for i in range(stack_count):
            stack_entry = li[i * 3]
            if stack_entry == ' ':
                continue
            stacks[i].append(ord(stack_entry))

    return stacks


def solve(lines):
    stack_count, stack_size = parse_input_bounds(lines)
    stacks = parse_stacks(stack_count, stack_size, lines)
    print(stacks)
