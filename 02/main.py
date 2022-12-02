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
def game_score(p1, p2):
    if p1 == p2:
        return TIE
    if p1 == 'ROCK' and p2 == 'PAPER':
        return WIN
    if p1 == 'PAPER' and p2 == 'SCISSORS':
        return WIN
    if p1 == 'SCISSORS' and p2 == 'ROCK':
        return WIN
    return LOSE

scores = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}

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
    pass

if __name__ == '__main__':
    input = read_input()
    print(f"A: {a(input)}")
    print(f"B: {b(input)}")