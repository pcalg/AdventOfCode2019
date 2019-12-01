from pathlib import Path


def read_file(file_location, file_name):
    fn = file_location / file_name

    with open(fn) as f:
        content = f.readlines()
    return [c.strip('\n').strip('\t') for c in content]


def read_file_int(file_location, file_name):
    fn = file_location / file_name

    with open(fn) as f:
        content = f.readlines()
    return [int(c.strip('\n').strip('\t')) for c in content]


def save_output(file_location, file_name, lines):
    fn = file_location / file_name
    with open(fn, 'w') as f:
        f.write('\n'.join(lines) + '\n')
