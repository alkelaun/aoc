class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


with open("day03/input.txt") as f:
    filedata = [x.strip() for x in f.readlines()]

def solve(data):
    total = 0
    for line in data:
        y, x = line[len(line)//2:], line[:len(line)//2]     
        intersection = set(x).intersection(set(y)) 
        character = "".join(intersection)
        if character.islower():
            priority = ord(character)-96
        else:
            priority = ord(character)-38
        #print(f"{intersection=}, {character=}, {priority=}")
        total += priority
    return total


def solve2(data):
    total = 0
    a = data[0::3]
    b = data[1::3]
    c = data[2::3]
    for x, y, z in zip(a,b,c):
        intersection = set(x).intersection(set(y)).intersection(set(z))
        character = "".join(intersection)
        if character.islower():
            priority = ord(character)-96
        else:
            priority = ord(character)-38
        total += priority
        print(f"{character=}, {priority=}")
    return total

test_input="""\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

test_answer = 70


if __name__=="__main__":
    ans = solve2([x.rstrip() for x in test_input.splitlines()])
    if ans == test_answer:
        print(f'{bcolors.OKGREEN}Test passed. {bcolors.ENDC}')
    else: 
        print(f'wrong answer was {ans}, expecting {test_answer}')
        exit(f"{bcolors.WARNING}Wrong Test Answer. Exiting.{bcolors.ENDC}")
    ans = solve2(filedata)
    print(ans)
