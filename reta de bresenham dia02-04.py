import pygame;
from pygame.locals import *

def reta_bresenham(p1,p2):
    x0=p1[0]
    y0=p1[1]

    x1=p2[0]
    y1=p2[1]

    lista=[]

    if(x0>x1):
        lista=reta_bresenham(p2,p1)
        return lista

    dy=y1-y0
    dx=x1-x0
    d=dy/dx

    inc=1
    
    if(dy<0):
        inc=-1
        dy=-dy

    x=x0
    y=y0

    #reta ang horizontal
    incdy=2*(dy-dx)
    incdx=2*dy
    #reta ang vertical
    incdy1=2*(dx-dy)
    incdx1=2*dx
    
    if(dx>dy):
        
        for i in range(1,dx+1):
            lista.append((x,y))

            if(d>0):
                y=y+inc
                d=d+incdy
            else:
                d=d+incdx

            x=x+1
    else:
        for i in range(1,dy+1):
            lista.append((x,y))

            if(d>0):
                x=x+inc
                d=d+incdy1
            else:
                d=d_incdx1
                
            y=y+1
            
    return lista

#entrada de dados
#p1
x0=int(input("Entre com x0 : "))
y0=int(input("Entre com y0 : "))
#p2
x1=int(input("Entre com x1 : "))
y1=int(input("Entre com y1 : "))
#3
x2=int(input("Entre com x2 : "))
y2=int(input("Entre com y2 : "))
#p4
x3=int(input("Entre com x3 : "))
y3=int(input("Entre com y3 : "))

lista_final=[[]]

lista_final.append(reta_bresenham((x0,y0),(x3,y3)))
lista_final.append(reta_bresenham((x1,y1),(x2,y2)))


pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

window = pygame.display.set_mode((640,480))
pygame.display.set_caption("Metodo Bresenham")

window.fill(WHITE)

for i in range(0,len(lista_final)):
    for j in range(0,len(lista_final[1])):
        window.set_at(lista_final[i][j],BLACK)
    
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        



