# config.py
#
# Configuration information for the Wumpus World. These are elements
# to play with as you develop your solution.
#
# Written by: Simon Parsons
# Modified by: Helen Harman
# Last Modified: 01/02/24

import random
from enum import Enum

class MODE(Enum):
    SELECTION_TEST = 0
    CROSSOVER_TEST = 1 # test will use a crossoverRate of 1
    MUTATION_TEST = 2  # test will use a mutationRate of 1
    RUN_GA = 3

# Dimensions in terms of the numbers of rows and columns
worldLength = 8
worldBreadth = 8

numberOfQueens = worldLength
numberOfLocations = worldBreadth

populationSize = 50
numberOfGenerations = 10
crossoverRate = 0.3
mutationRate = 0.1


displayBestAfterEachGeneration = True

mode = MODE.SELECTION_TEST
