from typing import List, Tuple
from time import time
import math


def get_inputs() -> Tuple[List[str], int]:
    with open('Puzzle_03/puzzle-inputs.txt', 'r') as f:
        lines = f.read().splitlines()
        width = len(lines[0])
        return (lines, width)


def puzzle_one(args: Tuple[List[str], int]):
    tree_hits = solve_puzzle(args, y_move=1, x_move=3)

    print(f'Puzzle one hit {tree_hits} trees')


def puzzle_two(args: Tuple[List[str], int]):
    def solve(x, y):
        return solve_puzzle(args, x_move=x, y_move=y)

    hits = [solve(x, y) for x, y in [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]]

    result = 1
    for x in hits:
        result = result * x

    print(f'Solution to puzzle 2 is {result}')


def solve_puzzle(args: Tuple[List[str], int], x_move: int, y_move: int):
    lines, width = args
    slope_length = len(lines)
    tree_hits = 0
    x, y = 0, 0
    while True:
        if (lines[y] * math.ceil(x / width + 1))[x] == '#':
            tree_hits += 1
        y += y_move
        x += x_move

        if y > slope_length - 1:
            break

    return tree_hits


def main():
    inputs = get_inputs()

    start_1 = time()
    puzzle_one(inputs)
    print(f'Solved puzzle one in {math.ceil((time() - start_1) * 1000)}ms')

    start_2 = time()
    puzzle_two(inputs)
    print(f'Solved puzzle one in {math.ceil((time() - start_2) * 1000)}ms')

    print(f'Solved both puzzles in {math.ceil((time() - start_1) * 1000)}ms')


if __name__ == '__main__':
    main()
