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

test_output = 467835

def read_input():
    with open("input.txt") as f:
        my_input = f.read().splitlines()
    return my_input

def solve(data):

    potential_gear_locations = []
    for ind_line, line in enumerate(data):
        for ind_char, char in enumerate(line):
            if char == "*":
                potential_gear_locations.append([ind_line, ind_char])
    
    number_and_locations=[]
    for ind_line, line in enumerate(data):
        num = ''
        location = [ind_line]
        for ind_char, char in enumerate(line):
            if char.isdigit():
                num += char
                location.append(ind_char)
            elif not char.isdigit() and num != '':
                number_and_locations.append([int(num), *location])
                #reset to find more numbers on line
                num = ''
                location = [ind_line]
        if num != '': 
            # We finished the line, but buffer isn't empty. Need to record
            number_and_locations.append([int(num), *location])

    adder=0
    for line, posit in potential_gear_locations:
        nums = []
        lines = [line - 1, line, line + 1]
        posits = [posit - 1, posit, posit + 1]
        for number, num_line, *num_posit in number_and_locations:
            if num_line in lines:
                for posit in posits:
                    if posit in num_posit:
                        nums.append(number)
                        break
        if len(nums) == 2:
            gear_ratio = nums[0]*nums[1]
            adder += gear_ratio
    return adder


if __name__ == "__main__":
    test_out = solve(test_input)
    print(test_out)
    my_input = read_input()
    if test_output == test_out:   
        ans = solve(my_input)
        print(ans)


