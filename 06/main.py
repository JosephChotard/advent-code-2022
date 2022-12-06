def read_input():
    with open('input.txt', 'r') as f:
        input = f.readline().strip()
    return input


def a(input):
    last_chars = []
    for i, char in enumerate(input):
        if char in last_chars:
            index_of_char = last_chars.index(char)
            last_chars = last_chars[index_of_char+1:]
            last_chars += char
        else:
            last_chars += char
            if len(last_chars) == 4:
                return i+1

def b(input):
    return 0

def asserts():
    assert(a('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5)
    assert(a('nppdvjthqldpwncqszvftbrmjlhg') == 6)
    assert(a('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10)
    assert(a('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11)
    assert(a('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7)

if __name__ == '__main__':
    input = read_input()
    asserts()
    print(f"A: {a(input)}")
    print(f"B: {b(input)}")
