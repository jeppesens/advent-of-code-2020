from typing import List
from time import time
import math
import re


def get_inputs() -> List[str]:
    with open('Puzzle_04/puzzle-inputs.txt', 'r') as f:
        lines = f.read().split('\n\n')
        return lines


def puzzle_one(inputs: List[str]):
    required_inputs = [
        'byr',  # (Birth Year)
        'iyr',  # (Issue Year)
        'eyr',  # (Expiration Year)
        'hgt',  # (Height)
        'hcl',  # (Hair Color)
        'ecl',  # (Eye Color)
        'pid',  # (Passport ID)
        # 'cid',  # (Country ID)
    ]
    valid_passports = 0
    for p in inputs:
        valid_passports += 1 if all([f'{e}:' in p for e in required_inputs]) else 0

    print(f'Puzzle one has {valid_passports} valid passports')


def puzzle_two(inputs: List[str]):
    regexes = [
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        '\\bbyr:(19[2-9][0-9]|200[0-2])\\b',

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        '\\biyr:(201[0-9]|2020)\\b',

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        '\\beyr:(202[0-9]|2030)\\b',

        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        '\\bhgt:(((1[5-8][0-9]|19[0-3])cm)|(59|6[0-9]|7[0-6])in)\\b',

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        '\\bhcl:#[0-f]{6}\\b',

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        '\\becl:(amb|blu|brn|gry|grn|hzl|oth)\\b',

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        '\\bpid:[0-9]{9}\\b',

        # cid (Country ID) - ignored, missing or not.
    ]
    valid_passports = 0
    for passport in inputs:
        valid_passports += 1 if all([re.search(r, passport) for r in regexes]) else 0

    print(f'Puzzle two has {valid_passports} valid passports')


def main():
    inputs = get_inputs()

    start_1 = time()
    puzzle_one(inputs)
    print(f'Solved puzzle one in {math.ceil((time() - start_1) * 1000)}ms')

    start_2 = time()
    puzzle_two(inputs)
    print(f'Solved puzzle two in {math.ceil((time() - start_2) * 1000)}ms')

    print(f'Solved both puzzles in {math.ceil((time() - start_1) * 1000)}ms')


if __name__ == '__main__':
    main()
