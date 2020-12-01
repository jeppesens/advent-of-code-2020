from typing import List
from time import time
import math


def get_inputs() -> List[str]:
    with open('Puzzle_1/puzzle-inputs.txt', 'r') as f:
        return [int(i) for i in f.read().split('\n')]


def puzzle_two(inputs: List[int]):
    enumerated_inputs = list(enumerate(inputs))
    results = []
    for i1, v1 in enumerated_inputs:
        for i2, v2 in enumerated_inputs[i1:]:
            if v1 + v2 >= 2020:
                continue
            for _i3, v3 in enumerated_inputs[i2:]:
                if sum([v1, v2, v3]) == 2020:
                    results.append(dict(
                        v1=v1,
                        v2=v2,
                        v3=v3,
                        result=v1*v2*v3
                    ))

    for result in results:
        print(f'One solution to puzzle two is input {result["v1"]}, {result["v2"]} and {result["v3"]} with result {result["result"]}')


def puzzle_one(inputs: List[int]):
    results = []

    for i1, v1 in enumerate(inputs):
        for v2 in inputs[i1:]:
            if v1 + v2 == 2020:
                results.append(dict(
                    v1=v1,
                    v2=v2,
                    result=v1*v2,
                ))

    for result in results:
        print(f'One solution to puzzle one is input {result["v1"]} and {result["v2"]} with result {result["result"]}')


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
