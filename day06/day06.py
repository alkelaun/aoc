test_input = """\
Time:      7  15   30
Distance:  9  40  200"""
test_input = test_input.split("\n")

TEST_OUTPUT = 288

TEST_OUTPUT2 = 30


def read_input():
    with open("input.txt") as f:
        my_input = f.read().splitlines()
    return my_input


def solve(data):
    value = 1
    times, distances = data[0].split(), data[1].split()
    for time, distance in zip(times[1:], distances[1:]):
        count = 0
        for x in range(int(time)):
            velocity = int(x)
            time_at_velocity = int(time) - int(x)
            distance_traveled = velocity * time_at_velocity
            print(velocity, distance_traveled)
            if distance_traveled > int(distance):
                count += 1
        value = value * count
    return value


def solve2(data):
    total = 0
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
