MARKER_SIZE = 14


def solve(lines):
    buffer = lines.pop()

    last4 = list(buffer[:MARKER_SIZE])
    for i, char in enumerate(buffer[MARKER_SIZE:]):
        if len(set(last4)) == MARKER_SIZE:
            return i + MARKER_SIZE

        last4.pop(0)
        last4.append(char)
