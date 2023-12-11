#!/usr/bin/python3

def main():
    data_in = [list(map(int, line.split(' '))) for line in read_file("input")]

    total = 0
    for entry in data_in:
        darray = entry
        while any(darray):
            total += darray[len(darray)-1]
            darray = difference_array(darray)

    print(total)

def difference_array(arr):
    darray = []
    for i in range(len(arr)-1):
        darray.append(arr[i+1] - arr[i])

    return darray


def read_file(path: str) -> list[str]:
    with open(path, 'r') as f:
        return f.read().split('\n')

if __name__ == '__main__':
    main()