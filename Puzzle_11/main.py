from typing import List
from time import time
import math

from functools import lru_cache


@lru_cache()
def get_inputs() -> List[List[str]]:
    with open('Puzzle_11/puzzle-inputs.txt', 'r') as f:
        return [[char for char in line] for line in f.read().splitlines()]


def puzzle_one():
    @lru_cache()
    def get_surrounding_chairs(column: int, row: int):
        state = get_inputs()
        return [(x, y) for x in range(max([column - 1, 0]), min([len(state[row]), column + 2])) for y in range(max([row - 1, 0]), min([row + 2, len(state)])) if state[y][x] != '.' and (y != row or x != column)]

    def get_final_state() -> List[List[str]]:
        state = get_inputs()
        while True:
            new_state = [line.copy() for line in state.copy()]
            changed = False
            for row, seat_row in enumerate(state):
                for column, status in enumerate(seat_row):
                    if status == '.':
                        continue
                    surrounding_coordinates = get_surrounding_chairs(column, row)
                    if status == 'L' and all([state[y][x] == 'L' for x, y in surrounding_coordinates]):
                        new_state[row][column] = '#'
                        changed = True
                    elif status == '#' and [state[y][x] == '#' for x, y in surrounding_coordinates].count(True) >= 4:
                        new_state[row][column] = 'L'
                        changed = True
            if not changed:
                return new_state
            else:
                state = new_state

    final_state = get_final_state()

    occupied_state = sum([r.count('#') for r in final_state])

    print(f'Puzzle one, the state to have {occupied_state} occupied seats')


def puzzle_two():
    @lru_cache()
    def get_surrounding_chairs(column: int, row: int):
        state = get_inputs()
        # return [(x, y) for x in range(max([column - 1, 0]), min([len(state[row]), column + 2])) for y in range(max([row - 1, 0]), min([row + 2, len(state)])) if y != row or x != column]
        return [c for c in [
            # --y x
            next(((column, row - step) for step in range(1, row + 1) if state[row - step][column] != '.'), None),
            # --y ++x
            next(((column + step, row - step) for step in range(1, min([row + 1, len(state[row][column:])])) if state[row - step][column + step] != '.'), None),
            # y ++x
            next(((column + step, row) for step in range(1, len(state[row][column:])) if state[row][column + step] != '.'), None),
            # ++y ++x
            next(((column + step, row + step) for step in range(1, min([len(state[row:]), len(state[row][column:])])) if state[row + step][column + step] != '.'), None),
            # ++y x
            next(((column, row + step) for step in range(1, len(state[row:])) if state[row + step][column] != '.'), None),
            # ++y --x
            next(((column - step, row + step) for step in range(1, min([len(state[row:]), column + 1])) if state[row + step][column - step] != '.'), None),
            # y --x
            next(((column - step, row) for step in range(1, column + 1) if state[row][column - step] != '.'), None),
            # --x --y
            next(((column - step, row - step) for step in range(1, min([row + 1, column + 1])) if state[row - step][column - step] != '.'), None),
        ] if c]

    def get_final_state() -> List[List[str]]:
        state = get_inputs()
        while True:
            new_state = [line.copy() for line in state.copy()]
            changed = False
            for row, seat_row in enumerate(state):
                for column, status in enumerate(seat_row):
                    if status == '.':
                        continue
                    surrounding_coordinates = get_surrounding_chairs(column, row)
                    if status == 'L' and all(state[y][x] == 'L' for x, y in surrounding_coordinates):
                        new_state[row][column] = '#'
                        changed = True
                    elif status == '#' and [state[y][x] == '#' for x, y in surrounding_coordinates].count(True) >= 5:
                        new_state[row][column] = 'L'
                        changed = True
                    else:
                        pass
            if not changed:
                return new_state
            else:
                state = new_state

    final_state = get_final_state()

    occupied_state = sum([r.count('#') for r in final_state])

    print(f'Puzzle two, the state to have {occupied_state} occupied seats')


def main():
    get_inputs()
    start_1 = time()
    puzzle_one()
    print(f'Solved puzzle one in {math.ceil((time() - start_1) * 1000)}ms')

    start_2 = time()
    puzzle_two()
    print(f'Solved puzzle two in {math.ceil((time() - start_2) * 1000)}ms')

    print(f'Solved both puzzles in {math.ceil((time() - start_1) * 1000)}ms')


if __name__ == '__main__':
    main()
