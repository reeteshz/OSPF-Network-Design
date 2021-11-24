# Name: Reetesh Zope
# Student ID: 801138214
# Email ID: rzope1@uncc.edu

"""
edge.py
_________
    A class used to represent the link between two routers in the network.
----------
Attributes
----------
    source : str
        A string which contains source router name of the link
    destination : list
        A string which contains destination router name of the link
    isUp : object
        A boolean flag which indicates whether link bewteen the routers is up/down
    cost : float
        A float value which indicates data transmission cost between two routers
"""

class Edge:
    def __init__(self, sourceVer, destinationVer, cost):
        self.source = sourceVer
        self.destination = destinationVer
        self.isUp = True
        self.cost = float(cost)
