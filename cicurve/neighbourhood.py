from sympy import Point2D
from typing import List


class Neighbourhood:
    def __init__(self, center: Point2D, neighbours: List[Point2D]):
        self.center = center
        self.neighbours = list(filter(lambda item: item != center, neighbours))
        if not self.neighbours:
            raise ValueError('Point must have neighbours!')

    def normal(self) -> Point2D:
        closest = min(self.neighbours, key=lambda item: self.center.distance(item))
        return Point2D(self.center.y - closest.y, - self.center.x + closest.x)