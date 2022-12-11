from __future__ import annotations

import re
from typing import Callable


Operation = Callable[[int], int]


class Monkey:
    re_block = re.compile(
        r"Monkey (?P<num>\d+):\n"
        r" {2}Starting items: (?P<starting>(\d+, )*\d+)\n"
        r" {2}Operation: new = old (?P<op>[+*]) (?P<c>\d+|old)\n"
        r" {2}Test: divisible by (?P<div>\d+)\n"
        r" {4}If true: throw to monkey (?P<tt>\d+)\n"
        r" {4}If false: throw to monkey (?P<tf>\d+)"
    )
    ops = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
    }

    def __init__(
            self, num: int,
            starting: list[int], operation: Operation,
            divisor: int, target_true: int, target_false: int
    ):
        self.num = num
        self.held = starting
        self.operation = operation
        self.divisor = divisor
        self.target_true = target_true
        self.target_false = target_false

    @classmethod
    def get_operation(cls, m: re.Match) -> Operation:
        op = cls.ops[m['op']]
        c = m['c']
        if c == 'old':
            return lambda x: op(x, x)
        else:
            c = int(c)
            return lambda x: op(x, c)

    @classmethod
    def new(cls, lines: list[str]) -> Monkey:
        block = '\n'.join(lines)
        m = cls.re_block.fullmatch(block)

        starting = [int(x) for x in m['starting'].split(', ')]

        instance = cls(
            m['num'],
            starting, cls.get_operation(m),
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
