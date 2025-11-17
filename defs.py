import numpy as np
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List, Optional

states = 6
dna_size = (states*24, 8)



class Sex(Enum):
    Male = auto()
    Female = auto()


class Thing(ABC):
    def __init__(self, pos: np.ndarray, id: int):

        if not isinstance(pos, np.ndarray) or pos.shape[0] != 2 or len(pos.shape) != 1:
            raise ValueError("Position must be a 2-integer vector.")

        self.pos = pos

    color = None

class Human(Thing):
    def __init__(self, pos: np.ndarray, id: int, dna: np.ndarray = np.array([]), sex: Optional[Sex] = None, energy: float = 1):

        super().__init__(pos, id)

        if dna.size == 0:
            self.dna = np.random.rand(dna_size[0], dna_size[1])
        else:
            self.dna = dna

        if sex == None:
            self.sex = np.random.randint(0, 2)
        else:
            self.sex = sex

        self.pos = pos
        self.energy = energy

        self.reprod_timeout = 0
    
    color = 3
    
    def move(self, direction: int = 0) -> None:
        shift = []
        match direction:
            case 0:
                return None
            case 1:
                shift = [-1, 1]
            case 2:
                shift = [0, 1]
            case 3:
                shift = [1, 1]
            case 4:
                shift = [-1, 0]
            case 5:
                shift = [1, 0]
            case 6:
                shift = [-1, -1]
            case 7:
                shift = [0, -1]
            case 8:
                shift = [1, -1]
            case _:
                raise ValueError("Shift must be an integer between 0 - 8.")
        self.pos += shift

    def think(self, grid: List[List[Thing]]):
        info_vector = []
        tile_number = 0
        for y in range(6):
            for x in range(6):
                if x == 2 and y == 2: break
                
                for _ in range(states+1):
                    info_vector.append(0)

                obj = grid[self.pos[1]+y-2][self.pos[0]+x-2]

                if not isinstance(obj, Thing):
                    info_vector[tile_number*states+0] = 1

                elif isinstance(obj, Human):
                    if obj.sex == Sex.Male:
                        info_vector[tile_number*states+1] = 1
                    
                    elif obj.sex == Sex.Female:
                        info_vector[tile_number*states+2] = 1
                
                elif isinstance(obj, Food):
                    info_vector[tile_number*states+3] = 1

                elif isinstance(obj, Poison):
                    info_vector[tile_number*states+4] = 1
                
                elif isinstance(obj, Wall):
                    info_vector[tile_number*states+5] = 1

                tile_number += 1


                    
class Food(Thing):
    def __init__(self, pos: np.ndarray, id: int, energy: float = 0.3):
        super().__init__(pos, id)
        self.energy = energy
    
    color = 4


class Poison(Thing):
    def __init__(self, pos: np.ndarray, id: int, energy: float = 0.3):
        super().__init__(pos, id)
        self.energy = energy
    
    color = 2

class Wall(Thing):
    def __init__(self, pos: np.ndarray, id: int):
        super().__init__(pos, id)
    
    color = 1