class Node:
    def __init__(self, coordenadas):
        self.x = coordenadas[0]
        self.y = coordenadas[1]
        self.z = coordenadas[2]

class Edge:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

class Wireframe:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNodes(self, nodeList):
        for node in nodeList:
            self.nodes.append(Node(node))

    def addEdges(self, edgeList):
        for (start, stop) in edgeList:
            self.edges.append(Edge(self.nodes[start], self.nodes[stop]))

    def outputNodes(self):
        print("Nodes")
        for i, node in enumerate(self.nodes):
            print(i, node.x, node.y, node.z)

    def outputEdges(self):
        print("Edges")
        for i, edge in enumerate(self.edges):
            print(i, edge.start.x, edge.start.y, edge.start.z, " - " ,
                     edge.stop.x, edge.stop.y, edge.stop.z)

if __name__ == "__main__":
    cube_nodes = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
    cube = Wireframe()
    cube.addNodes(cube_nodes)
    cube.addEdges([(n,n+4) for n in range(0,4)])
    cube.addEdges([(n,n+1) for n in range(0,8,2)])
    cube.addEdges([(n,n+2) for n in (0,1,4,5)])

    cube.outputNodes()
    cube.outputEdges()
