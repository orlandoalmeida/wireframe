import Wireframe as wireframe

import pygame

class Projecao:

    def __init__(self, largura, altura):
        self.largura = largura 
        self.altura = altura 
        self.screen = pygame.display.set_mode((largura,altura))
        pygame.display.set_caption('WireFrame Display')
        self.background = (0,0,0)

        self.wireframes = {}
        self.displayNodes = True
        self.displayEdges = True
        self.nodeColour = (255,255,255)
        self.edgeColour = (200,200,200)
        self.nodeRadius = 4

    def addWireframe(self, name, wireframe):
        self.wireframes[name] = wireframe

    def displayXZ(self):
        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():
            if self.displayEdges:
                for edge in wireframe.edges:
                    pygame.draw.aaline(self.screen,self.edgeColour, (edge.start.x, edge.start.z),(edge.stop.x,edge.stop.z),1)
#                    pygame.draw.aaline(self.screen,self.edgeColour, (edge.start.x, edge.start.y),(edge.stop.x,edge.stop.y),1)


            if self.displayNodes:
                for node in wireframe.nodes:
                    pygame.draw.circle(self.screen, self.nodeColour, (int(node.x), int(node.z)),self.nodeRadius, 0)                    
#                    pygame.draw.circle(self.screen, self.nodeColour, (int(node.x), int(node.y)),self.nodeRadius, 0)
                    

    def displayXY(self):
        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():
            if self.displayEdges:
                for edge in wireframe.edges:
                    pygame.draw.aaline(self.screen,self.edgeColour, (edge.start.x, edge.start.y),(edge.stop.x,edge.stop.y),1)


            if self.displayNodes:
                for node in wireframe.nodes:
                    pygame.draw.circle(self.screen, self.nodeColour, (int(node.x), int(node.y)),self.nodeRadius, 0)


    def displayZY(self):
        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():
            if self.displayEdges:
                for edge in wireframe.edges:
                    pygame.draw.aaline(self.screen,self.edgeColour, (edge.start.z, edge.start.y),(edge.stop.z,edge.stop.y),1)

            if self.displayNodes:
                for node in wireframe.nodes:
                    pygame.draw.circle(self.screen, self.nodeColour, (int(node.z), int(node.y)),self.nodeRadius, 0)                                     
                    

    def run(self, eixo):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if(eixo=="xy"):
                self.displayXY()
            elif(eixo=="xz"):
                self.displayXZ()
            else:
                self.displayZY()
            
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    cube = wireframe.Wireframe()
    cube.addNodes([(x,y,z) for x in (50,250) for y in (50,250) for z in(50,250)])
    cube.addEdges([(n,n+4) for n in range(0,4)])
    cube.addEdges([(n,n+1) for n in range(0,8,2)])
    cube.addEdges([(n,n+2) for n in (0,1,4,5)])

    piramide = wireframe.Wireframe()
    piramide.addNodes([(100,100,100),(200,100,100),(100,100,200),(200,100,200),(150,75,150)])
    piramide.addEdges([(0,1),(0,2),(2,3),(1,3),(0,4),(1,4),(2,4),(3,4)])

    print("Coordenadas do Cubo")
    cube.outputNodes()
    cube.outputEdges()

    print("Coordenadas da Piramide")
    piramide.outputNodes()
    piramide.outputEdges()

    pv = Projecao(400,300)
    pv.addWireframe('cube',cube)
    pv.addWireframe('piramide',piramide)
    
    pv.run('xz')
