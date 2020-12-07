from typing import List
from time import time
import math
import re

from functools import lru_cache


@lru_cache()
def get_inputs() -> List[str]:
    with open('Puzzle_07/puzzle-inputs.txt', 'r') as f:
        lines = f.read().splitlines()
        return lines


def puzzle_one(color: str):
    def get_parents(color: str):
        parents = []
        for line in get_inputs():
            parent_color, rest = line.split('contain')
            if not re.search(color, rest):
                continue
            parent_color = parent_color.replace(' bags', '')
            parents.append(dict(
                parents=get_parents(parent_color),
                color=color,
            ))
            parent_colors.append(parent_color)
        return parents

    parent_colors = []
    get_parents(color)
    possible_parents = len(list(set(parent_colors)))

    print(f'Puzzle one {color} has {possible_parents} possible parents')


def puzzle_two(color: str):
    bags = {}
    for line in get_inputs():
        parent_color, rest = line.split('contain')
        parent_color = parent_color.replace(' bags', '').strip()
        bags[parent_color] = dict()
        for c in rest.split(','):
            c = re.sub(r' bag.*', '', c)
            q = re.search(r'\d{1,}', c)
            if not q:
                continue
            q = q.group(0)
            c_color = re.sub(f'.*{q} ', '', c)
            bags[parent_color][c_color] = int(q)

    def get_count_of_children(p_color: str):
        return sum(bags[p_color][c_color] * (1 + get_count_of_children(c_color)) for c_color in bags[p_color])
    child_bags = get_count_of_children(color)

    print(f'Puzzle two {color} should contain {child_bags}')


def main():
    get_inputs()
    color = 'shiny gold'
    start_1 = time()
    puzzle_one(color)
    print(f'Solved puzzle one in {math.ceil((time() - start_1) * 1000)}ms')

    start_2 = time()
    puzzle_two(color)
    print(f'Solved puzzle two in {math.ceil((time() - start_2) * 1000)}ms')

    print(f'Solved both puzzles in {math.ceil((time() - start_1) * 1000)}ms')


if __name__ == '__main__':
    main()
