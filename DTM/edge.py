from PyQt6.QtCore import *
from qpoint3d import *

#Triangle edge (oriented)
class Edge:
    def __init__(self, start: QPoint3D, end: QPoint3D):
        self.start = start
        self.end = end

    def getStart(self):
        #Return start point
        return self.start

    def getEnd(self):
        # Return end point
        return self.end

    def switch(self):
        #Change edge orientation
        temp = self.start
        self.start = self.end
        self.end = temp
