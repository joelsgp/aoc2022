from __future__ import annotations

import re
from typing import Callable


Operation = Callable[[int], int]


ROUNDS = 10_000
POST_INSPECTION_DIVISOR = 1


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
        self.inspections = 0

        self.num = num
        self.held = starting
        self.operation = operation
        self.divisor = divisor
        self.target_true = target_true
        self.target_false = target_false

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.num < other.num

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.num == other.num

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
            int(m['num']),
            starting, cls.get_operation(m),
            int(m['div']), int(m['tt']), int(m['tf'])
        )
        return instance

    def get_target(self, item: int) -> int:
        if item % self.divisor == 0:
            return self.target_true
        else:
            return self.target_false


def solve(lines):
    monkeys = []
    monkey_lines = []
    lines.append('')
    for li in lines:
        if not li:
            new_monkey = Monkey.new(monkey_lines)
            monkeys.append(new_monkey)
            monkey_lines = []
        else:
            monkey_lines.append(li)

    for _ in range(ROUNDS):
        for m in monkeys:
            new_held = []
            for item in m.held:
                item = m.operation(item)
                m.inspections += 1
                item = item // POST_INSPECTION_DIVISOR
                target = m.get_target(item)
                if target == m.num:
                    new_held.append(item)
                else:
                    monkeys[target].held.append(item)
            m.held = new_held

    inspections = [m.inspections for m in monkeys]
    inspections.sort(reverse=True)
    monkey_business = inspections[0] * inspections[1]

    return monkey_business
