import math

def read_input():
    with open('09/input.txt', 'r') as f:
        input = [l.strip().split(' ') for l in f.readlines()]
        input = [(direction, int(amount)) for [direction, amount] in input]
    return input

def is_adjacent(knot_1, knot_2):
    return abs(knot_1[0] - knot_2[0]) <= 1 and abs(knot_1[1] - knot_2[1]) <= 1

move_pos = {
    "R": (0,1),
    "L": (0,-1),
    "U": (1,0),
    "D": (-1,0)
}

def move_n_knots(n: int, steps):
    rope = [(0,0)] * n
    visited = [set([knot]) for knot in rope]

    for (dir, amount) in steps:
        motion = move_pos[dir]
        for _ in range(amount):
            rope[0] = tuple(map(sum, zip(rope[0], motion)))
            for i in range(1,n):
                if not is_adjacent(rope[i-1], rope[i]):
                    if rope[i][0] != rope[i-1][0]:
                        rope[i] = (rope[i][0]+int(math.copysign(1, rope[i-1][0] - rope[i][0])), rope[i][1])
                    if rope[i][1] != rope[i-1][1]:
                        rope[i] = (rope[i][0], rope[i][1]+int(math.copysign(1, rope[i-1][1] - rope[i][1])))
                visited[i].add(rope[i])
    return len(visited[-1])

def a(moves):
    return move_n_knots(2, moves)


def b(moves):
    return move_n_knots(10, moves)

if __name__ == '__main__':
    moves = read_input()
    print(f"A: {a(moves)}")
    print(f"B: {b(moves)}")
