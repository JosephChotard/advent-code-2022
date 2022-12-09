from pprint import pprint

def read_input():
    with open('09/input.txt', 'r') as f:
        input = [l.strip().split(' ') for l in f.readlines()]
        input = [(direction, int(amount)) for [direction, amount] in input]
    return input

def is_adjacent(h_pos, t_pos):
    return abs(h_pos[0] - t_pos[0]) <= 1 and abs(h_pos[1] - t_pos[1]) <= 1

def a(moves):
    visited = set([(0,0)])
    prev_h_pos = (0,0)
    h_pos = (0,0)
    t_pos = (0,0)
    for (dir, amount) in moves:
        match dir:
            case "R":
                motion = (0,1)
            case "L":
                motion = (0,-1)
            case "U":
                motion = (1,0)
            case "D":
                motion = (-1,0)
        for _ in range(amount):
            prev_h_pos = tuple(h_pos)
            h_pos = tuple(map(sum, zip(h_pos, motion)))
            if not is_adjacent(h_pos, t_pos):
                visited.add(prev_h_pos)
                t_pos = tuple(prev_h_pos)
    return len(visited)


def b(moves):
    return 0

if __name__ == '__main__':
    moves = read_input()
    print(f"A: {a(moves)}")
    print(f"B: {b(moves)}")
