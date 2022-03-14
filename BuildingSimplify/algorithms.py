from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *

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
        try:
            return abs(acos(uv / (nu * nv)))
        except:
            return 0

    def createCH(self, pol:QPolygon):
        ch = QPolygon()

        #Find pivot
        q = min(pol, key=lambda k: k.y())

        # Initialise Pj, Pj1
        pj = q
        pj1 = QPoint(q.x() - 10, q.y())

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
                omega = self.get2LinesAngle(pj, pj1, pj, pol[index])

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

    def minMaxBox (self, pol: QPolygon):
        # Creating minmax box and calculating area
        # Finding extreme coordinates
        x_min = min(pol, key=lambda k: k.x()).x()
        x_max = max(pol, key=lambda k: k.x()).x()
        y_min = min(pol, key=lambda k: k.y()).y()
        y_max = max(pol, key=lambda k: k.y()).y()

        # Create vertices of bounding box
        v1 = QPoint(x_min,y_min)
        v2 = QPoint(x_max,y_min)
        v3 = QPoint(x_max, y_max)
        v4 = QPoint(x_min, y_max)

        # Area of rectangle
        a = x_max-x_min
        b = y_max-y_min
        S = a*b

        # Create QPolygon
        minmax_box = QPolygon([v1, v2, v3, v4])

        return S, minmax_box


    def minAreaEnclosingRectangle(self, pol: QPolygon):
        # Create approximation of building using minimum area enclosing rectangle
        # Create convex hull
        ch = self.createCH(pol)
        n_ch = len(ch)

        # Create initial approximation
        sigma_min = 0
        S_min, mmb_min = self.minMaxBox(ch)

        # Process all segments of convex hull
        for i in range(n_ch):
            dx = ch[(i+1)%n_ch].x()-ch[i].x()
            dy = ch[(i+1)%n_ch].y()-ch[i].y()

            # Direction of segment
            sigma_i = atan2(dy,dx)

            # Rotate by -sigma_i
            ch_rot = self.rotate(ch, -sigma_i)

            # Create MMB
            S_i, mmb_i = self.minMaxBox(ch_rot)

            # Updating minimum
            if S_i < S_min:
                S_min = S_i
                sigma_min = sigma_i
                mmb_min = mmb_i

        # Rotate mmb_min back by sigma_min
        er = self.rotate(mmb_min, sigma_min)

        # Resize mmb_res, S_mmb = S_building

        return er

    def getArea(self, pol: QPolygon):
        # Calculating area of non-convex polygon using LH formula
        n = len(pol)
        S = 0

        for i in range(n):
            dS = pol[i].x()*(pol[(i+1) % n].y()-pol[(i-1+n) % n].y())
            S += dS

        return 0.5 * S
















