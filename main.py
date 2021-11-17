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
        elif command[0] == "deleteedge ":
            print(f'Deleting edge from {command[1]} to {command[2]}...')
        elif command[0] == "edgedown":
            print(f'Edge from {command[1]} to {command[2]} is down...')
        elif command[0] == "edgeup":
            print(f'Edge from {command[1]} to {command[2]} is up...')
        elif command[0] == "vertexdown":
            print(f'Vertex {command[1]} is down')
        elif command[0] == "vertexup":
            print(f'Vertex {command[1]} is up')
        elif command[0] == "reachable":
            print("printing reachables...")
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
