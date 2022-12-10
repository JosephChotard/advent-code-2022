import math
from typing import Tuple

def read_input():
    with open('10/input.txt', 'r') as f:
        input = [l.strip() for l in f.readlines()]
    return input

def cycle_matters(cycle_count: int) -> bool:
    if cycle_count == 20:
        return True
    elif (cycle_count-20)%40 == 0:
        return True
    return False

def a(ops):
    total = 0
    cycle_count = 1
    X = 1
    for op in ops:
        cycle_count += 1
        if op != 'noop':
            if cycle_matters(cycle_count):
                total += cycle_count * X
            num = int(op[5:])
            X += num
            cycle_count += 1
        if cycle_matters(cycle_count):
            total += cycle_count * X
    return total

def num_to_pos(num: int) -> Tuple[int, int]:
    x = num%40
    y = num//40
    return (x,y)

def draw(cycle_count, grid, X):
    (x,y) = num_to_pos(cycle_count)
    if abs(x-X) <= 1:
        grid[y][x] = '#'
    return grid



def b(ops):
    grid = [[' ' for _ in range(40)] for _ in range(6)]
    cycle_count = -1
    X = 1
    for op in ops:
        cycle_count += 1
        draw(cycle_count, grid, X)
        if op != 'noop':
            cycle_count += 1
            # print(f"During cycle  {cycle_count}: CRT draws pixel in position {cycle_count-1}")
            draw(cycle_count, grid, X)
            num = int(op[5:])
            # print(f"Start cycle   {cycle_count}: begin executing addx {num}")
            X += num
    return render_grid(grid)

def render_grid(grid):
    out = ''
    for row in grid:
        out += ''.join(row) + '\n'
    return out

if __name__ == '__main__':
    ops = read_input()
    print(f"A: {a(ops)}")
    print(f"B: \n{b(ops)}")
