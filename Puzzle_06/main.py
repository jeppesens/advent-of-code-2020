from typing import List
from time import time
import math
import re


def get_inputs() -> List[str]:
    with open('Puzzle_06/puzzle-inputs.txt', 'r') as f:
        lines = f.read().split('\n\n')
        return lines


def puzzle_one(inputs: List[str]):
    yes_answers = sum(len(set([c for c in re.sub(r'\W', '', group)])) for group in inputs)

    print(f'Puzzle one has {yes_answers} yes answers')


def puzzle_two(inputs: List[str]):
    all_yes = sum(sum(sum([1 if all([c in p for p in group.splitlines()]) else 0]) for c in group.splitlines()[0]) for group in inputs)

    print(f'Puzzle two has {all_yes} all yes responses')


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
