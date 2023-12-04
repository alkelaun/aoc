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


with open("day04/input.txt") as f:
    filedata = [x.strip() for x in f.readlines()]

def solve(data):
    total = 0

    for line in data:
        elf1, elf2 = line.split(",")
        elf1_low, elf1_high = elf1.split("-")
        elf2_low, elf2_high = elf2.split("-")
        if int(elf1_low) >= int(elf2_low) and int(elf1_high) <= int(elf2_high):
            total+=1
            print(f"{elf1=}, {elf2=}")
        elif int(elf2_low) >= int(elf1_low) and int(elf2_high)<= int(elf1_high):
            total+=1
    return total


def solve2(data):
    total = 0
    for line in data:
        elf1, elf2 = line.split(",")
        elf1_low, elf1_high = elf1.split("-")
        elf2_low, elf2_high = elf2.split("-")
        elf1_low, elf1_high = int(elf1_low), int(elf1_high)+1
        elf2_low, elf2_high = int(elf2_low), int(elf2_high)+1
        elf1 = list(range(elf1_low, elf1_high))
        elf2 = list(range(elf2_low, elf2_high))
        intersection =set(elf1).intersection(set(elf2))
        if intersection != set():
            total += 1
    return total

test_input="""\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

test_answer = 2

test_answer2 = 4

if __name__=="__main__":
    ans = solve([x.rstrip() for x in test_input.splitlines()])
    if ans == test_answer:
        print(f'{bcolors.OKGREEN}Test passed. {bcolors.ENDC}')
    else: 
        print(f'wrong answer was {ans}, expecting {test_answer}')
        exit(f"{bcolors.WARNING}Wrong Test Answer. Exiting.{bcolors.ENDC}")
    ans = solve(filedata)
    print(ans)
    
    ans2 = solve2([x.rstrip() for x in test_input.splitlines()])
    if ans2 == test_answer2:
        print(f'{bcolors.OKGREEN}Test passed. {bcolors.ENDC}')
    else: 
        print(f'wrong answer was {ans2}, expecting {test_answer2}')
        exit(f"{bcolors.WARNING}Wrong Test Answer. Exiting.{bcolors.ENDC}")
    ans2 = solve2(filedata)
    print(ans2)
    
