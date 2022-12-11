from __future__ import annotations

from re import compile
from typing import Callable


class Monkey:
    re_block = compile(
        r"""Monkey (P<num>\d+):
 {2}Starting items: (P<repeat>(\d+), )*(P<final>\d+)
 {2}Operation: new = old (P<op>\+|\*) (P<c>\d+)
 {2}Test: divisible by (P<div>\d+)
 {4}If true: throw to monkey (P<tt>\d+)
 {4}If false: throw to monkey (P<tf>\d+)"""
    )

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

        starting = m['repeat'] + [m['final']]
        op = m['op']
        c = m['c']
        if op == '+':
            operation = lambda x: x + c
        elif op == '*':
            operation = lambda x: x * c

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
