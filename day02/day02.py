
test_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
test_input = test_input.split("\n")

test_output = 8

def read_input():
    with open("input.txt") as f:
        my_input = f.read().splitlines()
    return my_input

def solve(data):
    max_cubes = {'red':12, 'green':13, 'blue':14}
    adder = 0
    for row in data:
        game_id, game_set = row.split(':')
        game_id = int(game_id.split(" ")[1])
        games = game_set.split(";")
        bad = False
        for game in games:
            if "," in game:
                draws = game.split(",")
            else:
                draws= [game]
            for draw in draws:
                val, color = draw.lstrip().split(" ")
                if int(val) > max_cubes[color]:
                    bad = True
        if bad == False:
            adder += game_id
    return adder
 

if __name__ == "__main__":
    if test_output == solve(test_input):
        my_input = read_input()
        ans = solve(my_input)
        print(ans)

