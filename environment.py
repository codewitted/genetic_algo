# environment.py
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
import config  # Import config first to avoid partial initialization issues

class Environment():

    def __init__(self, game, windowName="World"):
        print("Environment initialized")

        # Import graphics here to avoid circular import issues
        from graphics import GraphWin, Rectangle, Line, Image, Point

        # Make a copy of the world an attribute, so that the graphics
        # have access.
        self.gameWorld = game

        # How many pixels the grid is offset in the window
        self.offset = 10

        # How many pixels correspond to each coordinate.
        self.magnify = 55  # Any smaller, and the images won't fit

        # How big to make "characters" when not using images
        self.cSize = 0.4

        # How big to make objects when not using images
        self.oSize = 0.6

        # Setup window and draw objects
        self.pane = GraphWin(windowName, ((2 * self.offset) + ((self.gameWorld.maxX + 1) * self.magnify)),
                             ((2 * self.offset) + ((self.gameWorld.maxY + 1) * self.magnify)))
        self.pane.setBackground("white")

        self.drawBoundary()
        self.drawGrid()
        self.drawQueens()

    #
    # Draw the world
    #

    def drawBoundary(self):
        from graphics import Rectangle, Point  # Import inside function

        rect = Rectangle(self.convert(0, 0), self.convert(self.gameWorld.maxX + 1, self.gameWorld.maxY + 1))
        rect.draw(self.pane)

    def drawGrid(self):
        from graphics import Line  # Import inside function

        # Vertical lines
        vLines = [Line(self.convert(i, 0), self.convert(i, self.gameWorld.maxY + 1)) for i in range(self.gameWorld.maxX + 1)]
        for line in vLines:
            line.draw(self.pane)

        # Horizontal lines
        hLines = [Line(self.convert(0, i), self.convert(self.gameWorld.maxX + 1, i)) for i in range(self.gameWorld.maxY + 1)]
        for line in hLines:
            line.draw(self.pane)

    #
    # Draw the agents
    #

    def drawQueens(self):
        from graphics import Image  # Import inside function

        self.queens = []
        for i in range(len(self.gameWorld.queenLocations)):
            queen_image = Image(self.convert2(self.gameWorld.queenLocations[i].x, self.gameWorld.queenLocations[i].y), "images/queen.png")
            queen_image.draw(self.pane)
            self.queens.append(queen_image)

    def update(self):
        for q in self.queens:
            q.undraw()
        self.drawQueens()

    #
    # Coordinate transformations
    #

    def convert(self, x, y):
        """Convert grid coordinates to window coordinates."""
        from graphics import Point  # Import inside function
        return Point(self.offset + (x * self.magnify), self.offset + (y * self.magnify))

    def convert2(self, x, y):
        """Convert grid coordinates to window coordinates (center of grid square)."""
        from graphics import Point  # Import inside function
        return Point((self.offset + 0.5 * self.magnify) + (x * self.magnify),
                     (self.offset + 0.5 * self.magnify) + (y * self.magnify))
