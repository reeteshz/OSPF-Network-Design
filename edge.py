class Edge:
    def __init__(self, sourceVer, destinationVer, cost):
        self.source = sourceVer
        self.destination = destinationVer
        self.isUp = True
        self.cost = float(cost)    #  Distance of path

    def Edge(self, sourceVer, destinationVer, status, transCost):
        self.source = sourceVer
        self.destination = destinationVer
        self.isUp = status
        self.cost = float(transCost)
