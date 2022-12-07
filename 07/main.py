from collections import defaultdict
from typing import List, Tuple
from pprint import pprint

def read_input():
    with open('07/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    files = defaultdict(int)
    path = []

    for line in lines:
        match line.split():
            case ['$', 'cd', '..']:
                path.pop()
            case ['$', 'cd', p]:
                path.append(p)
            case ['$', 'ls']:
                pass
            case ['dir', p]:
                pass
            case [s, f]:
                files[tuple(path)] += int(s)
                curr_path = path[:-1]
                while curr_path:
                    files[tuple(curr_path)] += int(s)
                    curr_path.pop()
    return files
    

def a(files):
    return sum([size for size in files.values() if size <= 100_000])

def b(files):
    return 0

if __name__ == '__main__':
    files = read_input()
    print(f"A: {a(files)}")
    print(f"B: {b(files)}")
