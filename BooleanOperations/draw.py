from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from edge import *
from typing import List
from qpointfb import *

class Draw(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.polA : List[QPointFB] = []
        self.polB : List[QPointFB] = []
        self.res : List[Edge] = []
        self.addA = True

        self.polA.append(QPointFB(0, 0))
        self.polA.append(QPointFB(200, 0))
        self.polA.append(QPointFB(200, 200))
        self.polA.append(QPointFB(0, 200))

        self.polB.append(QPointFB(100, 100))
        self.polB.append(QPointFB(300, 100))
        self.polB.append(QPointFB(300, 300))
        self.polB.append(QPointFB(100, 300))

    def switchPolygon(self):
        self.addA = not self.addA

    def mousePressEvent(self, e: QMouseEvent):
        # Get position
        x = e.position().x()
        y = e.position().y()

        #Create point
        p = QPointFB(int(x), int(y))

        #Add p to polygon A
        if self.addA:
            self.polA.append(p)

        #Add p to polygon B
        else:
            self.polB.append(p)

        # Repaint
        self.repaint()

    def paintEvent(self, e: QPaintEvent):

        # Create graphic object
        qp = QPainter(self)

        # Start draw
        qp.begin(self)

        # Set pen
        qp.setPen(Qt.GlobalColor.black)

        #Draw polygon A
        q_polA = QPolygonF()
        for p in self.polA:
            q_polA.append(p)
        qp.drawPolygon(q_polA)

        #Draw polygon B
        q_polB = QPolygonF()
        for p in self.polB:
            q_polB.append(p)
        qp.drawPolygon(q_polB)

        # Draw results
        qp.setPen(Qt.GlobalColor.red)
        for e in self.res:
            qp.drawLine(e.getStart(), e.getEnd())

        # End draw
        qp.end()

    def getPolygons(self):
        return self.polA, self.polB

    def setResults(self, edges):
        self.res = edges

    def clearResults(self):
        self.res.clear()

    def clearCanvas(self):
        self.polA.clear()
        self.polB.clear()
        self.res.clear()


