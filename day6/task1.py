#!/usr/bin/python3

def main():
    data = read_input(path="input")

    win_count = [0 for _ in range(len(data))]

    for i, entry in enumerate(data):
        for j in range(entry[0]):
            if (entry[0] - j)*j > entry[1]:
                win_count[i] += 1

    print(mult(win_count))

def mult(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0

    total = 1
    for v in arr:
        total *= v

    return total

def read_input(path):
    data = read_file(path)
    data = data.split("\n")
    times = data[0][len("Time:"):].split(" ")
    distances = data[1][len("Distance:"):].split(" ")
    entrys = []

    for i, time in enumerate(times):
        if time == '':
            continue

        for j, distance in enumerate(distances):
            if distance != '':
                if j+1 < len(distances):
                    distances = distances[j+1:]
                entrys.append((int(time), int(distance)))
                break

    return entrys

def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


if __name__ == '__main__':
    main()