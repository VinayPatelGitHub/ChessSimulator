import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 720, 720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Attempt - Star Ting")

#STAR = pygame.image.load(os.path.join("pics", "star.png"))
#BACKGROUND = pygame.image.load(os.path.join("pics", "background.png")) #can scale using pygame.transform.scale(/#/,/scaleto/) 


class Piece:
    def __init__(self, x, y, health=1, colour):
        self.x = x
        self.y = y
        self.health = health
        self.colour

    def draw(self, WIN):
                WIN.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

class Player(Piece):
    def __init__(self, x, y, health=1):
        super().__init__(x, y, health) #super().
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img) #collisions
        self.max_health = health

class Enemy(Piece):
    COLOUR_MAP =    {
                    "red": (RED_SPACE_SHIP, RED_LASER),
                    "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                    "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                    }
    def __init__(self, x, y, colour, health=1):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOUR_MAP[colour]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel
                
def main():
    run = True
    FPS = 60
    main_font = pygame.font.SysFont("comicsans", 50)

    player_pieces = []
    enemies_pieces = []
     
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window(): #function inside a function so only avaliable in this fucntion but won't need to pass varaibles through..
        WIN.blit(BACKGROUND, (0,0))
        lives_label = main_font.render(f"lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"level: {level}", 1, (255,255,255))
        
        WIN.blit(lives_label, (15,15))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 15,15))

        for enemy in enemies:
            enemy.draw(WIN)

        piece1.draw(WIN)
                
        if lost:
            lost_label =  main_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (500 , 300))

        pygame.display.update() 

    while run:
        clock.tick(FPS)
        
        redraw_window()
        
                 
        if lost:
            if lost_count > FPS *3:
                run = False
                print ("end")
            else:
                continue #restart while
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red","blue","green"]))
                enemies.append(enemy)
                print(i)
               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                            
          
#main()
