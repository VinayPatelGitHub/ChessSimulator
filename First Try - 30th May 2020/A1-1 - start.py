import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Attempt - Star Ting")

STAR = pygame.image.load(os.path.join("pics", "star.png"))
BACKGROUND = pygame.image.load(os.path.join("pics", "background.png")) #can scale using pygame.transform.scale(/#/,/scaleto/) 

vinay = 0

class Pieces:
    def __init__(self, x, y, colourx, coloury, health=1): #__init__(self,)
        self.x = x
        self.y = y
        self.colourx = colourx
        self.coloury = coloury
        self.health = health
        #self.ship_img = None
        #self.laser_img = None
        #self.lasers = []
        #self.cool_down_counter = 0

    def draw(self, WIN):
        pygame.draw.rect(WIN, (255,self.colourx,self.coloury), (self.x, self.y, 50, 50)) #or..50), #) for border
        

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    player_vel = 5
    
    Piece1 = Pieces(300,300,0,0)

    clock = pygame.time.Clock()

    def redraw_window(): #function inside a function so only avaliable in this fucntion but won't need to pass varaibles through..
        WIN.blit(BACKGROUND, (0,0))
        lives_label = main_font.render(f"lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"level: {level}", 1, (255,255,255))
        
        WIN.blit(lives_label, (15,15))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 15,15))

        Piece1.draw(WIN)
        
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #if event.type == pygame.KEYDOWN

        vinay.x = Piece1.x
        Piece1.colourx = round((vinay.x/1280)*255)
        vinay.y = Piece1.y
        Piece1.coloury = round((vinay.y/1280)*255)
   
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: 
            Piece1.x -= player_vel #LEFT (#4arrows)
        if keys[pygame.K_d]: #RIGHT
            Piece1.x += player_vel #right is posotive
        if keys[pygame.K_s]: #DOWN
            Piece1.y += player_vel #down is postive
        if keys[pygame.K_w]: #UP
            Piece1.y -= player_vel
            
                
main()
