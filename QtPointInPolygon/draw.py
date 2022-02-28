from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Draw(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pol = QPolygon()
        self.q = QPoint()
        self.add_vertex = True

    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = int(e.position().x())
        y = int(e.position().y())

        #Add new vertex
        if self.add_vertex:

            #Create new point
            p = QPoint(x, y)

            #Add to polygon
            self.pol.append(p)
        else:
            # Modify q
            self.q.setX(x)
            self.q.setY(y)

        #Repaint screen
        self.repaint()

    def paintEvent(self, e: QPaintEvent):
        #Create new object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Set pen and brush - polygon
        qp.setPen(Qt.GlobalColor.blue)
        qp.setBrush(Qt.GlobalColor.gray)

        #Draw polygon
        qp.drawPolygon(self.pol)

        # Set pen and brush - point
        qp.setPen(Qt.GlobalColor.green)
        qp.setBrush(Qt.GlobalColor.yellow)

        # Draw ellipse
        r = 5
        qp.drawEllipse(self.q.x() - r, self.q.y() - r, 2 * r, 2 * r)

        #End draw
        qp.end()

    def getQ(self):
        # Get q
        return self.q

    def getPol(self):
        # Get polygon
        return self.pol

    def setSource(self):
        self.add_vertex = not(self.add_vertex  )