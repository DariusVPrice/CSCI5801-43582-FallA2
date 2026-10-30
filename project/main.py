import sys, pygame, math, os, random;
from pygame.locals import *

def RoundToNearest(i, j):
    return i & ~(j-1)
def CreateArray(size, val):
    a = []
    for i in range(0,size):
        a.append(val)
    return a

class Vector(object):
    def __init__(self,x=0,y=0):
        self.x, self.y = x,y

class Window(object):
    def __init__(self,w=640,h=320):
        pygame.init()
        self.width = w
        self.height = h
        self.title = ""
        self.size = (w, h)
        self.window = pygame.display.set_mode(self.size)
        self.buffer = pygame.Surface((320,180))
    def GetBuffer(self):
        return self.buffer

    def Update(self):
        pygame.transform.scale(self.buffer,self.size,self.window)    
        pygame.display.flip()
        self.buffer.fill((0,0,0))


if __name__ == "__main__":
    window = Window()
    buffer = window.GetBuffer()

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 14)#font = pygame.font.Font(os.path.join(os.getcwd(),'FreeMonoBold.ttf'),12)
    random.seed(0)
    fx, fy = 8, 8
    #map.CreateMapFile()
    points = []
    points.append(1/14)
    points.append(87/13)

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == QUIT:
                isRunning = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                print("test1")
            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                print("test3")
            pressed = pygame.key.get_pressed()
            if pressed[K_s]:
                pygame.image.save(buffer,'pallette.bmp')
            elif pressed[K_r]:
                pass
            elif pressed[K_q]:
                isRunning = False

        buffer.blit(font.render("test",True,(255,255,255)),(fx,fy))
        window.Update()

    #quit
    pygame.display.quit()
    pygame.quit()
    sys.exit
