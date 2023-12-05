from pprint import pprint
from collections import defaultdict, Counter
test_input = '''\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
test_input = test_input.split("\n")

TEST_OUTPUT = 13

TEST_OUTPUT2 = 30

def read_input():
    with open("input.txt") as f:
        my_input = f.read().splitlines()
    return my_input

def solve(data):
    value=0
    for line in data:
        row_wins = 0 
        card = line.split(" ")
        card = list(filter(None,card))
        index = card.index("|")
        winning_numbers, numbers_found = card[2:index], card[index+1:]
        for number in numbers_found:
            if number in winning_numbers:
                row_wins += 1
        if row_wins == 0:
            continue
        row_value = 2**(row_wins-1)
        value += row_value
        
    return value

def solve2(data):
    counter = defaultdict(int)
    for index, line in enumerate(data):
        row_wins = 0 
        row = line.split(" ")
        row = list(filter(None,row))
        index = row.index("|")
        card, winning_numbers, numbers_found = int(row[1].strip(':')), row[2:index], row[index+1:]
        counter[card] += 1
        for number in numbers_found:
            if number in winning_numbers:
                row_wins += 1
        for y in range(counter[card]):
            for x in range(card+1, card+row_wins+1):
                counter[x]+=1

    total = sum(counter.values())   
    return total


if __name__ == "__main__":
    test_out = solve(test_input)
    print(f"{test_out= }")
    
    if TEST_OUTPUT == test_out:
        my_input = read_input()
        ans = solve(my_input)
        print(f"{ans= }")

    test_out2 = solve2(test_input)
    print(f"{test_out2= }")
    if TEST_OUTPUT2 == test_out2:
        my_input = read_input()
        ans2 = solve2(my_input)
        print(f"{ans2= }")


