# pylint: disable=redefined-outer-name
"""
aoc 2023 day 3

jakob johnson
"""

import numpy as np

symbols = ["#", "$", "%", "&", "*", "+", "-", "/", "=", "@"]


def import_grid(filename):
    with open(filename, "r", encoding="utf-8") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return np.array(grid)


def look_around(chargrid, row, col):
    """look around current position in grid and return True if there is a symbol in an adjacent cell"""
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            try:
                if chargrid[r, c] in symbols:
                    return True
            except IndexError:
                pass
    return False


def look_around_p2(chargrid, row, col):
    """look around current position in grid and return True if there is a cog symbol in an adjacent cell"""
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            try:
                if chargrid[r, c] == "*":
                    return f"{r}-{c}"
            except IndexError:
                pass
    return False


if __name__ == "__main__":
    grid = import_grid("input.txt")
    # print(grid)

    # Part 1
    total = 0
    curr_num = ""
    to_add = False

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            char = grid[r, c]
            if char.isdigit():
                curr_num += char
                to_add = to_add or look_around(grid, r, c)
            else:
                if to_add:
                    total += int(curr_num)
                curr_num = ""
                to_add = False

        if to_add:
            total += int(curr_num)
        curr_num = ""
        to_add = False

    print(f"part 1: {total}")

    # Part 2
    cogs = {}

    curr_num = ""
    pin_to_cogs = set()

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            char = grid[r, c]
            if char.isdigit():
                curr_num += char
                cog_loc = look_around_p2(grid, r, c)
                if cog_loc:
                    pin_to_cogs.add(cog_loc)
            else:
                for loc in pin_to_cogs:
                    if not loc in cogs:
                        cogs[loc] = [int(curr_num)]
                    else:
                        cogs[loc].append(int(curr_num))
                curr_num = ""
                pin_to_cogs = set()

        # at the end of each row, check if there are any cogs to connect to
        for loc in pin_to_cogs:
            if not loc in cogs:
                cogs[loc] = [int(curr_num)]
            else:
                cogs[loc].append(int(curr_num))
        curr_num = ""
        pin_to_cogs = set()

    total = 0
    for group in cogs.values():
        if len(group) == 2:
            total += group[0] * group[1]

    print(f"part 2: {total}")
