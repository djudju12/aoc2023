#!/usr/bin/python3

def main():
    data_in = read_file("input")
    srow, scol = 0, 0
    for i in range(len(data_in)):
        for j in range(len(data_in[i])):
            if data_in[i][j] == 'S':
                srow, scol = i, j

    path = find_path(data_in, srow, scol)
    print(path)
    fields = []
    for i in range(len(data_in)):
        r = []
        for j in range(len(data_in[i])):
            r.append(1 if (i, j) in path else 0)
        fields.append(r)

    total = 0
    for i, row in enumerate(fields):
        for j, value in enumerate(row):
            if not value and i > 0 and i < len(fields)-1 and j > 0 and j < len(fields[i])-1:
                # print(i, j, total_walls(fields, data_in, i, j))
                if all(map(lambda x: x%2==1, total_walls(fields, data_in, i, j))):
                    total += 1

    print(total)

def total_walls(data, data2, row, col):
    # print(row, col)
    # for d in data:
    #     for x in d:
    #         print(x, end="")
    #     print()

    up, right, down, left = 0, 0, 0, 0
    for i in range(row-1, 0, -1):
        if data[i][col] and data2[i][col] == '-':
            up += 1

    for i in range(row+1, len(data)-1, +1):
        if data[i][col] and data2[i][col] == '-':
            down += 1

    for i in range(col+1, len(data[row])-1, +1):
        if data[row][i] and data2[row][i] == '|':
            right += 1

    for i in range(col-1, 0, -1):
        if data[row][i] and data2[row][i] == '|':
            left += 1

    return up, right, down, left

def empty(move):
    return len(move) == 0

def find_path(data_in, srow, scol):
    row, col = srow, scol
    lrow, lcol = row, col
    path = [(srow, scol)]
    while True:
        moves = possible_moves(data_in, row, col)
        for move in moves:
            if not empty(move) and move != (lrow, lcol):
                lrow, lcol = row, col
                row, col = move
                path.append(move)
                break

        if (row, col) == (srow, scol):
            break

    return path

def possible_moves(data, row, col):
    left = lambda : (row, col-1) if col > 0 and data[row][col-1] != '.' else ()
    right = lambda : (row, col+1) if col < len(data[row]) and data[row][col+1] != '.' else ()
    up = lambda : (row-1, col) if row > 0 and data[row-1][col] != '.' else ()
    down = lambda: (row+1, col) if row < len(data) and data[row+1][col] != '.' else ()

    match data[row][col]:
        case 'S':
            return [up(), right(), down(), left()]
        case '|':
            return [up(), down()]
        case '-':
            return [right(), left()]
        case 'L':
            return [up(), right()]
        case 'J':
            return [up(), left()]
        case '7':
            return [down(), left()]
        case 'F':
            return [right(), down()]
        case _:
            return []

def read_file(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

if __name__ == '__main__':
    main()