#!/usr/bin/python3

def main():
    data_in = read_file("test_input")
    srow, scol = 0, 0
    for i in range(len(data_in)):
        for j in range(len(data_in[i])):
            if data_in[i][j] == 'S':
                srow, scol = i, j

    path_len = 0
    row, col = srow, scol
    lrow, lcol = row, col
    while True:
        moves = possible_moves(data_in, row, col)
        for move in moves:
            if not empty(move) and move != (lrow, lcol):
                lrow, lcol = row, col
                row, col = move
                path_len += 1
                break

        if (row, col) == (srow, scol):
            break

    print(path_len/2)

def empty(move):
    return len(move) == 0

"""
| up and down
- left and right
L up and right
J up and left
7 left and down
F right and down
. nothing
S start

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""
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