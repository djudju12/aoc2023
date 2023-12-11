#!/usr/bin/python3

def main():
    data_in = [list(map(int, line.split(' '))) for line in read_file("input")]

    total = 0
    for entry in data_in:
        darray = entry
        k = 0
        while any(darray):
            left_value = darray[0]
            total += left_value if k % 2 == 0 else -left_value
            darray = difference_array(darray)
            k += 1

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