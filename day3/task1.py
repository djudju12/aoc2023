#!/usr/bin/python3

def main():
    file = "input"
    lines = read_file(file).split("\n")

    maybe_parts = []
    for i, line in enumerate(lines):
        digit = ""
        inside_digit = False
        for j, c in enumerate(line):
            if not inside_digit and c.isdigit():
                inside_digit = True
                digit += c
            elif inside_digit and not c.isdigit():
                maybe_parts.append((i, j-len(digit),digit))
                digit = ""
                inside_digit = False
            elif inside_digit:
                digit += c
            else:
                assert not c.isdigit()

    actual_parts = []
    for part in maybe_parts:
        linei, start_digit, digit = part
        end_digit = start_digit + len(digit)-1
        line = lines[linei]


        right_side = end_digit+1
        left_side = start_digit-1
        linei_up = linei - 1
        linei_down = linei + 1

        if right_side < len(line) and line[right_side] != '.':
            actual_parts.append(part)
        elif left_side >= 0 and line[left_side] != '.':
            actual_parts.append(part)
        else:
            for i in range(left_side, right_side+1, 1):
                if i >= 0 and i < len(line):
                    if linei_up >= 0 and lines[linei_up][i] != '.':
                        actual_parts.append(part)
                        break
                    elif linei_down < len(lines) and lines[linei_down][i] != '.':
                        actual_parts.append(part)
                        break

    total = 0
    for part in actual_parts:
        _, _, digit = part
        total += int(digit)

    print(total)

def read_file(filepath) -> str:
    with open(filepath, "r") as f:
        return f.read()

if __name__ == '__main__':
    main()