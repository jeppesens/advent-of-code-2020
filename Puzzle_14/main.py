from typing import List
from time import time
import math
from functools import lru_cache


@lru_cache()
def get_inputs() -> List[List[str]]:
    with open('Puzzle_14/puzzle-inputs.txt', 'r') as f:
        return f.read().splitlines()


def puzzle_one():
    memory = dict()
    mask = None
    for command in get_inputs():
        action, value = command.split(' = ')
        if action == 'mask':
            mask = value
            continue
        memory[action] = int(''.join([c if m == 'X' else m for c, m in zip(
            [c for c in bin(int(value)).replace('0b', '').zfill(36)],
            [c for c in mask]
        )]), 2)

    values_in_mem = sum([memory[a] for a in memory])

    print(f'Puzzle one, memory value {values_in_mem}')


def puzzle_two():
    memory = {}
    mask = None
    combinations = []
    positions = []
    for command in get_inputs():
        action, value = command.split(' = ')
        if action == 'mask':
            mask = value
            exes = len([v for v in mask if v == 'X'])
            positions = [i for i, v in enumerate(mask) if v == 'X'] + [i for i, v in enumerate(mask) if v == '1']
            ones = '1'.join('' for _i in range(mask.count('1') + 1))
            combinations = [bin(i).replace('0b', '').zfill(exes) + ones for i in range(2**exes)]
            continue

        base_address = bin(int(action.replace('mem[', '').replace(']', ''))).replace('0b', '').zfill(36)
        for comb in combinations:
            a = [v for v in base_address]
            for i, v in zip(positions, [c for c in comb]):
                a[i] = v
            memory[''.join(a)] = int(value)

    values_in_mem = sum([memory[a] for a in memory])

    #  4453421803024 to high

    print(f'Puzzle two, memory value {values_in_mem}')


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
