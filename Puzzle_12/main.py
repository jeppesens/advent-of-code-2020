from typing import List
from time import time
import math
from functools import lru_cache
# import numpy as np


@lru_cache()
def get_inputs() -> List[List[str]]:
    with open('Puzzle_12/puzzle-inputs.txt', 'r') as f:
        return f.read().splitlines()


def puzzle_one():
    E, S = 0, 0
    direction = 0
    for command in get_inputs():
        d, h = command[0], int(command[1:])
        if d == 'N':
            S -= h
        elif d == 'S':
            S += h
        elif d == 'E':
            E += h
        elif d == 'W':
            E -= h
        elif d == 'L':
            direction -= h
        elif d == 'R':
            direction += h
        if d == 'F':
            o, a = 0, 0
            if direction not in [90, 270]:
                a = math.cos(math.radians(direction)) * h
            if direction not in [0, 180]:
                o = math.sin(math.radians(direction)) * h
            E += a
            S += o

    manhattan_distance = abs(E) + abs(S)

    print(f'Puzzle one, ship moved the manhattan distance of {manhattan_distance}')


def puzzle_two():
    E, S = 0, 0
    WPE, WPS = 10, -1

    for command in get_inputs():
        d, h = command[0], int(command[1:])
        h = h * (-1) if d in ['L', 'W', 'N'] else h
        if d in ['N', 'S']:
            WPS += h
        elif d in ['E', 'W']:
            WPE += h
        elif d == 'F':
            E += h * WPE
            S += h * WPS
        if d in ['L', 'R']:
            while h != 0:
                if h > 0:
                    WPE, WPS = -WPS, WPE
                    h -= 90
                elif h < 0:
                    WPE, WPS = WPS, -WPE
                    h += 90

        # r = np.power(np.add(np.power(WPE, 2), np.power(WPS, 2)), 0.5)
        # angle = np.degrees(np.arctan(np.abs(np.divide(WPS, WPE))))
        # angle += h + 360
        # angle = angle - angle // 90 * 90
        # x = np.cos(np.radians(angle)) * r
        # y = np.sin(np.radians(angle)) * r

        # target_quadrant = h // 90

        # if WPS > 0 and WPE > 0:
        #     target_quadrant += 1
        # elif WPS > 0 and WPE < 0:
        #     target_quadrant += 2
        # elif WPS < 0 and WPE < 0:
        #     target_quadrant += 3
        # elif WPS < 0 and WPE > 0:
        #     target_quadrant += 4
        # target_quadrant = target_quadrant - target_quadrant // 4 * 4

        # if target_quadrant == 1:
        #     WPS = y
        #     WPE = x
        # elif target_quadrant == 2:
        #     WPS = y
        #     WPS = -x
        # elif target_quadrant == 3:
        #     WPS = -y
        #     WPE = -x
        # elif target_quadrant == 4:
        #     WPS = y
        #     WPE = -x

        # degrees = np.add(angle, h)
        # WPE = np.cos(np.radians(degrees)) * r
        # WPS = np.sin(np.radians(degrees)) * r
        # continue

    manhattan_distance = abs(E) + abs(S)

    print(f'Puzzle two, ship moved the manhattan distance of {manhattan_distance}')


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
    import debugpy
    debugpy.listen(('0.0.0.0', 10001))
    print('⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳', flush=True)
    debugpy.wait_for_client()
    print('🎉 VS Code debugger attached, enjoy debugging 🎉', flush=True)

    main()
