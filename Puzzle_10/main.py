from typing import List
from time import time
import math

from functools import lru_cache


@lru_cache()
def get_inputs() -> List[int]:
    with open('Puzzle_10/puzzle-inputs.txt', 'r') as f:
        lines = [int(line) for line in f.read().splitlines()]
        lines.sort()
        return lines


def puzzle_one():
    inputs = get_inputs()
    computer_joltage = max(inputs) + 3
    one_step = 1
    three_step = 0
    for i, adapter in enumerate(inputs):
        diff = inputs[i + 1] - adapter
        if diff == 1:
            one_step += 1
        elif diff == 3:
            three_step += 1
        if inputs[i + 1] + 3 == computer_joltage:
            three_step += 1
            break
    result = one_step * three_step

    print(f'Puzzle one has the result {result}')


def puzzle_two():
    inputs = get_inputs()
    inputs.insert(0, 0)
    goal = max(inputs)

    @lru_cache()
    def get_paths(current_joltage: int = 0):
        return 1 if current_joltage == goal else sum([get_paths(a) for a in [a for a in inputs if current_joltage < a <= (current_joltage + 3)]])

    result = get_paths()
    print(f'Puzzle two has the result {result}')


def main():
    get_inputs()
    start_1 = time()
    result_1 = puzzle_one()
    print(f'Puzzle one has the value {result_1}')
    print(f'Solved puzzle one in {math.ceil((time() - start_1) * 1000)}ms')

    start_2 = time()
    puzzle_two()
    print(f'Solved puzzle two in {math.ceil((time() - start_2) * 1000)}ms')

    print(f'Solved both puzzles in {math.ceil((time() - start_1) * 1000)}ms')


if __name__ == '__main__':
    main()
