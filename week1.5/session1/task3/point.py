# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """
    x = 0
    y = 0
    # Add constructor here
    def __init__(self,x,y):
        self.x = x
        self.y = y
    # Add distance() method here
    def distance(self,point = {0,0}):
        return math.sqrt(pow(self.x-point[0],2)+pow(self.y-point[1],2))

    # Add distance_to() method here
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
