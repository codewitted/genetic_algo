# dirtyEnvironment.py
#
# Code to display information about the game in a window.
#
# Shouldn't need modifying --- only changes what gets shown, not what
# happens in the game.
#
# Written by: Simon Parsons. 
# Modified by: Helen Harman
# Last Modified: 01/02/24

from utils import Pose
from graphics import *
import config

class Environment():

    def __init__(self, game, windowName = "World"):
        # Make a copy of the world an attribute, so that the graphics
        # have access.
        self.gameWorld = game

        # How many pixels the grid if offset in the window
        self.offset = 10
        
        # How many pixels correspond to each coordinate.
        #
        # This works with the current images. any smaller and the
        # images will not fit in the grid.
        self.magnify = 55

        # How big to make "characters" when not using images
        self.cSize = 0.4

        # How big to make objects when not using images.
        self.oSize = 0.6

        # Setup window and draw objects
        self.pane = GraphWin(windowName, ((2*self.offset)+((self.gameWorld.maxX+1)*self.magnify)), ((2*self.offset)+((self.gameWorld.maxY+1)*self.magnify)))
        self.pane.setBackground("white")
        self.drawBoundary()
        self.drawGrid()
        self.drawQueens()

    #
    # Draw the world
    #
    
    # Put a box around the world
    def drawBoundary(self):
        rect = Rectangle(self.convert(0, 0), self.convert(self.gameWorld.maxX+1, self.gameWorld.maxY+1))
        rect.draw(self.pane)

    # Draw gridlines, to visualise the coordinates.
    def drawGrid(self):
        # Vertical lines
        vLines = []
        for i in range(self.gameWorld.maxX+1):
            vLines.append(Line(self.convert(i, 0), self.convert(i, self.gameWorld.maxY+1)))
        for line in vLines:
            line.draw(self.pane)
        # Horizontal lines
        hLines = []
        for i in range(self.gameWorld.maxY + 1):
            hLines.append(Line(self.convert(0, i), self.convert(self.gameWorld.maxX+1, i)))
        for line in hLines:
            line.draw(self.pane)

    #
    # Draw the agents
    #

    # We either use an image of the Queen
    def drawQueens(self):
        self.queens = []
        for i in range(len(self.gameWorld.queenLocations)):
            self.queens.append( Image(self.convert2(self.gameWorld.queenLocations[i].x, self.gameWorld.queenLocations[i].y), "images/queen.png") ) 
            self.queens[i].draw(self.pane)

    def update(self):
        for q in self.queens: 
            q.undraw()
        self.drawQueens()

    # Take x and y coordinates and transform them for using offset and
    # magnify.
    #
    # This conversion works for the lines. 
    def convert(self, x, y):
        newX = self.offset + (x * self.magnify)
        newY = self.offset + (y * self.magnify)
        return Point(newX, newY)

    # Take x and y coordinates and transform them for using offset and
    # magnify.
    #
    # This conversion works for objects, returning the centre of the
    # relevant grid square.
    def convert2(self, x ,y):
        newX = (self.offset + 0.5*self.magnify) + (x * self.magnify)
        newY = (self.offset + 0.5*self.magnify) + (y * self.magnify)
        return Point(newX, newY)
    