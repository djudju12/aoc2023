#!/usr/bin/python3

# thats not my solution
# https://www.youtube.com/watch?v=g3Ms5e7Jdqo
def main():
    data = day12("input")
    total = 0
    for cfg, nums in data:
        total += count(cfg, nums)

    print(total)

def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0
    if nums == ():
        return 1 if '#' not in cfg else 0

    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and '.' not in cfg[:nums[0]] and (len(cfg) == nums[0] or cfg[nums[0]] != '#'):
            result += count(cfg[nums[0] + 1:], nums[1:])

    return result

def day12(path):
    data = read_file(path)
    return [(t[0], tuple(map(int, t[1].split(',')))) for t in [entry.split(" ") for entry in data]]

def read_file(path):
    with open(path, 'r') as f:
        return f.read().splitlines()

if __name__ == '__main__':
    main()