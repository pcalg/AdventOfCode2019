from pathlib import Path


def read_file(file_location, file_name):
    fn = file_location / file_name

    with open(fn) as f:
        content = f.readlines()
    return [c.strip('\n').strip('\t') for c in content]


def get_location_input_files():
    """
    Input files are either in '..\\puzzles' or in 'puzzles'.
     This depends  on how the code is run (console or run in pycharm).
    """
    p = Path('puzzles')
    if p.exists():
        return p

    p = Path('..\\puzzles')
    if p.exists():
        return p

    # Didn't find the inputs
    raise ValueError("Can't locate the input files.")


def read_file_int(file_location, file_name):
    fn = file_location / file_name

    with open(fn) as f:
        content = f.readlines()
    return [int(c.strip('\n').strip('\t')) for c in content]


def save_output(file_location, file_name, lines):
    fn = file_location / file_name
    with open(fn, 'w') as f:
        f.write('\n'.join(lines) + '\n')
