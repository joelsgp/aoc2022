from enum import IntEnum


class Choice(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


MAPPING_YOU = {
    'A': Choice.ROCK,
    'B': Choice.PAPER,
    'C': Choice.SCISSORS
}
MAPPING_OPPONENT = {
    'X': Choice.ROCK,
    'Y': Choice.PAPER,
    'Z': Choice.SCISSORS
}
LOSING_PAIRS = (
    (Choice.ROCK, Choice.PAPER),
    (Choice.PAPER, Choice.SCISSORS),
    (Choice.SCISSORS, Choice.ROCK)
)


def get_win_score(you: Choice, opponent: Choice) -> int:
    # draw
    if you == opponent:
        return 3

    # lose
    for pair in LOSING_PAIRS:
        if pair == (you, opponent):
            return 0

    # waynerWin
    return 6


def get_round_score(you: Choice, opponent: Choice) -> int:
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
        opponent, you = parse_line(li)
        round_score = get_round_score(you, opponent)
        total += round_score

    return total
