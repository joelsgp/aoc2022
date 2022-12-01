from pathlib import Path
import pyperclip


class Solution:
    input_dir = Path('input')
    input_name = 'input'

    def __init__(self, day: int):
        self.day = day
        self.input_path = self.input_dir / str(self.day) / self.input_name
        with open(self.input_path, encoding='utf-8') as input_file:
            self.input = input_file.read()
        self.input_lines = self.input.splitlines()

    def solution(self) -> str:
        raise NotImplementedError

    def clipboard_copy(self):
        pyperclip.copy(self.solution())
