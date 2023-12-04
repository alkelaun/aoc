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


with open("day02/input.txt") as f:
    filedata = [x.strip() for x in f.readlines()]

def result_of_game(me, you):
    if ((me == "A" and you == "X") or
        (me == "B" and you == "Y") or
        (me == "C" and you == "Z")
    ):
        return 3
    if ((me == "A" and you == "Z") or   #Rock beats scissors
        (me == "B" and you == "X") or   #Paper beats Rock
        (me == "C" and you == "Y")      #Scissors beats paper
    ):
        return 0
    if ((me == "A" and you == "Y") or
        (me == "B" and you == "Z") or
        (me == "C" and you == "X")
    ):
        return 6
    raise("wtf")

def solve(data):
    
    mapping ={
        "X": 1, #rock
        "Y": 2, #paper
        "Z": 3, #scissors
    }
    score = 0
    for line in data:
        you, me = line.split(" ")
        score += mapping[me]
        score += result_of_game(you, me)
    return score

test_input="""\
A Y
B X
C Z
"""

test_answer = 12

#map X is lose, Y is draw and Z is win, given the input, select the output
# A Rock, B Paper, C Scissors
outcome_map = {
    "X":{
        "A":"Z",
        "B":"X",
        "C":"Y",
        },
    "Y":{
        "A":"X",
        "B":"Y",
        "C":"Z",
        },
    "Z":{
        "A":"Y",
        "B":"Z",
        "C":"X",
        },
}

def solve2(data, outcome_map):
    
    mapping ={
        "X": 1, #rock
        "Y": 2, #paper
        "Z": 3, #scissors
    }
    score = 0
    for line in data:
        you, outcome = line.split(" ")
        me = outcome_map[outcome][you]
        score += mapping[me]
        score += result_of_game(you, me)
    return score

if __name__=="__main__":
    ans = solve2([x.rstrip() for x in test_input.splitlines()], outcome_map)
    if ans == test_answer:
        print(f'{bcolors.OKGREEN}Test passed. {bcolors.ENDC}')
    else: 
        print(f'{ans}')
        exit(f"{bcolors.WARNING}Wrong Test Answer. Exiting.{bcolors.ENDC}")
    ans = solve2(filedata, outcome_map)
    print(ans)
    