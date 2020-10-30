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
HIGHLIGHTED_SQUARE = pygame.image.load(os.path.join("PicsA2", "highlighted square.png"))

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

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
                  
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
                
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

class Index():
    def__init__(self,x,y,button,piece)

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece_img = None
    def draw(self, window):
        window.blit(self.piece_img, (self.x, self.y))

class Pawn(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_PAWN),
        "dark": (DARK_PAWN)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]

class Castle(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_CASTLE),
        "dark": (DARK_CASTLE)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]

class Knight(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_KNIGHT),
        "dark": (DARK_KNIGHT)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]

class Bishop(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_BISHOP),
        "dark": (DARK_BISHOP)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]

class Queen(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_QUEEN),
        "dark": (DARK_QUEEN)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]
        
class King(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_KING),
        "dark": (DARK_KING)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]
  

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
    home_pieces = []
    away_pieces = []

    COLOUR_MAP = {
        "light": (LIGHT_PAWN, LIGHT_CASTLE, LIGHT_KNIGHT, LIGHT_BISHOP, LIGHT_QUEEN, LIGHT_KING),
        "dark": (DARK_PAWN, DARK_CASTLE, DARK_KNIGHT, DARK_BISHOP, DARK_QUEEN, DARK_KING)
        }

    #randomsing player colour
    home_colour = random.choice(["light", "dark"])
    if home_colour == "light":
        away_colour = "dark"
    else:
        away_colour = "light"
    
#pawns
    for i in range (0,8):
        piece = Pawn(i*90, 6*90, home_colour)
        home_pieces.append(piece)
    for i in range (0,8):
        piece = Pawn(i*90, 1*90, away_colour)
        away_pieces.append(piece)
#backrow
    #Castles
    piece = Castle(0*90, 7*90, home_colour)
    home_pieces.append(piece)
    piece = Castle(7*90, 7*90, home_colour)
    home_pieces.append(piece)
    piece = Castle(0*90, 0*90, away_colour)
    away_pieces.append(piece)
    piece = Castle(7*90, 0*90, away_colour)
    away_pieces.append(piece)
    #Knights
    piece = Knight(1*90, 7*90, home_colour)
    home_pieces.append(piece)
    piece = Knight(6*90, 7*90, home_colour)
    home_pieces.append(piece)
    piece = Knight(1*90, 0*90, away_colour)
    away_pieces.append(piece)
    piece = Knight(6*90, 0*90, away_colour)
    away_pieces.append(piece)
    #Bishops
    piece = Bishop(2*90, 7*90, home_colour)
    home_pieces.append(piece)
    piece = Bishop(5*90, 7*90, home_colour)
    home_pieces.append(piece)
    piece = Bishop(2*90, 0*90, away_colour)
    away_pieces.append(piece)
    piece = Bishop(5*90, 0*90, away_colour)
    away_pieces.append(piece)
    #Queens
    piece = Queen(3*90, 7*90, home_colour)
    home_pieces.append(piece)
    piece = Queen(3*90, 0*90, away_colour)
    away_pieces.append(piece)
    #Kings
    piece = King(4*90, 7*90, home_colour)
    home_pieces.append(piece)
    piece = King(4*90, 0*90, away_colour)
    away_pieces.append(piece)

        
    for piece in home_pieces:
         piece.draw(WIN)
    for piece in away_pieces:
         piece.draw(WIN)

    pygame.display.update()
    print(away_pieces)
    
def main():
  
    background()
    set_up()


main()

    




    

