from graph import Graph

def main():
    graphObj = Graph()
    while True:
        command = input("Enter your query:")
        command = command.strip().split(" ")
        if command[0] == "addedge":
            graphObj.addEdge(command[1], command[2], command[3])
        elif command[0] == "deleteedge":
            graphObj.deleteEdge(command[1], command[2])
        elif command[0] == "edgedown":
            graphObj.takeEdgeUpOrDown(command[1], command[2], False)
        elif command[0] == "edgeup":
            graphObj.takeEdgeUpOrDown(command[1], command[2], True)
        elif command[0] == "vertexdown":
            graphObj.takeVertexUpOrDown(command[1], False)
        elif command[0] == "vertexup":
            graphObj.takeVertexUpOrDown(command[1], True)
        elif command[0] == "reachable":
            graphObj.printReachables()
        elif command[0] == "print":
            graphObj.printGraph()
        elif command[0] == "graph":
            fin = command[1]
            with open(fin) as f:
                edges = f.readlines()
                graphObj.createGraph(edges)
        elif command[0] == "path":
            graphObj.findShortestPath(command[1], command[2])
        elif command[0] == "quit":
            break
        else:
            print("Invalid command")

if __name__=="__main__":
    main()
