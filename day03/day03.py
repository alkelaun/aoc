from pprint import pprint
test_input = '''\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''
test_input = test_input.split("\n")

TEST_OUTPUT = 4361

def read_input():
    with open("input.txt") as f:
        my_input = f.read().splitlines()
    return my_input

def solve(data):
    '''
    1. Find locations of special characters
    2. Find locations of numbers
    3. Find where numbers are within 1 of special characters (8 positions)
    '''

    special_char_locations = []
    for ind_line, line in enumerate(data):
        for ind_char, char in enumerate(line):
            if not(char.isdigit() or char == "."):
                special_char_locations.append([ind_line, ind_char])
    
    number_and_locations = []
    for ind_line, line in enumerate(data):
        # number_and_locations = [number, ind_line, ind_char, ind_char...]
        # location = [ind_line, ind_char, ind_char, ind_char]
        num = ''
        location = [ind_line]
        for ind_char, char in enumerate(line):
            if char.isdigit():
                num += char
                location.append(ind_char)
            elif not char.isdigit() and num != '':
                number_and_locations.append([int(num), *location])
                num = ''
                location = [ind_line]
        if num != '':
            number_and_locations.append([int(num), *location])

    adder=0
    for line, posit in special_char_locations:
        lines = [line - 1, line, line + 1]
        posits = [posit - 1, posit, posit + 1]
        for number, num_line, *num_posit in number_and_locations:
            if num_line in lines:
                for posit in posits:
                    if posit in num_posit:
                        adder += number
                        break
    return adder


if __name__ == "__main__":
    test_out = solve(test_input)
    print(f"{test_out= }")
    
    if TEST_OUTPUT == test_out:
        my_input = read_input()
        ans = solve(my_input)
        print(f"{ans= }")

