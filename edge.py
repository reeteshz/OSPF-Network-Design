class Edge:
    def __init__(self, sourceVer, destinationVer, cost):
        self.source = sourceVer
        self.destination = destinationVer
        self.isUp = True
        self.cost = float(cost)
