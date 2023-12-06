#!/usr/bin/python3

def main():
    data = read_input(path="input")
    print(data)

    win_count = 0
    for j in range(data[0]):
        if (data[0] - j)*j > data[1]:
            win_count += 1

    print(win_count)

def read_input(path):
    data = read_file(path)
    data = data.split("\n")
    times = data[0][len("Time:"):].split(" ")
    distances = data[1][len("Distance:"):].split(" ")
    entrys = []

    time = ""
    for i, t in enumerate(times):
        if t != '':
            time += t
            continue

    distance = ""
    for i, d in enumerate(distances):
        if d != '':
            distance += d

    return int(time), int(distance)

def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


if __name__ == '__main__':
    main()