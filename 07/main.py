def read_input():
    with open('input.txt', 'r') as f:
        input = f.readlines()
    return input

def a(input):
    return 0

def b(input):
    return 0

if __name__ == '__main__':
    input = read_input()
    print(f"A: {a(input)}")
    print(f"B: {b(input)}")
