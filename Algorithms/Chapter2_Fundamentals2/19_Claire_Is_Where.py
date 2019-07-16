# Create four functions - reset(), moveBy(), xLocation(), and yLocation(), to track the travels of Claire, our wanderer.  Calling reset() moves Claire home to origin (0,0). The moveBy(xDiff, yDiff) moves her by those amounts, in those directions. Finally, xLocation() and yLocation() returns how far Claire is from home, in X and Y directions respectively. After the calls of reset(), moveBy(1,-2) and moveBy(3,1), calling xLocation() and yLocation() should return 4 and -1. Create distanceFromHome() - assuming she moves diagonally, return distance from home.
import math

class Journey:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0

    def reset(self):
        self.xPos = 0
        self.yPos = 0
        return self

    def moveBy(self, xDiff, yDiff):
        self.xPos += xDiff
        self.yPos += yDiff
        return self

    def xLocation(self):
        print("X-Postion:", self.xPos)
        return self

    def yLocation(self):
        print("Y-Postion:", self.yPos)
        return self

    def distanceFromHome(self):
        distance = round(math.sqrt(self.xPos**2 + self.yPos**2),2)
        print("You are", distance, "away from home")
        return self

# Test Cases
claire = Journey()
claire.moveBy(1,-2).moveBy(3,1)
claire.xLocation().yLocation()
claire.distanceFromHome()
