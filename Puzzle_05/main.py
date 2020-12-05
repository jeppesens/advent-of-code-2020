from typing import List
from time import time
import math


def get_inputs() -> List[str]:
    with open('Puzzle_05/puzzle-inputs.txt', 'r') as f:
        lines = f.read().splitlines()
        return lines


def puzzle_one(inputs: List[str]):
    highest_id = max([int(place[:7].replace('B', '1').replace('F', '0'), 2) * 8 + int(place[7:].replace('R', '1').replace('L', '0'), 2) for place in inputs])
    print(f'Puzzle one has the highest id of {highest_id}')


def puzzle_two(inputs: List[str]):
    vacant_seat_ids = [r * 8 + c for r in range(0, 127) for c in range(0, 8) if f'{r:b}'.zfill(7).replace('1', 'B').replace('0', 'F') + f'{c:b}'.zfill(3).replace('1', 'R').replace('0', 'L') not in inputs]
    possible_seats = [s for s in vacant_seat_ids if s + 1 not in vacant_seat_ids and s - 1 not in vacant_seat_ids]
    for possible in possible_seats:
        print(f'Puzzle two a possible seat with id {possible}')


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
