import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from defs import Thing, Sex, Human, Food, Poison
from enum import Enum, auto
import random
from typing import List, Optional

grid_size = 50
start_players_avg = 20

colors = [
    (1.0, 1.0, 1.0),        # 0: white background
    (0.0, 0.0, 0.0),        # 1: black walls
    (0.0, 1.0, 0.0),        # 2: green poison
    (0.957, 0.859, 0.609),  # 3: human color
    (0.0, 0.0, 1.0),        # 4: blue food
]

things_ids = {}
next_id = 0
cmap = ListedColormap(colors)

def grid_to_array():
    arr = np.zeros((grid_size+1, grid_size+1))

    for y in range(grid_size+1):
        for x in range(grid_size+1):
            obj = grid[y][x]

            if isinstance(obj, Thing):
                arr[y, x] = obj.color
            else:
                arr[y, x] = 0

    return arr


grid: List[List[Optional[Thing]]] = [[None for _ in range(grid_size+1)] for _ in range(grid_size+1)]

for y, row in enumerate(grid):
    for x, el in enumerate(row):
        if random.random() < start_players_avg/(grid_size*grid_size):

            obj = Human(np.array([x, y]), next_id)
            things_ids[next_id] = obj
            grid[y][x] = obj

            next_id += 1

arr = grid_to_array()

fig, ax = plt.subplots()
img = ax.imshow(arr, cmap=cmap, vmin=0, vmax=len(colors)-1)
plt.show()



