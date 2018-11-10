from typing import List
from copy import copy
from sympy import Point2D


class CIC:
    def __init__(self, points: List[Point2D]):
        self.points = points

    def streamline(self):
        points = copy(self.points)
        start = points[0]
        sorted = [start]
        while points:
            pass
