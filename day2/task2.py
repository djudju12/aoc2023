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
        r, g, b = find_max_play(game)
        total += (r*g*b)
    print(total)

def find_max_play(game: dict):
    r, b, g = 1, 1, 1
    for play in game["PLAYS"]:
        tr = play.get("red")
        if tr != None:
            r = tr if tr > r else r

        tb = play.get("blue")
        if tb != None:
            b = tb if tb > b else b

        tg = play.get("green")
        if tg != None:
            g = tg if tg > g else g

    return r, g, b


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