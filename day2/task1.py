#!/usr/bin/python3

def read_file(filepath) -> str:
    with open(filepath, "r") as f:
        return f.read()

def main():
    input = read_file("input").split("\n")
    games = []
    for line in input:
        if len(line) == 0:
            continue

        games.append(parse_game(line))

    total = 0
    for game in games:
        if game_is_possible(game, red=12, blue=14, green=13):
            total += game["ID"]

    print(total)

def possible_play(play: dict, key, limit):
    value = play.get(key)
    if value == None:
        return True

    return value <= limit

def game_is_possible(game: dict, red, blue, green):
    for play in game["PLAYS"]:
        if not possible_play(play, "red", red):
            return False

        if not possible_play(play, "blue", blue):
            return False

        if not possible_play(play, "green", green):
            return False

    return True

def parse_game(game: str):
    game_dict = {"PLAYS": []}
    game = game[5:]
    game = game.split(":")
    game_dict["ID"] = int(game[0])
    try:
        game = game[1].strip()
    except IndexError as e:
        print(game)
        exit(1)

    for g in game.split(";"):
        plays = {}
        for num_color in g.split(","):
            num_color = num_color.lstrip()
            num, color = num_color.split(" ")
            plays[color] = int(num)

        game_dict["PLAYS"].append(plays)

    return game_dict

if __name__ == '__main__':
    main()