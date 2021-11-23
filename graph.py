import numpy as np
from vertex import Vertex
from edge import Edge
import heapq

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
                reached = self.getReachables(vertex)
                reached = sorted(reached)
                print("   " , end = '')
                print(*reached, sep = "\n   ")

    def getReachables(self, v):
        q = []
        q.append(v)
        reached = []
        while q:
            visitedVertex = q.pop(0)
            for edge in visitedVertex.adj:
                if edge.isUp == True:
                    adjVertex = self.vertexMap[edge.destination]
                    if adjVertex.visited == False and adjVertex.isUp == True:
                        adjVertex.visited = True
                        reached.append(adjVertex.name)
                        q.append(adjVertex)
        return reached

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
                edge.cost = float(cost)
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
        heap = [v for v in self.vertexMap.values()]
        heapq.heapify(heap)
        while len(heap) != 0:
            vertex = heapq.heappop(heap)
            for connectingEdge in vertex.adj:
                if (self.vertexMap[connectingEdge.destination].dist > vertex.dist + connectingEdge.cost) and (connectingEdge.isUp == True and self.vertexMap[connectingEdge.destination].isUp == True):
                    self.vertexMap[connectingEdge.destination].dist = round(vertex.dist + connectingEdge.cost, 2)
                    self.vertexMap[connectingEdge.destination].prev = vertex
                    self.heapDecreaseKey(heap, heap.index(self.vertexMap[connectingEdge.destination]), self.vertexMap[connectingEdge.destination].dist)
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

    def heapDecreaseKey(self, heap, i, key):
        if key > heap[i].dist:
            return
        heap[i].dist = key
        while i > 0 and heap[(i-1)//2].dist > heap[i].dist:
            temp = heap[(i-1)//2]
            heap[(i-1)//2] = heap[i]
            heap[i] = temp
            i = (i-1)//2



