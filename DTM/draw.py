from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Draw (QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Building polygon
        self.pol = QPolygon()
        #self.pol.append(QPoint(0,0))
        #self.pol.append(QPoint(100, 100))
        #self.pol.append(QPoint(200, 10))

        # Convex hull of polygon
        self.ch = QPolygon()

        # Enclosing rectangle
        self.er = QPolygon()

    def getPolygon(self):
        return self.pol

    def setEnclosingRectangle(self, er: QPolygon):
        self.er = er

    def mousePressEvent(self, e: QMouseEvent):
        # Get cursor position
        x = int(e.position().x())
        y = int(e.position().y())

        # Create new point
        p = QPoint(x, y)

        # Add to polygon
        self.pol.append(p)

        # Repaint screen
        self.repaint()

    def paintEvent(self, e: QPaintEvent):
        # Create new object
        qp = QPainter(self)

        # Start draw
        qp.begin(self)

        # Set pen and brush - building
        qp.setPen(Qt.GlobalColor.blue)
        qp.setBrush(Qt.GlobalColor.gray)

        # Draw building
        qp.drawPolygon(self.pol)

        # Set pen and brush - convex hull
        qp.setPen(Qt.GlobalColor.red)
        #qp.setBrush(Qt.GlobalColor.gray)

        # Draw convex hull
        qp.drawPolygon(self.ch)

        # Set pen and brush - enclosing rectangle
        qp.setPen(Qt.GlobalColor.magenta)
        qp.setBrush(Qt.BrushStyle.NoBrush)
        qp.drawPolygon(self.er)

        # End draw
        qp.end()

