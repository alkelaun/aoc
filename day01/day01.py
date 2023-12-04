
test_input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''
test_input = test_input.split("\n")

test_output = 142

def read_input():
    with open("input.txt") as f:
        my_input = f.read().splitlines()
    return my_input

#print(my_input[0:5])

def find_first_number(string):
    for letter in string:
        try:
            int(letter)
            return letter
        except:
            continue



def solve(data):
    adder = 0
    for line in data:
        first_number = find_first_number(line)
        last_number = find_first_number(reversed(line))
        number = int(str(first_number)+str(last_number))
        adder += number
    return adder

if __name__ == "__main__":
    if test_output == solve(test_input):
        my_input = read_input()
        ans = solve(my_input)
    print(ans)

