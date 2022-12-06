from enum import IntEnum


class Choice(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


MAPPING_YOU = {
    'A': Choice.ROCK,
    'B': Choice.PAPER,
    'C': Choice.SCISSORS,
}
MAPPING_OPPONENT = {
    'X': Choice.ROCK,
    'Y': Choice.PAPER,
    'Z': Choice.SCISSORS,
}


def get_win_score(you: Choice, opponent: Choice) -> int:
    if you == opponent:
        return 3
    elif you == Choice.ROCK and opponent == Choice.PAPER:
        return 0
    elif you == Choice.PAPER and opponent == Choice.SCISSORS:
        return 0
    elif you == Choice.SCISSORS and opponent == Choice.ROCK:
        return 0
    else:
        return 6


def get_match_score(you: Choice, opponent: Choice) -> int:
    win_score = get_win_score(you, opponent)
    return you + win_score


def parse_line(li: str) -> tuple[Choice, Choice]:
    both = li.split()
    you = MAPPING_YOU[both[0]]
    opponent = MAPPING_OPPONENT[both[1]]

    return you, opponent


def solve(lines):
    total = 0
    for li in lines:
        you, opponent = parse_line(li)
        total += get_match_score(you, opponent)

    return total
