# Shortest Paths in a Network with OSPF protocol

````
Name: Reetesh Gopal Zope
Student ID: 801138124
````

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
  - It contains pairs of routers which indicate linkage between them followed the time of data transmission between them
  
    ````
    <source> <destination> <transmission time>
    ````
    
### Program Design

As per the given problem statement, we needed to create data communication network that must route data packets. 
The network consists of routers connected by physical cables or links. A router can act as a source, a destination, or a 
forwarder of data packets. Here, ***class Vertex*** represents a router in the network and ***class Edge*** represents link 
between two routers. ***class main*** accepts user inputs and call respective functions. Links between two routers are 
provided in simple text file. <br>
The input is passed to ***createGraph*** function which call ***createEdge*** function iteratively for every link. 
***createEdge*** checks whether ***vertexMap*** (a dictionary which hold all router objects) already contains both the 
vertices. If not, it creates new vertices and append to ***vertexMap***. Then it creates respective edges and append it 
to list ***adj*** (it contains all outgoing links) of the vertices. This way all routers and links between are added in
order to construct network graph.

This is a data communication network. So, we need to handle cases when router is down or link between two routers is 
down. Specific function are created in order to make changes to the existing network to mimic various router failure or link
down situations. 
- ***takeEdgeUpOrDown*** - It updates the status(up/down) of link connecting two routers in our data communication network
  - Link UP Query : `edgeup <source-name> <destination-name>`
  - Link Down Query : `edgedown <source-name> <destination-name>`
- ***takeVertexUpOrDown*** - It updates the status(up/down) a router in our data communication network
  - Router UP Query : `vertexup <vertex-name>`
  - Router Down Query : `vertexdown <vertex-name>`
- ***addEdge*** - It add new links to the network. If link is already present then it just updates data transmission time
over that link
  - Add Link Query : `addedge <source-name> <destination-name> <trasmission-time>`
- ***deleteEdge***  - It removes link between two routers in our data communication network
  - Delete Link Query : `deletedge <source-name> <destination-name>

To get overview of our network communication, there are two useful methods:
- ***printGraph*** - It prints each router (vertex) in the network and its adjacent routers. It is performed iterating
over vertexMap and accessing adj list of each router which gives outgoing links from the router. Destination of the outgoing
link gives adjacent router information. Likewise, we can print each router in the network and its adjacent routers.
- ***printReachables*** - It prints each router (vertex) and all the other reachable routers in the network from it. It
one router at time and apply BFS algorithm by considering the router as a start point in order to find all reachable routers 
from it. Process is repeated for reach router

Finding the shortest path in a data communication network with OSPF protocol, Dijkstra's shortest path algorithm is used.
While finding the shortest path, it avoids down links and down routers. 
- ***findShortestPath*** - It sets transmission time of starting router as 0 and previous router as None. Here, all 
routers (vertices) in the vertexMap are added to priority queue.  As Dijkstra's is a greedy algorithm it pops out next 
router from priority queue with the smallest transmission time. It checks all adjacent routers (vertices) and updates 
their the dist attribute and set prev router attribute if it is greater than transmission time data over current path. 
It repeats same process until priority queue is empties.

- ***heapDecreaseKey*** -  Here, Python's standard library heapq is used for priority queue implementation. Whenever, 
dist attribute of any router (vertex) changes, the position of the router (vertex) in the priority queue should also change.
One way to do it is heapify. But as only router's value changes every iteration, it wouldn't be an efficient approach to 
use heapify. As we are finding the shortest path. Router's dist value will be always less that its previous value. So, 
Decrease Key Algorithm is used here. It moves the router with the changed dist value at appropriate position in priority
queue.

### Overview of Data structure used in the solution
Following data structure types have been used in this project:
- ***Graph*** -  We are building a data communication network which has router/forwarders and links connecting to them.
Graph is the best data structure to implement it where vertex can be a router/forwarder and edge can be a link between 
two routers

- ***Hashmap*** - We're keeping all routers (vertices) as key-value pair in vertexMap dictionary. Where key is router name
value is object of the router

- ***Queue*** - While finding all other reachable routers from each router, we are running BFS algorithm. It is using queue
to keep track of adjacent routers (vertices) which are yet to be explored.

- ***Priority Queue*** - Here, Dijkstra's shortest path algorithm is used. It is a greedy algorithm with picks next router
(vertex) with the smallest dist attribute. Priority Queue is can be the best bet in this case because it maintains all nodes
in ascending order if implemented using binary min-heap. Rearrangement of the elements in the priority queue can be done
by Decrease Key Algorithm whenever required.
