from pprint import pprint
from more_itertools import windowed


class bcolors:

    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


with open("day06/input.txt") as f:
    filedata = [x.strip() for x in f.readlines()]


def solve(data):

    a = list(str(data[0]))
    b = a[1:]
    c = a[2:]
    d = a[3:]
    counter = 3
    for w in zip(a,b,c,d):
        counter+=1
        if len(set(w)) == 4:
            return counter

    return None


def solve2(data):
    a = list(str(data[0]))
    counter=14
    for index, _ in enumerate(range(len(a))):
        window = a[index:index+14] 
        if len(set(window)) == 14:
            return counter
        else:
            counter += 1
    return None

test_input="""\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""

test_answer = 7

test_answer2 = 19

if __name__=="__main__":
    ans = solve([x.rstrip() for x in test_input.splitlines()])
    if ans == test_answer:
        print(f'{bcolors.OKGREEN}Test passed. {bcolors.ENDC}')
    else: 
        print(f'wrong answer was {ans}, expecting {test_answer}')
        exit(f"{bcolors.WARNING}Wrong Test Answer. Exiting.{bcolors.ENDC}")
    ans = solve(filedata)
    print(ans)
    ans2 = solve2(filedata)
    
    ans2 = solve2([x.rstrip() for x in test_input.splitlines()])
    if ans2 == test_answer2:
        print(f'{bcolors.OKGREEN}Test passed. {bcolors.ENDC}')
    else: 
        print(f'wrong answer was {ans2}, expecting {test_answer2}')
        exit(f"{bcolors.WARNING}Wrong Test Answer. Exiting.{bcolors.ENDC}")
    ans2 = solve2(filedata)
    print(ans2)
    
    
