#!/usr/bin/python3

def main():
    data = read_file("input")
    instructions = data[0]
    data = data[2:]
    nodes = parse_nodes(data)
    curr_index = 0
    steps = 0
    print(nodes)
    while (curr_index != len(nodes)-1):
        for i in instructions:
            if i.isspace():
                continue

            if curr_index == len(nodes)-1:
                break

            if i == 'L':
                curr_index = nodes[curr_index][0]
            elif i == 'R':
                curr_index = nodes[curr_index][1]

            steps += 1

    print(steps)


def parse_nodes(data: list[str]) -> list[tuple]:
    already_checked = ["AAA"]
    for node in data:
        label = node[0:3]
        if label != "ZZZ" and label not in already_checked:
            already_checked.append(label)
    already_checked.append("ZZZ")

    nodes = [None for _ in already_checked]
    for direction in data:
        label = direction[0:3]
        direction = direction[7:15]
        l, r = direction.split(',')
        l, r = l.strip(), r.strip()
        label, r, l = already_checked.index(label), already_checked.index(r), already_checked.index(l)
        nodes[label] = (l, r)

    return nodes

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    main()