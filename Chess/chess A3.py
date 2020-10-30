import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 780, 780
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess - A2")

LIGHT_SQUARE = pygame.image.load(os.path.join("PicsA2", "light square.png"))
DARK_SQUARE = pygame.image.load(os.path.join("PicsA2", "dark square.png"))
HIGHLIGHTED_SQUARE = pygame.image.load(os.path.join("PicsA2", "highlighted square.png"))

DARK_PAWN = pygame.image.load(os.path.join("PicsA2", "dark pawn.png"))

font = pygame.font.SysFont('comicsans', 60)

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    ##def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
                  
        ##pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        ##if self.text != '':
            ##font = pygame.font.SysFont('comicsans', 60)
            ##text = font.render(self.text, 1, (0,0,0))
            ##win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

class Position():
    def __init__(self,x,y,piece):
        self.x=x
        self.y=y
        self.piece=None

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece_img = DARK_PAWN
        
    def draw(self, window):
        window.blit(self.piece_img, (self.x, self.y))
        
    def posCheck(self, x1, y1):
        if self.x == x1 and self.y == y1:
            return True
        else:
            return False
        
    def move(self, difx, dify):
        self.x += difx
        self.y += dify
        
        
  
 
def main():
    piece = Piece(4*90, 3*90)
    run = True
    toggle = 0
    button1 = Button((0,255,0), 500,500,90,90, 'fm')
    def background():
        scale = 90
        for x in range(0,4):
            for y in range (0,4):
                WIN.blit(LIGHT_SQUARE,(2*x*scale,2*y*scale))
        for x in range(1,5):
            for y in range (1,5):
                WIN.blit(LIGHT_SQUARE,(((2*x)-1)*scale,((2*y)-1)*scale))
        for x in range(1,5):
            for y in range (0,4):
                WIN.blit(DARK_SQUARE,((2*x-1)*scale,2*y*scale))
        for x in range(0,4):
            for y in range (1,5):
                WIN.blit(DARK_SQUARE,(2*x*scale,(2*y-1)*scale))
        

        NUMBER_MAP =     {
           1 : ("A"),
           2 : ("B"),
           3 : ("C"),
           4 : ("D"),
           5 : ("E"),
           6 : ("F"),
           7 : ("G"),
           8 : ("H")
                        }
        
        for n in range(1, 9):
            WIN.blit(font.render(NUMBER_MAP[n], 1, (255,255,255)), ((n-1)*90 + 30, 730))

        for n in range (1,9):
            WIN.blit(font.render(f"{n}", 1, (255,255,255)), (740, (n-1)*90 + 30))
        
    
    while run:
        pygame.time.Clock().tick(60)
        
        if toggle == 0:
            background()

        piece.draw(WIN)
        pygame.display.update()       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                #quit()
                
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] < 720 and pos [1] < 720:
                    x1 = int(pos[0]/90)*90
                    y1 = int(pos[1]/90)*90
                    if toggle == 0:
                        if piece.posCheck(x1,y1) == True:
                            cur_sel_x = x1
                            cur_sel_y = y1
                            toggle = 1
                            WIN.blit(HIGHLIGHTED_SQUARE,(x1,y1))
                        continue
                    if toggle == 1:
                        if piece.posCheck(x1,y1) == True:
                            toggle = 0
                            continue
                        else:
                            difx = x1 - cur_sel_x
                            dify = y1 - cur_sel_y
                            piece.move(difx, dify)
                            toggle = 0
                            continue
                      
                                                                                        
        
                    

main()

    




    

