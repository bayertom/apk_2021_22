from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Draw(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pol = QPolygon()

    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = int(e.position().x())
        y = int(e.position().y())

        #Create new point
        p = QPoint(x, y)

        #Add to polygon
        self.pol.append(p)

        #Repaint screen
        self.repaint()

    def paintEvent(self, e: QPaintEvent):
        #Create new object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Set pen and brush
        qp.setPen(Qt.GlobalColor.blue)
        qp.setBrush(Qt.GlobalColor.gray)

        #Draw polygon
        qp.drawPolygon(self.pol)

        #End draw
        qp.end()