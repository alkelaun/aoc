
with open("input.txt") as f:
    data = f.readlines()

def solve(data):
    total = 0
    cals = []
    for line in data:
        if line.rstrip() == "":
            cals.append(total)
            total = 0
            continue

        total += int(line.rstrip())
    total_cals_3 = 0 
    for _ in range(3):
        high = max(cals)
        total_cals_3 += high
        high_index = cals.index(high)
        cals.pop(high_index)
    return total_cals_3

test_input="""\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

if __name__=="__main__":
    ans2 = solve(data)
    print(ans2)