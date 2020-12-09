from typing import List
from time import time
import math

from functools import lru_cache


@lru_cache()
def get_inputs() -> List[str]:
    with open('Puzzle_09/puzzle-inputs.txt', 'r') as f:
        lines = f.read().splitlines()
        return [int(l) for l in lines]


def puzzle_one():
    inputs = get_inputs()
    return next(n for i, n in enumerate(inputs[25:]) if not any(n - nn != nn and n - nn in inputs[i:i + 25] for nn in inputs[i:i + 25]))


def puzzle_two():
    inputs = get_inputs()
    looking_for = puzzle_one()
    solution = next(max(inputs[i:i + r]) + min(inputs[i:i + r]) for r in range(2, len(inputs) - 1) for i in range(len(inputs) - r - 1) if sum(inputs[i:i + r]) == looking_for)
    print(f'Puzzle two has the solution {solution}')


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
