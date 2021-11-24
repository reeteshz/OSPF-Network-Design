# Name: Reetesh Zope
# Student ID: 801138214
# Email ID: rzope1@uncc.edu

"""
edge.py
_______
    A class used to represent a router in the network.
----------
Attributes
----------
    name : str
        A string which indicate name of the router
    adj : list
        A list contains objects of the the links connecting to adjacent vertices
    prev : object
        A object of the prev router in shortest path which help in traversing over the shortest path.
    dist : float
        stores shortest distance (cost) from the source router.
    isUp : Boolean
        a boolean flag which indicates whether router is running or down
    visited : Boolean
        a boolean flag which indicates whether the router is visited or not while traversing over network in
        order to find all reachable routers for a router in the network
"""

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
