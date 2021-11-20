#  Represents a vertex in the graph.
import numpy as np

class Vertex:
    def __init__(self, name):
        self.name = name    #  Vertex name
        self.adj =  []    #  Adjacent vertices
        self.prev = None    #  Previous vertex on shortest path
        self.dist = np.inf    #  Distance of path
        self.isUp = True
        self.visited = False

    def Vertex(self, name):
        self.name = name
        adj = []
