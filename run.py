from argparse import ArgumentParser
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable
from sys import stderr

try:
    import pyperclip
except ImportError:
    pyperclip = None


INPUTS_DIR_NAME = 'inputs'
INPUT_SUFFIX = '.txt'
# when problems are released, relative to UTC
RELEASE_OFFSET = timedelta(hours=-3)
RELEASE_TZ = timezone(RELEASE_OFFSET)

Lines = list[str]


def get_parser() -> ArgumentParser:
    parser = ArgumentParser()

    parser.add_argument('day', type=int, nargs='?')
    parser.add_argument('-c', '--copy', action='store_false', help='Copy solution to clipboard')

    return parser


def load_lines(filename: str) -> Lines:
    """Note: uses str.splitlines."""
    inputs_dir = Path(INPUTS_DIR_NAME)
    filepath = inputs_dir / filename
    filepath = filepath.with_suffix(INPUT_SUFFIX)
    text = filepath.read_text(encoding='utf-8')
    lines = text.splitlines()

    return lines


def current_day() -> int:
    now = datetime.now(tz=RELEASE_TZ)
    day = now.day
    return day


def retrieve_solver(filename: str) -> Callable:
    try:
        solutions = __import__(f'solutions.{filename}')
    except ImportError as error:
        raise ValueError(f"Solution {filename} doesn't exist!") from error
    module = getattr(solutions, filename)

    return module.solve


def format_filename(day: int) -> str:
    return f'{day:02}'


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.day is None:
        args.day = current_day()
    filename = format_filename(args.day)

    solve = retrieve_solver(filename)
    lines = load_lines(filename)

    solution = solve(lines)

    if args.copy:
        if pyperclip is None:
            print("pyperclip isn't installed, won't copy solution", file=stderr)
        else:
            pyperclip.copy(solution)
    print(solution)


if __name__ == '__main__':
    main()
