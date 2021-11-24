# Shortest Paths in a Network with OSPF protocol

### How to run
````
python main.py
````

### File Structure

```
OSPF-Network-Design
└── main.py
└── graph.py
└── edge.py
└── vertex.py
└── network.txt
└── README.md
```

`main.py`
  - It accepts file input through standard i/o operation which contains pairs of router and time of data trasmission bewteen them
  - It accepts user queries and does network operations accordingly on the network graph

`graph.py`
  - It contains a class used to represent network graph.
  - Creates network graph as per the input file
  - Performs netork operations such as Add Edge, Delete Edge, Edge Down, Edge Up, Vertex Down, Vertex Up
  - Computes shortest paths by OSPF protocol routes packets using Dijkstra's shortest path algorithm
  - Printing all routers and their adjacent routers
  - Printing all other reachable routers from the routers in the network

`vertex.py`
  - It contains a class to represent a router in the network.

`edge.py`
  - It contains a class to represent the link between two routers in the network.

 `network.txt`
  - It contains pairs of router which indicate linkage between them followed the time of data trasmission bewteen them
  
    ````
    <source> <destination> <transmission time>
    ````
    
### Program Design
 
### Overview of Data structure used in the solution
