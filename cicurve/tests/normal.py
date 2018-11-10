from unittest import TestCase

from sympy import Point2D

from cicurve.neighbourhood import Neighbourhood


class Test(TestCase):
    def test(self):
        point1 = Point2D(1, 1)
        point2 = Point2D(2, 2)

        normal = Neighbourhood(point1, [point2]).normal()

        self.assertIn(normal, [Point2D(-1, 1), Point2D(1, -1)])
