https://adventofcode.com/2022

Input files go in `inputs/` named 01.txt, 02.txt ... 25.txt

Python files go in `solutions/` named 01.py, 02.py ... 25.py.    
Each Python file has to have a function `solve(lines: list[str] -> int`.

Run `run.py` to use em. It's built like this so you don't have to load the file, split the lines and print the solution every time, just make a new file with the same function signature. 

It also copies the solution to the clipboard if pyperclip is installed. If not installed it prints and error message and runs anyway.    
To toggle this functionality see `run.py --help`.

The help also tells you how to pick which solution, by default it picks based on day of the month.
