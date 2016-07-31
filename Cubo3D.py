import math

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

    def translate(self, axis, d):
        """ Add constant 'd' to the coordinate 'axis' of each node of a wireframe """
        
        if axis in ['x', 'y', 'z']:
            for node in self.nodes:
                setattr(node, axis, getattr(node, axis) + d)

    def find_center (self):
        num_nodes = len(self.nodes)

        meanX = sum([node.x for node in self.nodes])/num_nodes
        meanY = sum([node.y for node in self.nodes])/num_nodes
        meanZ = sum([node.z for node in self.nodes])/num_nodes

        return(meanX, meanY, meanZ)

    def rotateX(self, radians):
        meanXYZ = self.find_center()
        
        meanX = meanXYZ[0]
        meanY = meanXYZ[1]
        meanZ = meanXYZ[2]

        for node in self.nodes:
            y = node.y - meanY
            z = node.z - meanZ

            d = math.hypot(y,z)
            theta = math.atan2(y,z) + radians

            node.z = meanZ + d * math.cos(theta)
            node.y = meanY + d * math.sin(theta)

    def rotateY(self, radians):
        meanXYZ = self.find_center()
        
        meanX = meanXYZ[0]
        meanY = meanXYZ[1]
        meanZ = meanXYZ[2]

        for node in self.nodes:
            x = node.x - meanX
            z = node.z - meanZ

            d = math.hypot(x,z)
            theta = math.atan2(x,z) + radians

            node.z = meanZ + d * math.cos(theta)
            node.x = meanX + d * math.sin(theta)

    def rotateZ(self, radians):
        meanXYZ = self.find_center()
        
        meanX = meanXYZ[0]
        meanY = meanXYZ[1]
        meanZ = meanXYZ[2]

        for node in self.nodes:
            x = node.x - meanX
            y = node.y - meanY

            d = math.hypot(x,y)
            theta = math.atan2(x,y) + radians

            node.y = meanY + d * math.cos(theta)
            node.x = meanX + d * math.sin(theta)

    def scale(self, scale):
        """ Scale the wireframe from the centre of the screen """
        
        meanXYZ = self.find_center()

        meanX = meanXYZ[0]
        meanY = meanXYZ[1]
        meanZ = meanXYZ[2]
        
        for node in self.nodes:
            node.x = meanX + scale * (node.x - meanX)
            node.y = meanY + scale * (node.y - meanY)
            node.z = meanZ + scale * (node.z - meanZ)


if __name__ == "__main__":
    cube_nodes = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
    cube = Wireframe()
    cube.addNodes(cube_nodes)
    cube.addEdges([(n,n+4) for n in range(0,4)])
    cube.addEdges([(n,n+1) for n in range(0,8,2)])
    cube.addEdges([(n,n+2) for n in (0,1,4,5)])

    cube.outputNodes()
    cube.outputEdges()
