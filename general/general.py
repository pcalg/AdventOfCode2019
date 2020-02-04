from pathlib import Path
from functools import wraps
from time import time


def read_file(file_location, file_name):
    fn = file_location / file_name

    with open(fn) as f:
        content = f.readlines()
    return [c.strip('\n').strip('\t') for c in content]


def get_location(folder):

    p = Path(folder)
    if p.exists():
        return p

    p = Path(f'..\\{folder}')
    if p.exists():
        return p

    # Didn't find the folder
    raise ValueError(f"Can't locate the folder: {folder}.")


def get_location_input_files():
    """
    Input files are either in '..\\puzzles' or in 'puzzles'.
     This depends  on how the code is run (console or run in pycharm).
    """
    return get_location('puzzles')


def read_file_int(file_location, file_name):
    fn = file_location / file_name

    with open(fn) as f:
        content = f.readlines()
    return [int(c.strip('\n').strip('\t')) for c in content]


def save_output(file_location, file_name, lines):
    fn = file_location / file_name
    with open(fn, 'w') as f:
        f.write('\n'.join(lines) + '\n')


def save_grid(fn: Path, ascii_output: str):
    with open(fn, 'w') as f:
        for ch in ascii_output:
            f.write(ch)


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return _time_it
