from pprint import pprint
def read_input():
    with open('08/input.txt', 'r') as f:
        grid = [[int(cell) for cell in line.strip()] for line in f.readlines()]
    return grid
    

def a(grid):
    size = len(grid)
    visible_count = 0
    visible = [[False for _ in range(size)] for _ in range(size)]
    for _ in range(4):
        for y, row in enumerate(grid):
            max_h = -1
            for x, tree in enumerate(row):
                if tree > max_h:
                    max_h = tree
                    if visible[y][x] == False:
                        visible_count += 1
                        visible[y][x] = True
        # Yeah this is dumb and inefficient, whatever 
        # Complexity goes brrrrr
        grid = list(zip(*grid[::-1]))
        visible = [list(row) for row in zip(*visible[::-1])]
    return visible_count

def b(grid):
    return 0

if __name__ == '__main__':
    grid = read_input()
    print(f"A: {a(grid)}")
    print(f"B: {b(grid)}")
