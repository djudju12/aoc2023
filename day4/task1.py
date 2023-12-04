#!/usr/bin/python3

def calc_points(x):
    if x == 0:
        return 0

    total = 1
    x -= 1
    while x != 0:
        total *= 2
        x -= 1

    return total

def main():
    lines = read_file("input").split("\n")

    cards = []
    for line in lines:
        if len(line) == 0:
            continue

        line = line[line.index(":")+2:]
        winning, guesses = line.split("|")

        numbers = {"winning":[], "guesses":[]}
        for w_number in winning.split(" "):
            w_number = w_number.strip()
            if w_number != '':
                numbers["winning"].append(int(w_number))

        for g_number in guesses.split(" "):
            g_number = g_number.strip()
            if g_number != '':
                numbers["guesses"].append(int(g_number))

        cards.append(numbers)

    total = 0
    for card in cards:
        total_winning_nums = 0
        for guess in card["guesses"]:
            if guess in card["winning"]:
                total_winning_nums += 1
        total += calc_points(total_winning_nums)

    print(total)


def read_file(filepath) -> str:
    with open(filepath, "r") as f:
        return f.read()

if __name__ == '__main__':
    main()