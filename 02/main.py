def read_input():
    games = []
    with open("input.txt", "r") as f:
        for row in f:
            [a,b] = row.strip().split(' ')
            if a == 'A':
                p1 = 'ROCK'
            elif a == 'B':
                p1 = 'PAPER'
            else:
                p1 = 'SCISSORS'

            games.append((p1,b))
    return games

TIE = 3
WIN = 6
LOSE = 0

scores = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}

rules = {
    'ROCK': {
        'X': 'SCISSORS',
        'Y': 'ROCK',
        'Z': 'PAPER'
    },
    'PAPER': {
        'X': 'ROCK',
        'Y': 'PAPER',
        'Z': 'SCISSORS'
    },
    'SCISSORS': {
        'X': 'PAPER',
        'Y': 'SCISSORS',
        'Z': 'ROCK'
    }
}

def game_score(p1, p2):
    if rules[p1]['X'] == p2:
        return LOSE
    if rules[p1]['Y'] == p2:
        return TIE
    return WIN

def a(input):
    input_for_a = []
    for (p1,b) in input:
        if b == 'X':
            p2 = 'ROCK'
        elif b == 'Y':
            p2 = 'PAPER'
        else:
            p2 = 'SCISSORS'
        input_for_a.append((p1,p2))
    s = [scores[p2] + game_score(p1,p2) for (p1,p2) in input_for_a]
    return sum(s)

def b(input):
    input_for_b = []
    for (p1,b) in input:
        input_for_b.append((p1, rules[p1][b]))
    s = [scores[p2] + game_score(p1,p2) for (p1,p2) in input_for_b]
    return sum(s)

if __name__ == '__main__':
    input = read_input()
    print(f"A: {a(input)}")
    print(f"B: {b(input)}")