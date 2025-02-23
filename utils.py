# utils.py
#
# Some bits and pieces that are used in different places in the code.
#
# Written by: Simon Parsons
# Modified by: Helen Harman
# Last Modified: 01/02/24

import random
import math
from enum import Enum

# representation of game state
class State(Enum):
    PLAY = 0
    FINISHED  = 1
    
    

# Class to represent the position of elements within the game
#
class Pose():
    x = 0
    y = 0

    
    def __init__(self, *args): 
        if len(args) > 1:
            self.x = args[0]
            self.y = args[1]
        
        
        
    def print(self):
        print('[', self.x, ',', self.y, ']')
        
    
    def __repr__(self):
        return f"<Pose x:{self.x} y:{self.y}>"
            
    def __str__(self):
        return f"[{self.x},{self.y}]"
        
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Pose):
            return (self.x == other.x and self.y == other.y)
        return False


# Check if two game elements are in the same location
def sameLocation(pose1, pose2):
    return pose1 == pose2



# Define the order over two locations/poses by distance from origin
def ltPose(pose):
    origin = Pose()
    return separation(pose, origin)
    
# Return distance between two game elements.
def separation(pose1, pose2):
    return math.sqrt((pose1.x - pose2.x) ** 2 + (pose1.y - pose2.y) ** 2)

# Make sure that a location doesn't step outside the bounds on the world.
def checkBounds(max, dimension):
    if (dimension > max):
        dimension = max
    if (dimension < 0):
        dimension = 0

    return dimension

# Pick a location in the range [0, x] and [0, y]
#
# Used to randomize the initial conditions.
def pickRandomPose(x, y):
    p = Pose()
    p.x = random.randint(0, x)
    p.y = random.randint(0, y)

    return p

# Pick a unique location, in the range [0, x] and [0, y], given a list
# of locations that have already been chosen.

def pickUniquePose(x, y, taken):
    uniqueChoice = False
    while(not uniqueChoice):
        candidatePose = pickRandomPose(x, y)
        if not containedIn(candidatePose, taken):
            uniqueChoice = True
    return candidatePose

# Check if a pose with the same x and y is already in poseList.
#
def containedIn(pose, poseList):
    return pose in poseList
