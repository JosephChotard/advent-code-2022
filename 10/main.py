import math

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
        if op == 'noop':
            cycle_count += 1
        else:
            cycle_count += 1
            if cycle_matters(cycle_count):
                total += cycle_count * X
            num = int(op[5:])
            X += num
            cycle_count += 1
        if cycle_matters(cycle_count):
            total += cycle_count * X
    return total



def b(moves):
    return 0

if __name__ == '__main__':
    ops = read_input()
    print(f"A: {a(ops)}")
    print(f"B: {b(ops)}")
