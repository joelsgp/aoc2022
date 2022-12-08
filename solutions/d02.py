from enum import IntEnum


class Choice(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    LOSE = 0
    DRAW = 3
    WIN = 6


MAPPING_OPPONENT = {
    'A': Choice.ROCK,
    'B': Choice.PAPER,
    'C': Choice.SCISSORS
}
MAPPING_OUTCOME = {
    'X': Outcome.LOSE,
    'Y': Outcome.DRAW,
    'Z': Outcome.WIN
}
LOSING_PAIRS = (
    # (lose, win)
    (Choice.ROCK, Choice.PAPER),
    (Choice.PAPER, Choice.SCISSORS),
    (Choice.SCISSORS, Choice.ROCK)
)


def get_your_move(opponent: Choice, outcome: Outcome) -> Choice:
    if outcome == Outcome.DRAW:
        return opponent
    if outcome == Outcome.WIN:
        for lose, win in LOSING_PAIRS:
            if lose == opponent:
                return win
    if outcome == Outcome.LOSE:
        for lose, win in LOSING_PAIRS:
            if win == opponent:
                return lose


def get_round_score(opponent: Choice, outcome: Outcome) -> int:
    you = get_your_move(opponent, outcome)
    return you + outcome


def parse_line(li: str) -> tuple[Choice, Outcome]:
    both = li.split()
    you = MAPPING_OPPONENT[both[0]]
    opponent = MAPPING_OUTCOME[both[1]]

    return you, opponent


def solve(lines):
    total = 0
    for li in lines:
        opponent, outcome = parse_line(li)
        round_score = get_round_score(opponent, outcome)
        total += round_score

    return total
