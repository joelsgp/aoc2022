from __future__ import annotations

from re import compile
from typing import Optional


Lines = list[str]

RE_COMMAND_CD = compile(r'\$ cd (.+)')
RE_OUTPUT_DIR = compile('dir (.+)')
RE_OUTPUT_FILE = compile('([0-9]+) (.+)')

TOTAL_MAX_SIZE = 100_000
DISK_SIZE = 70_000_000
SPACE_REQUIRED = 30_000_000


class Node:
    def __init__(self, name: str, parent: Optional[Directory]):
        self.size = 0
        self.name = name
        self.parent = parent
        if self.parent is not None:
            self.parent.children.append(self)


class File(Node):
    def __init__(self, name: str, parent: Directory, size: int):
        super().__init__(name, parent)
        self.size = size

        parent = self.parent
        while parent is not None:
            parent.size += self.size
            parent = parent.parent


class Directory(Node):
    def __init__(self, name: str, parent: Optional[Directory]):
        super().__init__(name, parent)
        self.children: list[Node] = []


def process_cd(name: str, pwd: Directory, root: Directory) -> Directory:
    if name == '/':
        return root
    elif name == '..':
        if pwd.parent is not None:
            return pwd.parent
        else:
            return pwd
    else:
        for n in pwd.children:
            if n.name == name and isinstance(n, Directory):
                return n
        new = Directory(name, pwd)
        return new


def process_ls(output: Lines, pwd: Directory):
    for line in output:
        if m := RE_OUTPUT_DIR.fullmatch(line):
            name = m[1]
            Directory(name, pwd)
        elif m := RE_OUTPUT_FILE.fullmatch(line):
            size = int(m[1])
            name = m[2]
            File(name, pwd, size)


def process_command(command: str, output: Lines, pwd: Directory, root: Directory) -> Directory:
    if command == '$ ls':
        process_ls(output, pwd)
    elif m := RE_COMMAND_CD.fullmatch(command):
        pwd = process_cd(m[1], pwd, root)
    return pwd


def make_tree(lines: Lines) -> Directory:
    root = Directory('', None)
    pwd = root

    command = lines[0]
    output = []
    for li in lines[1:]:
        if li.startswith('$'):
            pwd = process_command(command, output, pwd, root)
            command = li
            output = []
        else:
            output.append(li)

    return root


def get_total(pwd: Directory, minimum: int, maximum: int) -> int:
    if minimum <= pwd.size <= maximum:
        maximum = pwd.size
    for node in pwd.children:
        if isinstance(node, Directory):
            maximum = get_total(node, minimum, maximum)
    return maximum


def solve(lines):
    root = make_tree(lines)
    space_available = DISK_SIZE - root.size
    free_up_needed = SPACE_REQUIRED - space_available
    total = get_total(root, free_up_needed, DISK_SIZE)
    return total
