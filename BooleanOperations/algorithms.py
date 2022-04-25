from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *
from typing import List
from qpointfb import *
from pointlineposition import *
from pointandpolygonposition import *
from lineandlineposition import *

class Algorithms:
    def __init__(self):
        pass

    def getPointAndLinePosition(self, a:QPointFB, p1:QPointFB, p2:QPointFB):
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
            return PointLinePosition.Left_HP

        # Point in right halfplane
        if t < -eps:
            return PointLinePosition.Right_HP

        # Colinear point
        return PointLinePosition.On_Line


    def get2LinesAngle(self, p1: QPointFB, p2: QPointFB, p3: QPointFB, p4:QPointFB):
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


    def getPositionPointAndPolygon(self, q:QPointFB, pol:List[QPointFB]):
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
            return PointAndPolygonPosition.Inside

        # Point q outside polygon
        return PointAndPolygonPosition.Outside

def get2LinesIntersection(self, p1:QPointFB,p2:QPointFB,p3:QPointFB,p4:QPointFB):
    #Compute intersection of two lines, if exists

    # Directions
    ux = p2.x()-p1.x()
    uy = p2.y()-p1.y()
    vx = p4.x() - p3.x()
    vy = p4.y() - p3.y()
    wx = p1.x() - p3.x()
    wy = p1.y() - p3.y()

    # Coefficients k1, k2, k3
    k1 = vx*wy - vy*wx
    k2 = ux*wy - uy*wx
    k3 = vy*ux - vx*uy

    # Collinear lines
    eps = 1e-10
    if abs(k3) < eps:
        return LineAndLinePosition.Collinear, None

    # Compute alpha, beta
    alpha = k1 / k2
    beta = k2/ k3

    #Parallel lines
    if abs(k1) <= eps and abs(k2) <= eps:
        return LineAndLinePosition.Parallel, None

    # Line intersect
    if eps < alpha < 1-eps and eps < beta < 1-eps:
        # Get point of intersection
        x = p1.x() + alpha*ux
        y = p1.y() + alpha*uy

        Q = QPointFB(x, y, alpha, beta)

        return LineAndLinePosition.Intersect, Q

    #Skew lines
    return LineAndLinePosition.Skew, None

def updateVertices(polA:List[QPointFB], polB:List[QPointFB]):
    # Add line segment intersections to polygon vertices
    for i in range(len(polA)):
       #Create dictionary
       D = {}
       for j in range(len(polB)):

           #Get intersection
           status, I = Qself.get2LinesIntersection(polA[i], polA[(i+1)%len(polA)], polB[j], polB[(j+1)%len(polB)])