# A main routine that:
# 1. Reads a file containing edges (supplied as a command-line parameter);
# 2. Forms the graph;
# 3. Repeatedly prompts for two vertices and
#    runs the shortest path algorithm.
# The data file is a sequence of lines of the format
#    source destination

from graph import Graph

def main():
    graphObj = Graph()
    while True:
        command = input("Enter your command:")
        command = command.strip().split(" ")
        print(f'command is {command[0]}')
        if command[0] == "addedge":
            print(f'Adding edge from {command[1]} to {command[2]}...')
            graphObj.addEdge(command[1], command[2], command[3])
        elif command[0] == "deleteedge ":
            print(f'Deleting edge from {command[1]} to {command[2]}...')
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
        elif command[0] == "quit":
            print("Thank you!!!")
            break
        else:
            print("Invalid command")

if __name__=="__main__":
    main()
