#!/usr/bin/python3

import re

def main():
    lines = []
    with open("input", "r") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        m = re.findall("(?=([0-9]|zero|one|two|three|four|five|six|seven|eight|nine))", line)
        first = todigit(m[0])
        second = todigit(m[len(m)-1])
        total += int(first+second)

    print(total)

def todigit(word: str):
    if word.isdigit():
        return word
    match word:
        case "zero":
            return "0"
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"


if __name__ == '__main__':
    main()