from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Algorithms:
    def __init__(self):
        pass

    def get2LinesAngle(self, p1: QPoint, p2: QPoint, p3: QPoint, p4: QPoint):
        # Get angle between 2 vectors
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()

        # Cross product
        uv = ux * vx + uy * vy

        # Norms
        nu = (ux ** 2 + uy ** 2) ** 0.5
        nv = (vx ** 2 + vy ** 2) ** 0.5

        # Angle
        return abs(acos(uv / (nu * nv)))

    def createCH(self, pol:QPolygon):
        ch = QPolygon()

        #Find pivot
        q = min(pol, key=lambda k: k.y())

        # Initialise Pj, Pj1
        pj = q
        pj1 = QPoint(q.x()-10, q.y())

        # Appending pivot to convex hull
        ch.append(q)

        # Jarvis scan
        first_pass = True

        while pj != q or first_pass:
            first_pass = False

            # Find point maximizing omega
            omega_max = 0
            index_max = -1

            for index in range(len(pol)):
                # Compute omega angle
                omega = self.get2LinesAngle(pj1, pj, pj, pol[index])

                # Updating maximum
                if omega > omega_max:
                    omega_max = omega
                    index_max = index

            # Add vertex to convex hull
            ch.append(pol[index_max])

            # Update last two points of ch
            pj1 = pj
            pj = pol[index_max]

        return ch

    def rotate(self, pol: QPolygon, angle: float):
        # Rotate polygon vertices by angle
        pol_rot = QPolygon()

        # Browse points one by one
        for i in range(len(pol)):
            # Apply rotation matrix
            xr = pol[i].x() * cos(angle) - sin(angle) * pol[i].y()
            yr = pol[i].x() * sin(angle) + cos(angle) * pol[i].y()

            # Add point to rotated polygon
            point = QPoint(int(xr), int(yr))
            pol_rot.append(point)

        return pol_rot







