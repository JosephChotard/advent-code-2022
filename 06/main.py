def read_input():
    with open('input.txt', 'r') as f:
        input = f.readline().strip()
    return input


def find_marker(input, length):
    last_chars = []
    for i, char in enumerate(input):
        if char in last_chars:
            index_of_char = last_chars.index(char)
            last_chars = last_chars[index_of_char+1:]
            last_chars += char
        else:
            last_chars += char
            if len(last_chars) == length:
                return i+1

def a(input):
    return find_marker(input, 4)

def b(input):
    return find_marker(input, 14)

def test_a():
    assert a('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert a('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert a('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert a('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
    assert a('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7

def test_b():
    assert b('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
    assert b('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
    assert b('nppdvjthqldpwncqszvftbrmjlhg') == 23
    assert b('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
    assert b('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26

if __name__ == '__main__':
    input = read_input()
    print(f"A: {a(input)}")
    print(f"B: {b(input)}")
