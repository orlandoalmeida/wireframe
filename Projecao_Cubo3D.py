#!/bin/env python

import Cubo3D as wireframe
import pygame


key_to_function = {
    pygame.K_LEFT:   (lambda x: x.translateAll('x', -10)),
    pygame.K_RIGHT:  (lambda x: x.translateAll('x',  10)),
    pygame.K_DOWN:   (lambda x: x.translateAll('y',  10)),
    pygame.K_UP:     (lambda x: x.translateAll('y', -10)),
    pygame.K_EQUALS: (lambda x: x.scaleAll(1.25)),
    pygame.K_MINUS:  (lambda x: x.scaleAll( 0.8)),
    pygame.K_x:      (lambda x: x.set_vision('xy')),
    pygame.K_z:      (lambda x: x.set_vision('xz')),
    pygame.K_s:      (lambda x: x.rotateALLX(10)), 
    pygame.K_a:      (lambda x: x.rotateALLX(-10)),
    pygame.K_q:      (lambda x: x.rotateALLY(10)), 
    pygame.K_w:      (lambda x: x.rotateALLY(-10)),
    pygame.K_e:      (lambda x: x.rotateALLY(10)), 
    pygame.K_r:      (lambda x: x.rotateALLY(-10))}

class ProjectionViewer:
    """ Displays 3D objects on a Pygame screen """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Wireframe Display')
        self.background = (10,10,50)

        self.wireframes = {}
        self.displayNodes = True
        self.displayEdges = True
        self.nodeColour = (255,255,255)
        self.edgeColour = (200,200,200)
        self.nodeRadius = 4
        self.vision = 'xy'
        self.zfactor = 0


    def rotateALLX (self, radians):
        for wireframe in self.wireframes.values():
            wireframe.rotateX(radians)
            
    def rotateALLY (self, radians):
        for wireframe in self.wireframes.values():
            wireframe.rotateY(radians)

    def rotateALLZ (self, radians):
        for wireframe in self.wireframes.values():
            wireframe.rotateZ(radians)


            
            
    def set_vision(self, vision):
        self.vision = vision

        print(vision)

        if(self.zfactor!=0):
            if(self.vision=='xy'):
                if(self.zfactor>0):
                    scale=1.05
                else:
                    scale=0.95
            else:
                if(self.zfactor>0):
                    scale=0.95
                else:
                    scale=1.05

            for i in range(0,abs(self.zfactor)):
                self.scaleAll(scale)
                    

    def addWireframe(self, name, wireframe):
        """ Add a named wireframe object. """

        self.wireframes[name] = wireframe

    def run(self):
        """ Create a pygame screen until it is closed. """

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in key_to_function:
                        key_to_function[event.key](self)
                    
            self.display(self.vision)  
            pygame.display.flip()

        pygame.quit()
        
    def display(self, vision):
        """ Draw the wireframes on the screen. """

        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():              
            if self.displayEdges:
                  for edge in wireframe.edges:
                      if(self.vision=='xy'):
                          xi=edge.start.x
                          yi=edge.start.y
                          xf=edge.stop.x
                          yf=edge.stop.y
                      elif(self.vision=='xz'):
                          xi=edge.start.x
                          yi=edge.start.z
                          xf=edge.stop.x
                          yf=edge.stop.z

                      pygame.draw.aaline(self.screen, self.edgeColour, (xi, yi), (xf, yf), 1)

            if self.displayNodes:
                for node in wireframe.nodes:
                    if(self.vision=='xy'):
                        nx=node.x
                        ny=node.y
                    elif(self.vision=='xz'):
                        nx=node.x
                        ny=node.z
                        
                    pygame.draw.circle(self.screen, self.nodeColour, (int(nx), int(ny)), self.nodeRadius, 0)

    def translateAll(self, axis, d):
        """ Translate all wireframes along a given axis by d units. """

        if(self.vision=='xz' and axis =='y'):
            if(d>0):
                self.scaleAll(0.95)
                self.zfactor+=1
            else:
                self.scaleAll(1.05)
                self.zfactor-=1
        elif(self.vision=='xy' and axis =='y'):
            if(d>0):
                self.zfactor+=1
            else:
                self.zfactor-=1

        for wireframe in self.wireframes.values():
            wireframe.translate(axis, d)

    def scaleAll(self, scale):
        """ Scale all wireframes by a given scale, centred on the centre of the screen. """

        #centre_x = self.width/2
        #centre_y = self.height/2

        for wireframe in self.wireframes.values():
            wireframe.scale(scale)

if __name__ == '__main__':
    pv = ProjectionViewer(400, 300)

    cube = wireframe.Wireframe()
    cube.addNodes([(x,y,z) for x in (50,250) for y in (50,250) for z in (50,250)])
    cube.addEdges([(n,n+4) for n in range(0,4)]+[(n,n+1) for n in range(0,8,2)]+[(n,n+2) for n in (0,1,4,5)])
    
    pv.addWireframe('cube', cube)
    pv.run()
