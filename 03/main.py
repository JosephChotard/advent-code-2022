def read_input():
    rucksacks = []
    with open("input.txt", 'r') as f:
        for row in f:
            rucksacks.append(row.strip())
    return rucksacks

def char_priority(c):
    if c.lower() == c:
        return ord(c)-97+1
    else:
        return ord(c) - 65 + 27

def a(input):
    total = 0
    for rucksack in input:
        middle = len(rucksack)//2
        (comp_a, comp_b) = (rucksack[:middle], rucksack[middle:])
        outsider = set(comp_a).intersection(set(comp_b)).pop()
        total += char_priority(outsider)
    return total

def b(input):
    total = 0
    step = 3
    for i in range(0, len(input), step):
        (elf1, elf2, elf3) = input[i:i+step]
        common = set(elf1).intersection(set(elf2)).intersection(set(elf3)).pop()
        total += char_priority(common)
    return total

if __name__ == '__main__':
    input = read_input()
    print(f"A: {a(input)}")
    print(f"B: {b(input)}")