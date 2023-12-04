
test_input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
test_input = test_input.split("\n")

test_output = 281

def read_input():
    with open("input.txt") as f:
        my_input = f.read().splitlines()
    return my_input


number_map = {"one":1,
              "two":2,
              "three":3,
              "four":4,
              "five":5,
              "six":6,
              "seven":7,
              "eight":8,
              "nine":9, 
              }


def find_numbers(string):
    numbers_to_index_map = {}

    for ind, letter in enumerate(string):
        if letter.isdigit():
            numbers_to_index_map[ind]=int(letter)

    for key in number_map:
        if key in string:
            ind = string.find(key)
            rind = string.rfind(key)
            numbers_to_index_map[ind] = number_map[key]
            numbers_to_index_map[rind] = number_map[key]

    keys = list(numbers_to_index_map.keys())
    keys.sort()
    sorted_order = {i:numbers_to_index_map[i] for i in keys}
    pair = sorted_order[keys[0]], sorted_order[keys[-1]]
    value = int(str(pair[0]) + str(pair[1]))
    return value


def solve(data):
    adder = 0
    for line in data:
        value = find_numbers(line)
        adder += value
    return adder

if __name__ == "__main__":
    test = solve(test_input)
    print(test)
    if test_output == test:
        my_input = read_input()
        ans = solve(my_input)
        print(ans)

