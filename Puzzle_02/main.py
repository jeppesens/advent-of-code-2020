from typing import List
from time import time
import math
from collections import namedtuple

PasswordAndPolicy = namedtuple(
    'PasswordAndPolicy',
    ['min_chars', 'max_chars', 'letter', 'password']
)


def get_inputs() -> List[PasswordAndPolicy]:
    with open('Puzzle_02/puzzle-inputs.txt', 'r') as f:
        parsed_lines = []
        for line in f.read().split('\n'):
            times, letter, password = line.split(' ')
            min_chars, max_chars = times.split('-')
            letter = letter.replace(':', '')
            parsed_lines.append(PasswordAndPolicy(
                int(min_chars),
                int(max_chars),
                letter,
                password,
            ))
        return parsed_lines


def puzzle_two(inputs: List[PasswordAndPolicy]):
    correct_passwords = 0

    for p in inputs:
        correct_positions = 0
        for pos, char in enumerate(p.password):
            if char != p.letter:
                continue
            if pos in [p.min_chars - 1, p.max_chars - 1]:
                correct_positions += 1
            if correct_positions > 1:
                continue

        if correct_positions == 1:
            correct_passwords += 1

    print(f'Puzzle two has {correct_passwords} valid passwords')


def puzzle_one(inputs: List[PasswordAndPolicy]):
    correct_passwords = 0

    for p in inputs:
        occurrences = p.password.count(p.letter)
        if occurrences <= p.max_chars and occurrences >= p.min_chars:
            correct_passwords += 1

    print(f'Puzzle one has {correct_passwords} valid passwords')


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
