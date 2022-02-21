import select

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Draw(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pol = QPolygon()

    def mousePressEvent(self, e:QMouseEvent):
        #Get position
        x = e.position().x()
        y = e.position().y()

        #Create new polygon
        p = QPoint(x, y)

        #Add polygon to the list
        self.pol.append(p)

        #Repaint
        self.repaint()

    def paintEvent(self, e: QPaintEvent):

        #Create graphic object
        qp = QPainter(self)

        #Set parameters
        qp.setPen(Qt.GlobalColor.red)
        qp.setBrush(Qt.GlobalColor.yellow)

        #Start draw
        qp.begin(self)
        qp.drawPolygon(self.pol)

        #End draw
        qp.end()

    def getPol(self):
        return self.pol
