import pygame
import os
import time
import random
pygame.font.init()

def hello():
    for x in range(1, 5):
        print("We're on time %d" % (x))
#hello()

def star():
    WIDTH, HEIGHT = 720, 720
    WIN = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("First Attempt - Star Ting")
    #STAR = pygame.image.load(os.path.join("pics", "star.png"))
    BG = pygame.transform.scale(pygame.image.load(os.path.join("pics", "background.png")), (WIDTH, HEIGHT))
    WIN.blit(BG, (0,0))
    pygame.display.update()
#star()


def passing_data():
    a = [5, 6, 7]
    b = [6 , 8]
    return [a,b]
def main_calling_data():
    a = passing_data()
    b = a[0]
    c = a[1]
    print(b)
    print(c)
#main_calling_data()


def main_con(): #aim to restart (x+=1) while when t=3 or s=3
    run = True
    x=0
    b=0
    while run:
        pygame.time.Clock().tick(1)
        x += 1
        print('x=',x)
        if x == 2:
            print ('a')
            for t in range (1,10):
                if b == 1:
                    break
                if t == 3:
                    break
                print('t=',t)
                if t == 2:
                    for s in range(1,10):
                        print('s=',s)
                        if s == 3:
                            b=1
                            break
        if x == 5:
            run = False
        
main_con()
                
        
 
            
