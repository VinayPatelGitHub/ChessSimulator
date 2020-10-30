import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 720, 720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess - A2")

LIGHT_SQUARE = pygame.image.load(os.path.join("PicsA2", "light square.png"))
DARK_SQUARE = pygame.image.load(os.path.join("PicsA2", "dark square.png"))

LIGHT_PAWN = pygame.image.load(os.path.join("PicsA2", "light pawn.png"))
LIGHT_CASTLE = pygame.image.load(os.path.join("PicsA2", "light castle.png"))
LIGHT_KNIGHT = pygame.image.load(os.path.join("PicsA2", "light knight.png"))
LIGHT_BISHOP = pygame.image.load(os.path.join("PicsA2", "light bishop.png"))
LIGHT_QUEEN = pygame.image.load(os.path.join("PicsA2", "light queen.png"))
LIGHT_KING = pygame.image.load(os.path.join("PicsA2", "light king.png"))

DARK_PAWN = pygame.image.load(os.path.join("PicsA2", "dark pawn.png"))
DARK_CASTLE = pygame.image.load(os.path.join("PicsA2", "dark castle.png"))
DARK_KNIGHT = pygame.image.load(os.path.join("PicsA2", "dark knight.png"))
DARK_BISHOP = pygame.image.load(os.path.join("PicsA2", "dark bishop.png"))
DARK_QUEEN = pygame.image.load(os.path.join("PicsA2", "dark queen.png"))
DARK_KING = pygame.image.load(os.path.join("PicsA2", "dark king.png"))

class Piece:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

  

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
    pygame.display.update()
    
def set_up():
    light_pieces = []
    dark_pieces = []

    for i in range (0,8):
        piece = Piece(i*90, 6*90, LIGHT_PAWN)
        light_pieces.append(piece)
    for piece in light_pieces:
         piece.draw(WIN)

    pygame.display.update()
    
def main():
  
    background()
    set_up()

main()

    




    

