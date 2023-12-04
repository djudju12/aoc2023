#!/usr/bin/python3
def main():
    lines = read_file("input").split("\n")

    cards = [1 for _ in lines]
    for i, line in enumerate(lines):
        if len(line) == 0:
            continue

        line = line[line.index(":")+2:]
        w, guesses = line.split("|")

        winning = []
        for w_number in w.split(" "):
            w_number = w_number.strip()
            if w_number != '':
                winning.append(int(w_number))

        # [1, 2, 4, 8, 14, 1]
        cur = 1 + i
        for g_number in guesses.split(" "):
            g_number = g_number.strip()
            if g_number != '' and int(g_number) in winning:
                if cur < len(cards):
                    cards[cur] += (cards[i])
                    cur += 1

    print(sum(cards))


def read_file(filepath) -> str:
    with open(filepath, "r") as f:
        return f.read()

if __name__ == '__main__':
    main()