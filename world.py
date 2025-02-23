# world.py
#
# A file that represents the Vacuum World, keeping track of the
# position of all the objects and the agent, and
# moving them when necessary.
#
# Written by: Simon Parsons
# Modified by: Helen Harman
# Last Modified: 01/02/24

import random
import config
import utils
from utils import Pose
from utils import State

class World():

    def __init__(self):

        # Import boundaries of the world. because we index from 0,
        # these are one less than the number of rows and columns.
        self.maxX = config.worldLength - 1
        self.maxY = config.worldBreadth - 1

        # Keep a list of locations that have been used.
        self.locationList = []

        
        # Queens        
        self.queenLocations = []
        for i in range(config.numberOfQueens):
            newLoc = utils.Pose(i, random.randint(0, self.maxY))
            self.queenLocations.append(newLoc)
            self.locationList.append(newLoc)

        # Game state
        self.status = State.PLAY

        
    #--------------------------------------------------
    # Access Methods
    #
    # These are the functions that should be used by Link to access
    # information about the world.

    # Where is the vacuum?
    def getQueenLocations(self):
        return self.queenLocations

    
            
    #------------        
            
    # Implements the move 
    def updateWorld(self, individual, fitness):
        print("fitness of displayed solution: ", fitness)
        for i in range(len(individual)): 
            self.queenLocations[i] = utils.Pose(i, individual[i])
        
        
            
            
        

        
            
