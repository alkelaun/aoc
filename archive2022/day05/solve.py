from pprint import pprint
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


with open("day05/input.txt") as f:
    filedata = [x for x in f.readlines()]


def parse_start(header):
    data=[]
    for i in range(8): 
        line = header[i] 
        x = [ line[x:x+4].strip() for x in range(0,len(line),4) ]
        data.append(x) 
    reversed_data= data[::-1]
    m = reversed_data
    rez = [[m[j][i] for j in range(len(m)) if m[j][i] != "" ] for i in range(len(m[0]))]
    print(rez)
    return rez

def move(line):
    pass

def solve(data):
    blocks = parse_start(data[:8])
    for index, line in enumerate(data[10:]):
        line = line.strip()
        #move 6 from 2 to 8
        _, boxes, _, from_row, _, to_row = line.split(" ")
        boxes=int(boxes)
        from_row=int(from_row)-1
        to_row=int(to_row)-1
        for box in range(boxes):
            try:
                a = blocks[from_row].pop()
                blocks[to_row].append(a)
            except IndexError:
                print(f'error on {index} with {from_row=}, {to_row=} {boxes=}')
                continue 
    ans = []
    for line in blocks:
       ans.append(line.pop()) 
    answer = "".join(ans)
    answer2 = answer.replace("[","").replace("]","")
    print(answer2)
    return ans


def solve2(data):
    blocks = parse_start(data[:8])
    for index, line in enumerate(data[10:]):
        line = line.strip()
        #move 6 from 2 to 8
        _, boxes, _, from_row, _, to_row = line.split(" ")
        boxes=int(boxes)
        from_row=int(from_row)-1
        to_row=int(to_row)-1
        move = blocks[from_row][-boxes:]
        del blocks[from_row][-boxes:]
        for el in move:
            blocks[to_row].append(el)
        
    ans = []
    for line in blocks:
       ans.append(line.pop()) 
    answer = "".join(ans)
    answer2 = answer.replace("[","").replace("]","")
    print(answer2)
    return answer2

test_input="""\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""

test_answer = "CMZ"

test_answer2 = 1

if __name__=="__main__":
    #ans = solve([x.rstrip() for x in test_input.splitlines()])
   # if ans == test_answer:
   #     print(f'{bcolors.OKGREEN}Test passed. {bcolors.ENDC}')
   # else: 
   #     print(f'wrong answer was {ans}, expecting {test_answer}')
   #     exit(f"{bcolors.WARNING}Wrong Test Answer. Exiting.{bcolors.ENDC}")
    ans = solve(filedata)
    ans2 = solve2(filedata)
    '''
    ans2 = solve2([x.rstrip() for x in test_input.splitlines()])
    if ans2 == test_answer2:
        print(f'{bcolors.OKGREEN}Test passed. {bcolors.ENDC}')
    else: 
        print(f'wrong answer was {ans2}, expecting {test_answer2}')
        exit(f"{bcolors.WARNING}Wrong Test Answer. Exiting.{bcolors.ENDC}")
    ans2 = solve2(filedata)
    print(ans2)
    '''
    
