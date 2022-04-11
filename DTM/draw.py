from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from random import *

from typing import List
from qpoint3d import *
from edge import *

from typing import List
from qpoint3d import *
from edge import *

class Draw (QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.points : List[QPoint3D] = []       #Input points
        self.dt : List[Edge] = []               #Delaunay edges
        self.cont_lines : List[Edge] = []       #Contour lines
<<<<<<< Updated upstream

        #self.points.append(QPoint3D(0.0,0.0))
        #self.points.append(QPoint3D(400, 0))
        #self.points.append(QPoint3D(200, 400))
        #self.points.append(QPoint3D(200, 200))

    def getPoints(self):
        return self.points

    def setDT(self, dt):
        self.dt = dt
=======

        #self.points.append(QPoint3D(0.0,0.0))
        #self.points.append(QPoint3D(400, 0))
        #self.points.append(QPoint3D(200, 400))
        #self.points.append(QPoint3D(200, 200))

    def getPoints(self):
        return self.points

    def getDT(self):
        return self.dt

    def setDT(self, dt):
        self.dt = dt

    def setCL(self, cont_lines):
        self.cont_lines = cont_lines
>>>>>>> Stashed changes

    def mousePressEvent(self, e: QMouseEvent):
        # Get cursor position
        x = e.position().x()
        y = e.position().y()

        # Create new point
<<<<<<< Updated upstream
        p = QPoint3D(x, y, 0.0)
=======
        p = QPoint3D(x, y, 500*random())
>>>>>>> Stashed changes

        # Add to polygon
        self.points.append(p)

        # Repaint screen
        self.repaint()

    def paintEvent(self, e: QPaintEvent):
        # Create new object
        qp = QPainter(self)

        # Start draw
        qp.begin(self)

        # Set pen and brush - building
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.white)

        # Draw points
        radius = 5
        for p in self.points:
            qp.drawEllipse(int(p.x()- radius), int(p.y()) - radius, 2 * radius, 2 * radius)

        #Draw Delaunay edges
        qp.setPen(Qt.GlobalColor.green)
        for e in self.dt:
            qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))
            #qp.drawLine(QPointF(e.getStart()), QPointF(e.getEnd()))

        # Draw contour lines
        qp.setPen(Qt.GlobalColor.black)
        for e in self.cont_lines:
            qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))

        # End draw
        qp.end()