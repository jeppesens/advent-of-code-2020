from typing import List
from time import time
import math
from functools import lru_cache


@lru_cache()
def get_inputs() -> List[List[str]]:
    with open('Puzzle_13/puzzle-inputs.txt', 'r') as f:
        lines = f.read().splitlines()
        return (
            int(lines[0]),
            [int(b) if b != 'x' else b for b in lines[1].split(',')]
        )


def puzzle_one():
    earliest_departure, buses = get_inputs()
    buses = [b for b in buses if b != 'x']
    bus = sorted([(bus, earliest_departure // bus * bus - earliest_departure + bus) for bus in buses], key=lambda x: x[1], reverse=True).pop()
    print(f'Puzzle one, next bus is {bus[0]} leaves in {bus[1]} with answer {bus[0] * bus[1]}')


def puzzle_two():
    buses = get_inputs()[1]
    buses = [(bus, bus - i) for i, bus in enumerate(buses) if bus != 'x']

    p = math.prod([bus for bus, _i in buses])
    total = sum(i * pow(p // bus, -1, bus) * (p // bus) for bus, i in buses)
    t = total % p
    # 905694340256752
    print(f'Puzzle two, the time t where all buses leave after eachother is {t}')


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
