def read_input():
    towers = []
    operations = []
    with open('input.txt', 'r') as f:
        lines = iter([line for line in f.readlines() if len(line.strip()) > 0])
        for line in lines:
            if line.strip()[0].isdigit():
                break
            towers.append(line[:-1])
        for line in lines:
            [tower, pos] = line.split(' from ')
            tower = int(tower[5:])
            [start, end] = [int(x) for x in pos.split(' to ')]
            operations.append({
                'towers': tower,
                'from': start,
                'to': end
            })
    towers = parse_towers(towers)
    return (towers, operations)

def parse_towers(towers_input):
    towers = []
    num_columns = (len(towers_input[0])+1)//4
    towers = [[] for _ in range(num_columns)]
    for i in range(len(towers_input)):
        row = towers_input[-i-1]
        for c in range(num_columns):
            char = row[c*4+1]
            if char != ' ':
                towers[c].append(char)
    return towers

def execure_operations(towers, operations, flip: bool):
    towers = [t.copy() for t in towers]
    for operation in operations:
        towers[operation['to']-1] += towers[operation['from']-1][-operation['towers']:][::-1 if flip else 1]
        towers[operation['from']-1] = towers[operation['from']-1][:-operation['towers']]
    return towers


def a(towers, operations):
    towers = execure_operations(towers, operations, True)
    return ''.join(tower[-1] for tower in towers)

def b(towers, operations):
    towers = execure_operations(towers, operations, False)
    return ''.join(tower[-1] for tower in towers)

if __name__ == '__main__':
    towers, operations = read_input()
    print(f"A: {a(towers, operations)}")
    print(f"B: {b(towers, operations)}")
