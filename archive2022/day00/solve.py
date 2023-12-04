from pprint import pprint
from more_itertools import windowed


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# TODO: Change to current day
with open("day00/input.txt") as f:
    filedata = [x.strip() for x in f.readlines()]


def solve(data):
    return None


def solve2(data):
    return None


test_input="""\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

test_answer = 1

test_answer2 = 1

PART2 = False #set to true to run through the second solver


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
    
    if PART2 == False:
        exit()
    ans2 = solve2([x.rstrip() for x in test_input.splitlines()])
    if ans2 == test_answer2:
        print(f'{bcolors.OKGREEN}Test passed. {bcolors.ENDC}')
    else: 
        print(f'wrong answer was {ans2}, expecting {test_answer2}')
        exit(f"{bcolors.WARNING}Wrong Test Answer. Exiting.{bcolors.ENDC}")
    ans2 = solve2(filedata)
    print(ans2)
    
    
