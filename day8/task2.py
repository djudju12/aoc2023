#!/usr/bin/python3
import math

def main():
    data = read_file("input")
    instructions = data[0]
    data = data[2:]
    nodes, start_nodes, final_nodes = parse_nodes(data)
    steps_list = []
    for curr_node in start_nodes:
        curr_index = curr_node
        steps = 0
        while not nodes_in_final_state([curr_index], final_nodes):
            for i in instructions:
                if i.isspace():
                    continue

                if nodes_in_final_state([curr_index], final_nodes):
                    break

                if i == 'L':
                    curr_index = nodes[curr_index][0]
                elif i == 'R':
                    curr_index = nodes[curr_index][1]

                steps += 1
        steps_list.append(steps)

    print(math.lcm(*steps_list))

def nodes_in_final_state(nodes_list, final_nodes):
    for nodes in nodes_list:
        if nodes not in final_nodes:
            return False
    return True

def parse_nodes(data: list[str]):
    labels = []
    final_nodes = []
    start_nodes = []
    for node in data:
        label: str = node[0:3]
        labels.append(label)
        if label.endswith("Z"):
            final_nodes.append(len(labels)-1)
        elif label.endswith("A"):
            start_nodes.append(len(labels)-1)

    nodes = [None for _ in labels]
    for direction in data:
        label = direction[0:3]
        direction = direction[7:15]
        l, r = direction.split(',')
        l, r = l.strip(), r.strip()
        label, r, l = labels.index(label), labels.index(r), labels.index(l)
        nodes[label] = (l, r)

    return nodes, start_nodes, final_nodes

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    main()