#!/usr/bin/python3

def main():
    data = read_file("input")
    a1 = sum_paths(data, 1)
    an = a1 + (1_000_000 - 1)*(sum_paths(data, 2) - a1)
    print(an)

def sum_paths(data, factor):
    expanded_universe = expand_rows_cols(data, factor)
    galaxies = find_galaxies(expanded_universe)
    total = 0
    for i, galaxy in enumerate(galaxies):
        for nb_galaxy in galaxies[i+1:]:
            total += distance(galaxy, nb_galaxy)

    return total

def distance(tuple1, tuple2):
    return abs(tuple2[0] - tuple1[0]) + abs(tuple2[1] - tuple1[1])

def find_galaxies(universe):
    galaxies = []
    for i, line in enumerate(universe):
        for j, c in enumerate(line):
            if c == '#':
                galaxies.append((i, j))
    return galaxies

def expand_rows_cols(data, factor):
    data = expand(data, factor)
    data = transpose(data)
    data = expand(data, factor)
    return transpose(data)

def expand(data, factor):
    expanded = []
    for line in data:
        if '#' not in line:
            for _ in range(factor):
                expanded.append(line)
        else:
            expanded.append(line)

    return expanded

def transpose(matrix):
    new_matrix = zero_matrix(len(matrix), len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

def zero_matrix(i, j):
    return [[0 for _ in range(i)] for _ in range(j)]

def read_file(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

if __name__ == '__main__':
    main()