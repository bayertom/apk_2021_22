from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *

class Algorithms:
    def __init__(self):
        pass

    def getPointAndLinePosition(self, a:QPoint, p1:QPoint, p2:QPoint):
        # Analyze position point and line
        eps = 1.0e-10

        # Coordinate differences
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = a.x() - p1.x()
        vy = a.y() - p1.y()

        # Calculating determinant
        t = ux * vy - vx * uy

        # Point in left halfplane
        if t > eps:
            return 1

        # Point in right halfplane
        if t < -eps:
            return 0

        # Colinear point
        return -1


    def get2LinesAngle(self, p1: QPoint, p2: QPoint, p3: QPoint, p4:QPoint):
        # Get angle between 2 vectors
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()

        # Dot product
        uv = ux*vx + uy*vy

        # Norms
        nu = (ux**2 + uy**2)**0.5
        nv = (vx**2 + vy**2)**0.5

        # Angle
        return abs(acos(uv/(nu*nv)))


    def getPositionPointAndPolygon(self, q:QPoint, pol:QPolygon) -> int:
        # Analyzes position of the point and polygon
        n = len(pol)
        omega_sum = 0

        # Loop through polygon nodes
        for i in range(n):

            # Analyze position of q and pi, pi+1
            pos = self.getPointAndLinePosition(q, pol[i], pol[(i+1)%n])

            # Angle between q and pi, pi+1
            omega = self.get2LinesAngle(q, pol[i], q, pol[(i+1)%n])

            # Computing winding number
            if pos == 1:
                # Point in the left halfplane
                omega_sum += omega
            else:
                # Point in the right halfplane
                omega_sum -= omega

        # Point q inside polygon
        epsilon = 1.0e-10
        if abs(abs(omega_sum)-2*pi) < epsilon:
            return 1

        # Point q outside polygon
        return 0
