# Name: Reetesh Zope
# Student ID: 801138214
# Email ID: rzope1@uncc.edu

"""
graph.py
________
    - It contains a class used to represent network graph.
    - Creates network graph as per the input file
    - Performs netork operations such as Add Edge, Delete Edge, Edge Down, Edge Up, Vertex Down, Vertex Up
    - Computes shortest paths by OSPF protocol routes packets using Dijkstra's shortest path algorithm
    - Printing all routers and their adjacent routers
    - Printing all other reachable routers from the routers in the network

Attributes
----------
    vertexMap : dict
        A dictonary which contains all routers in the network
"""

import numpy as np
from vertex import Vertex
from edge import Edge
import heapq

class Graph:
    def __init__(self):
        self.vertexMap =  dict()

    # Shows network graph structure. Prints all routers and their adjacent routers
    def printGraph(self):
        for key, vertex in sorted(self.vertexMap.items()):
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

    """ Printing all other reachable routers from the routers in the network
   
    Time Complexity : O(V * (V + E))
    ---------------
        To print all other reachable routers from the routers in the network, simple 
        Breadth First Search algorithm is used. BFS has time complexity of O(|V+E|)
        when adjacency matrix is used. We do this for all the vertices (routers) in 
        the network graph. So time complexity of printReachables() is O(V * (|V + E|))
    """
    def printReachables(self):
        for key, vertex in sorted(self.vertexMap.items()):
            self.markAllUnvisited()
            print(key)
            if vertex.isUp == True:
                reached = self.getReachables(vertex)
                reached = sorted(reached)
                print("   " , end = '')
                print(*reached, sep = "\n   ")

    """Collecting all reachable routers from a particular router
    
    Parameters
    ----------
    v : str
        Object of the router from which all reachable routers in the network to be found
    
    Returns
    -------
    list
        a list of names of all routers which are reachable from the given router
    """
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

    """Routing function to create network graph from given pairs of the router which indicates direct link bewteen them
    
    Parameters
    ----------
    v : list
        A list contains directed link pairs and trasmission cost as read from file input
    """
    def createGraph(self, edges):
        for edge in edges:
            edge = edge.strip().split(" ")
            self.createEdge(edge[0], edge[1], edge[2])

    # Creates routing network as per the input
    """Creates router if not already present the newtwork. Add bidirectional link between them
    
    Parameters
    ----------
    sourceName : string
        A string indicates name of the source router
    destName : string
        A string indicates name of the destination router
    cost : float
        A float value indicates transmission cost to send data over link bewteen source and destination router
    """
    def createEdge(self, sourceName,  destName, cost):
        v = self.getVertex(sourceName)
        w = self.getVertex(destName)
        edge = Edge(sourceName, destName, cost)
        v.adj.append(edge)
        edgeReverse = Edge(destName, sourceName, cost)
        w.adj.append(edgeReverse)

    """Adds directed link bewteen given pair of routers in the network. 
    Updates cost of transmission if link bewteen the routers already exists
    
    Parameters
    ----------
    sourceName : string
        A string indicates name of the source router
    destName : string
        A string indicates name of the destination router
    cost : float
        A float value indicates transmission cost to send data over link bewteen source and destination router 
    """
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

    """Updates up/down status of a link between two routers
    
    Parameters
    ----------
    sourceName : string
        A string indicates name of the source router of the link
    destName : string
        A string indicates name of the destination router of the link
    statusToUpdate : boolean
        A boolean value indicates link status (Up/Down) to be upadted
    """
    def takeEdgeUpOrDown(self, sourceName,  destName, statusToUpdate):
        edges = self.vertexMap[sourceName].adj
        for edge in edges:
            if edge.destination == destName:
                edge.isUp =  statusToUpdate
                if statusToUpdate:
                    print(f'Link from {sourceName} to {destName} is up...')
                else:
                    print(f'Link from {sourceName} to {destName} is down...')

    """Updates up/down status of a router
    
    Parameters
    ----------
    verName : string
        A string indicates name of the router
    statusToUpdate : boolean
        A boolean value indicates router status (Up/Down) to be upadted
    """
    def takeVertexUpOrDown(self, verName, statusToUpdate):
        vertex = self.vertexMap[verName]
        vertex.isUp = statusToUpdate
        if statusToUpdate:
            print(f'{verName} router is up')
        else:
            print(f'{verName} router is down')

    """Removes a link between two routers
    
    Parameters
    ----------
    sourceName : string
        A string indicates name of the source router of the link
    destName : string
        A string indicates name of the destination router of the link
    """
    def deleteEdge(self, sourceName,  destName):
        edges = self.vertexMap[sourceName].adj
        for edge in edges:
            if edge.destination == destName:
                self.vertexMap[sourceName].adj.remove(edge)
                print(f'Link from {sourceName} to {destName} is removed...')

    """ If router is not present, add it to network router map.
    In either case, return the router.
    
    Parameters
    ----------
    vertexName : string
        A string indicates name of the router
    
    Returns
    -------
    Object
        a object of the router(vertex class)
    """
    def  getVertex(self, vertexName):
        if vertexName not in self.vertexMap:
            v = Vertex(vertexName)
            self.vertexMap[vertexName] = v
        v = self.vertexMap[vertexName]
        return  v

    """ Computes shortest paths by OSPF protocol routes packets using Dijkstra's shortest path algorithm
    
    Parameters
    ----------
    start : string
        A string indicates name of the router from which data is trasmitted
    destination : string
        A string indicates name of the router by which data is to be received
    
    Time Complexity : O(V + E log V)
    ---------------
        To find shortest path from source router to destination router to transmit data, we are using Dijkstra's 
        shortest path algorithm. It is similar to BFS algorithm whose time complexity is O(V + E). Here, we are using 
        priority queue implementation using min-heap to get router with shortest distance from source vertex. To main 
        min-heap, we need to perform Decrease-Key operation whenever router shortest path distance from the source 
        router reduces. Decrease-Key operation takes O(log V) time. In worst case, scenario the operation will be 
        perform for each edge. So running time complexity of shortest path algorithm using priority queue is O((V + E log V))
    """
    def findShortestPath(self, start, destination):
        self.resetAll()
        if self.vertexMap[start].isUp != False:
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
        else:
            print(f'{start} is down')

    """ Driver routine to print total distance shortest distance and path bewteen two routers.
    
    Parameters
    ----------
    destName : string
        A string indicates name of the destination router
    """
    def printPath(self, destName):
        w = self.vertexMap[destName]
        if w is None:
            print("Destination not found")
        elif np.isinf(w.dist):
            print(destName + " is unreachable")
        else:
            self.printPath_(w)
            print(f' {w.dist}')

    """ Traverse recursively from destination router to source router and prints the shorted distance path
    
    Parameters
    ----------
    dest : string
        A string indicates name of the destination router
    """
    def printPath_(self, dest):
        if dest.prev is not None:
            self.printPath_(dest.prev)
            print(" ", end ="")
        print(dest.name, end ="")

    # Resets distance and parent of each router before calculating shortest distance.
    def resetAll(self):
        for key, vertex in self.vertexMap.items():
            self.vertexMap[key].dist = np.inf
            self.vertexMap[key].prev = None

    # Marks all routers unvisited
    def markAllUnvisited(self):
        for key, vertex in self.vertexMap.items():
            self.vertexMap[key].visited = False

    """ Rearranges the position of router in the heap when shortest distance from the source decreases from the previous
    value
    
    Parameters
    ----------
    heap : list
        A list maintains min-heap of routers having router with shortest distance from the source router as a root
    i : int
        A int value index of the router in heap whose shortest distance value is updated
    key : float
        A float value updated cost of tranmission over shortest path from the source router to the current router
        
    Time Complexity : O(log V)
    ---------------
        To main the proper priority queue using min-heap, we need perform Decrease-Key operation so that router with the
        shorted distance from the source router is at the top of the queue. In worst case, it takes O(log V) time in order
        to move element from a leaf position to root position
    """
    def heapDecreaseKey(self, heap, i, key):
        if key > heap[i].dist:
            return
        heap[i].dist = key
        while i > 0 and heap[(i-1)//2].dist > heap[i].dist:
            heap[i], heap[(i-1)//2] = (heap[(i-1)//2], heap[i])
            i = (i-1)//2



