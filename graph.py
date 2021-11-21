import numpy as np
import queue as q
from vertex import Vertex
from edge import Edge

class Graph:
    def __init__(self):
        self.vertexMap =  dict()

    # Printing graph structure
    def printGraph(self):
        print("Printing Graph...")
        for key, vertex in self.vertexMap.items():
            if vertex.isUp == False:
                print(f'{key} DOWN')
            else:
                print(key)
            vertex.adj.sort(key=lambda e: e.destination)
            for edge in vertex.adj:
                if edge.isUp:
                    print(f'     {edge.destination} {edge.cost}')
                else:
                    print(f'     {edge.destination} {edge.cost} DOWN')

    # Printing reachable vertices and ignoring DOWN vertices
    def printReachables(self):
        print("printing reachables...")
        for key, vertex in self.vertexMap.items():
            self.markAllUnvisited()
            print(key)
            if vertex.isUp == True:
                self.getReachables(vertex)

    def getReachables(self, v):
        q = []
        q.append(v)
        while q:
            visitedVertex = q.pop(0)
            for edge in visitedVertex.adj:
                if edge.isUp == True:
                    adjVertex = self.vertexMap[edge.destination]
                    if adjVertex.visited == False and adjVertex.isUp == True:
                        adjVertex.visited = True
                        print(f'    {adjVertex.name}')
                        q.append(adjVertex)

    # Iterating over all vertices pairs given as input
    def createGraph(self, edges):
        for edge in edges:
            edge = edge.strip().split(" ")
            self.createEdge(edge[0], edge[1], edge[2])

    # Its initially adds edges to the graph.
    def createEdge(self, sourceName,  destName, cost):
        v = self.getVertex(sourceName)
        w = self.getVertex(destName)
        edge = Edge(sourceName, destName, cost)
        v.adj.append(edge)
        edgeReverse = Edge(destName, sourceName, cost)
        w.adj.append(edgeReverse)

    # It adds new edge to the existing graph.
    def addEdge(self, sourceName,  destName, cost):
        alreadyExists = False
        for edge in self.vertexMap[sourceName].adj:
            if edge.destination == destName:
                edge.cost = cost
                alreadyExists = True
                break
        if not alreadyExists:
            v = self.getVertex(sourceName)
            edge = Edge(sourceName, destName, cost)
            v.adj.append(edge)

    def takeEdgeUpOrDown(self, sourceName,  destName, statusToUpdate):
        edges = self.vertexMap[sourceName].adj
        for edge in edges:
            # print(f'{edge.source} >> {edge.destination}')
            if edge.destination == destName:
                edge.isUp =  statusToUpdate
                if statusToUpdate:
                    print(f'Edge from {sourceName} to {destName} is up...')
                else:
                    print(f'Edge from {sourceName} to {destName} is down...')

    def takeVertexUpOrDown(self, verName, statusToUpdate):
        vertex = self.vertexMap[verName]
        vertex.isUp = statusToUpdate
        if statusToUpdate:
            print(f'Vertex {verName} is up')
        else:
            print(f'Vertex {verName} is down')

    def deleteEdge(self, sourceName,  destName):
        edges = self.vertexMap[sourceName].adj
        for edge in edges:
            if edge.destination == destName:
                self.vertexMap[sourceName].adj.remove(edge)
                print(f'Edge from {sourceName} to {destName} is deleted...')

    # If vertexName is not present, add it to vertexMap.
    # In either case, return the Vertex.
    def  getVertex(self, vertexName):
        if vertexName not in self.vertexMap:
            v = Vertex(vertexName)
            self.vertexMap[vertexName] = v
        v = self.vertexMap[vertexName]
        return  v

    def findShortestPath(self, start, destination):
        self.resetAll()
        self.vertexMap[start].dist = 0
        self.vertexMap[start].prev = None

        for key, vertex in self.vertexMap.items():
            pq = q.PriorityQueue()
            for edge in vertex.adj:
                if edge.isUp == True and self.vertexMap[edge.destination].isUp == True:
                    pq.put((edge.cost, edge.source, edge.destination))
            while not pq.empty():
                connectingEdge = pq.get()
                if self.vertexMap[connectingEdge[2]].dist > self.vertexMap[connectingEdge[1]].dist + connectingEdge[0]:
                    self.vertexMap[connectingEdge[2]].dist = round(self.vertexMap[connectingEdge[1]].dist + connectingEdge[0], 2)
                    self.vertexMap[connectingEdge[2]].prev = self.vertexMap[connectingEdge[1]]
        self.printPath(destination)

    def printPath(self, destName):
        w = self.vertexMap[destName]
        if w is None:
            print("Destination vertex not found")
        elif np.isinf(w.dist):
            print(destName + " is unreachable")
        else:
            self.printPath_(w)
            print(f' {w.dist}')
        print()

    def printPath_(self, dest):
        if dest.prev is not None:
            self.printPath_(dest.prev)
            print(" ", end ="")
        print(dest.name, end ="")

    def resetAll(self):
        for key, vertex in self.vertexMap.items():
            self.vertexMap[key].dist = np.inf
            self.vertexMap[key].prev = None

    def markAllUnvisited(self):
        for key, vertex in self.vertexMap.items():
            self.vertexMap[key].visited = False



