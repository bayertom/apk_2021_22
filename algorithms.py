from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from math import *

class Algorithms:

    def __init__(self):
        pass

    def getPointLinePosition(self, a : QPoint, p1 : QPoint, p2 : QPoint):
        eps = 1.0e-10

        #Coordinate differences
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = a.x() - p1.x();
        vy = a.y() - p1.y();

        # Half plane test(cross product)
        t = ux * vy - vx * uy

        # Point in the left halfplane
        if t > eps:
            return 1

        #Point in the right halfplane
        if t < -eps:
            return 0;

        # Point on the line
        return -1;

    def get2LinesAngle(self, p1 : QPoint, p2 : QPoint, p3 : QPoint, p4 : QPoint ):
        # Compute angle formed by two lines

        # Coordinate differences
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()

        # Dot product
        dp = ux * vx + uy * vy

        # Norms
        nu = (ux * ux + uy * uy)**0.5
        nv = (vx * vx + vy * vy)**0.5

        # Angle
        return abs(acos(dp / (nu * nv)))

    def getPositionWinding(self, q : QPoint, pol : QPolygon):
        # Analyze position of point and polygon
        n = len(pol)
        omega_sum = 0

        # Process all segments of polygon
        for i in range(len(pol)):
            # Angle between two line segments
            omega = self.get2LinesAngle(pol[i], q, pol[(i+1) % n], q)

            # Point and line segment position
            pos = self.getPointLinePosition(q, pol[i], pol[(i+1) % n]);

            # Point in the left halfplane
            if pos == 1:
                omega_sum += omega;
            else:
                omega_sum -= omega;

        # Point inside polygon
        eps = 1.0e-5;
        if abs(abs(omega_sum) - 2 * pi) < eps:
            return 1

        # Point outside polygon
        if abs(omega_sum) < eps:
            return 0

        # Point on the boundary
        return -1