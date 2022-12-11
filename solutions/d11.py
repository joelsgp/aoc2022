from __future__ import annotations

import re
from typing import Callable


class Monkey:
    re_block = re.compile(
        r"""
        Monkey\ (?P<num>\d+):\n
        \ {2}Starting\ items:\ (?P<starting>(\d+,\ )*\d+)\n
        \ {2}Operation:\ new\ =\ old\ (?P<op>[+*])\ (?P<c>\d+|old)\n
        \ {2}Test:\ divisible\ by\ (?P<div>\d+)\n
        \ {4}If\ true:\ throw\ to\ monkey\ (?P<tt>\d+)\n
        \ {4}If\ false:\ throw\ to\ monkey\ (?P<tf>\d+)
        """,
        re.VERBOSE
    )
    ops = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
    }

    def __init__(
            self, num: int,
            starting: list[int], operation: Callable[[int], int],
            divisor: int, target_true: int, target_false: int
    ):
        self.num = num
        self.held = starting
        self.operation = operation
        self.divisor = divisor
        self.target_true = target_true
        self.target_false = target_false

    @classmethod
    def new(cls, lines: list[str]) -> Monkey:
        block = '\n'.join(lines)
        m = cls.re_block.fullmatch(block)

        starting = [int(x) for x in m['starting'].split(', ')]
        op = cls.ops[m['op']]
        c = m['c']
        if c == 'old':
            operation = lambda x: op(x, x)
        else:
            c = int(c)
            operation = lambda x: op(x, c)

        instance = cls(
            m['num'],
            starting, operation,
            m['div'], m['tt'], m['tf']
        )
        return instance


def solve(lines):
    monkeys = []
    monkey_lines = []
    for li in lines:
        if not li:
            new_monkey = Monkey.new(monkey_lines)
            monkeys.append(new_monkey)
            monkey_lines = []
        else:
            monkey_lines.append(li)

    # todo
    return
