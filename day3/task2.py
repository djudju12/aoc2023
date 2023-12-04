#!/usr/bin/python3

def main():
    dot_or_number = ".0123456789"
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
            elif inside_digit:
                if not c.isdigit():
                    maybe_parts.append((i, j-len(digit),digit))
                    digit = ""
                    inside_digit = False
                elif j == len(line)-1:
                    digit += c
                    maybe_parts.append((i, j-len(digit)+1,digit))
                else:
                    digit += c

            else:
                assert not c.isdigit()

    actual_parts = []
    for part in maybe_parts:
        linei, start_digit, digit = part
        end_digit = start_digit + len(digit)-1
        line = lines[linei]

        right_side = end_digit + 1
        left_side = start_digit - 1
        linei_up = linei - 1
        linei_down = linei + 1

        if right_side < len(line)-1 and line[right_side] == '*':
            actual_parts.append((part, (line[right_side], linei, right_side)))
        elif left_side >= 0 and line[left_side] == '*':
            actual_parts.append((part, (line[left_side], linei, left_side)))
        else:
            for i in range(left_side, right_side+1, 1):
                if i >= 0 and i < len(line):
                    if linei_up >= 0 and lines[linei_up][i] == '*':
                        actual_parts.append((part, (lines[linei_up][i], linei_up, i)))
                        break
                    elif linei_down < len(lines) and lines[linei_down][i] == '*':
                        actual_parts.append((part, (lines[linei_down][i], linei_down, i)))
                        break

    stars_with_part = [[[] for i in range(len(l))] for l in lines]
    for part_symbol in actual_parts:
        part, symbol_data = part_symbol
        if symbol_data[0] == "*":
            stars_with_part[symbol_data[1]][symbol_data[2]].append(int(part[2]))

    total = 0
    for line in stars_with_part:
        for star in line:
            if len(star) == 2:
                total += (star[0]*star[1])

    print(total)

def read_file(filepath) -> str:
    with open(filepath, "r") as f:
        return f.read()

if __name__ == '__main__':
    main()