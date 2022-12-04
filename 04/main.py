def read_input():
    input = []
    with open('input.txt', 'r') as f:
        for row in f:
            pairs = [
                [int(x) for x in side.split('-')] for side in row.split(',')
            ]
            pairs[0][0], pairs[0][1] = min(pairs[0][0], pairs[0][1]), max(pairs[0][0], pairs[0][1])
            pairs[1][0], pairs[1][1] = min(pairs[1][0], pairs[1][1]), max(pairs[1][0], pairs[1][1])
            input.append(pairs)
    return input

def a(input):
    count = 0
    for (p1,p2) in input:
        if p1[0] >= p2[0] and p1[1] <= p2[1]:
            count += 1
        elif p2[0] >= p1[0] and p2[1] <= p1[1]:
            count += 1
    return count

def b(input):
    return 0

if __name__ == '__main__':
    input = read_input()
    print(f"A: {a(input)}")
    print(f"B: {b(input)}")