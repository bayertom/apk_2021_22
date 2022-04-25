from pointandpolygonposition import *
from PyQt6.QtCore import *

class QPointFB(QPointF):
    def __init__(self, x:float, y:float, alpha:float = 0, beta:float = 0, position = PointAndPolygonPosition.Inside):
        super().__init__(x, y)
        self.alpha = alpha
        self.beta = beta
        self.position = position

