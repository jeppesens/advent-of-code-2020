from typing import List
from time import time
import math

from functools import lru_cache


@lru_cache()
def get_inputs() -> List[str]:
    with open('Puzzle_08/puzzle-inputs.txt', 'r') as f:
        lines = f.read().splitlines()
        return lines


def puzzle_one():
    inputs = get_inputs()
    handled_instructions = []

    def handle_row(index: int = 0, result: int = 0):
        try:
            if index in handled_instructions:
                return result
            row = inputs[index]
            action, arg = row.split(' ')
            operator = (-1 if arg[0] == '-' else 1)
            value = int(arg[1:])
            next_index = index + 1
            if action == 'acc':
                result += value * operator
            elif action == 'nop':
                pass
            elif action == 'jmp':
                next_index += value * operator - 1
            handled_instructions.append(index)
            return handle_row(next_index, result)
        except KeyError:
            return result

    solution = handle_row()
    print(f'Puzzle one has the value {solution}')


def puzzle_two():
    inputs = get_inputs()
    handled_instructions = []
    changed_instructions = []
    solution = None
    while solution is None:
        def handle_row(index: int = 0, result: int = 0, changed: bool = False):
            try:
                row = inputs[index]
                action, arg = row.split(' ')
                operator = (-1 if arg[0] == '-' else 1)
                value = int(arg[1:])
                next_index = index + 1

                if index in handled_instructions:
                    raise Exception('Looping')

                if index not in changed_instructions and action in ['jmp', 'nop'] and not changed:
                    if action == 'nop':
                        action = 'jmp'
                    elif action == 'jmp':
                        action = 'nop'
                    changed_instructions.append(index)
                    changed = True
                if action == 'acc':
                    result += value * operator
                elif action == 'nop':
                    pass
                elif action == 'jmp':
                    next_index += value * operator - 1
                handled_instructions.append(index)
                if index == len(inputs) - 1:
                    return result
                else:
                    return handle_row(next_index, result, changed)
            except Exception:
                while handled_instructions:
                    handled_instructions.pop()

        try:
            solution = handle_row()
        except Exception:
            pass

    print(f'Puzzle two has the value {solution}')


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
