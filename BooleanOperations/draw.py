from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from edge import *
from typing import List

class Draw(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    def mousePressEvent(self, e: QMouseEvent):
        # Get position
        x = e.position().x()
        y = e.position().y()

        #Create point
        p = QPointFB(int(x), int(y))


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
        

        #Draw polygon B
        

        #Draw results
        
        # End draw
        qp.end()

   



