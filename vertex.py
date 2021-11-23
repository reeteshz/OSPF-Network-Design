#  Represents a vertex in the graph.
import numpy as np

class Vertex:

    def __init__(self, name):
        self.name = name
        self.adj =  []
        self.prev = None
        self.dist = np.inf
        self.isUp = True
        self.visited = False

    def __lt__(self, other):
        return self.dist<other.dist
