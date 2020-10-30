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

font = pygame.font.SysFont('comicsans', 60)

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece_img = None
        self.kind = None
        
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

    #basic movement options
    def options(self, difx, dify, direction):
        if self.kind == "pawn":
            if difx == 0 and dify == 90*direction:
                return True
        elif self.kind == "castle":
            if difx == 0 or dify == 0:
                return True
        elif self.kind == "knight":
            print (difx, dify)
            if (abs(difx) == 90 and abs(dify) == 180) or (abs(difx) == 180 and abs(dify) == 90):
                return True
        elif self.kind == "bishop":
            if dify != 0 and (difx/dify == 1 or difx/dify == -1):
                return True
        elif self.kind == "queen":
            if difx == 0 or dify == 0:
                return True
            elif dify != 0 and (difx/dify == 1 or difx/dify == -1):
                return True
        elif self.kind == "king":
            if abs(difx) <= 90 and  abs(difx) <= 90:
                return True
        else:
            return False
            
    #only for pawn attack check
    def attack_destroy(self, difx, dify, direction):
        if self.kind == "pawn":
            if (difx == 90 or difx == -90) and dify == 90*direction:
                self.move(difx, dify)
                return True
            else:
                return False
                
        else:
            print("Heello")
            return True #for other pieces to get to this point must be move ture
        
    

class Pawn(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_PAWN),
        "dark": (DARK_PAWN)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]
        self.kind = "pawn"

class Castle(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_CASTLE),
        "dark": (DARK_CASTLE)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]
        self.kind = "castle"

class Knight(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_KNIGHT),
        
        "dark": (DARK_KNIGHT)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]
        self.kind = "knight"

class Bishop(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_BISHOP),
        "dark": (DARK_BISHOP)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]
        self.kind = "bishop"

class Queen(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_QUEEN),
        "dark": (DARK_QUEEN)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]
        self.kind = "queen"
        
        
class King(Piece):
    COLOUR_MAP = {
        "light": (LIGHT_KING),
        "dark": (DARK_KING)
        }
    def __init__(self, x, y, colour):
        super().__init__(x,y)
        self.piece_img = self.COLOUR_MAP[colour]
        self.kind = "king"
     
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
        first_move = "home"
    else:
        away_colour = "light"
        first_move = "away"
    
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
    
    return [home_pieces, away_pieces], first_move
     
def main():
    def print_background(): #print over old piece positions
        #board
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

        #lettering and numbering
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
    
    def print_pieces(home_pieces,away_pieces):
        #pieces    
        for piece in home_pieces:
            piece.draw(WIN)
        for piece in away_pieces:
            piece.draw(WIN)

    def board_options

    
            
        
    FPS = 60
    setupdata, first_move = set_up()
    home_pieces = setupdata[0]
    away_pieces = setupdata[1]
    
    run = True
    toggle = False 

    print_background()
    print_pieces(home_pieces,away_pieces)
    pygame.display.update()

    turn = first_move    
    while run:
        pygame.time.Clock().tick(FPS)
        b=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                #quit()
                
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print_background() #if board click board resets
                print_pieces(home_pieces,away_pieces)
                if pos[0] < 720 and pos [1] < 720:
                    x1 = int(pos[0]/90)*90
                    y1 = int(pos[1]/90)*90
#####################For initial select
                    if toggle == False: #nothing selected - highlighting piece
                        #home p
                        if turn == "home":
                            for piece in home_pieces:
                                if piece.posCheck(x1,y1) == True:
                                    cur_sel_x = x1
                                    cur_sel_y = y1
                                    toggle = True
                                    WIN.blit(HIGHLIGHTED_SQUARE,(x1,y1)) # highlight sqaure
                                    print_pieces(home_pieces,away_pieces)
                                    b=1
                                    break
                            if b==1: #because need to break out of TWO for loops
                                pygame.display.update()
                                break
                        #away p
                        if turn == "away":
                            for piece in away_pieces:
                                if piece.posCheck(x1,y1) == True:
                                    cur_sel_x = x1
                                    cur_sel_y = y1
                                    toggle = True
                                    WIN.blit(HIGHLIGHTED_SQUARE,(x1,y1))
                                    print_pieces(home_pieces,away_pieces)
                                    b=1
                                    break
                            if b==1:
                                pygame.display.update() 
                                break
                        
#####################For move and other
                    if toggle == True:#selected/unselected - maybe change to select another piece (A3-3)
                        toggle = False #unselects if clicked 
                        if x1 == cur_sel_x and y1 == cur_sel_y:
                            pygame.display.update() #already blanked out at start
                            break    
                        else: #seleceted - move
                            difx = x1 - cur_sel_x
                            dify = y1 - cur_sel_y
                            #home
                            if turn == "home":
                                for piece in home_pieces:
                                    homepiece = piece #using the same element in a sub for loop gets messy so..
                                    if piece.posCheck(cur_sel_x,cur_sel_y) == True: #gets selected peice to be manipulated
                                        if board_options(difx,dify,home_pieces,away_pieces) == True:
                                            BoOp = True
                                        else:
                                            BoOp = False
                                        if piece.options(difx,dify,-1) == True and BoOp == True:
                                            piece.move(difx, dify)
                                            print_background()
                                            print_pieces(home_pieces,away_pieces)
                                            b=1
                                        if piece.attack_destroy(difx,dify,-1) == True and BoOp == True:
                                            for piece in away_pieces:
                                                if piece.posCheck(x1,y1) == True:
                                                    away_pieces.remove(piece)#remove piece from away_pieces
                                                    print_background()
                                                    print_pieces(home_pieces,away_pieces)
                                                    b=1
                                                    break
                                            break
                                if b==1:
                                    turn = "away"
                                    pygame.display.update() 
                                    break
                            #away
                            if turn == "away":
                                for piece in away_pieces:
                                    awaypiece = piece
                                    if piece.posCheck(cur_sel_x,cur_sel_y) == True:
                                        if piece.options(difx,dify,1) == True:
                                            piece.move(difx, dify)
                                            print_background()
                                            print_pieces(home_pieces,away_pieces)
                                            b=1
                                        if piece.attack_destroy(difx,dify,1) == True:
                                            for piece in home_pieces:
                                                if piece.posCheck(x1,y1) == True:
                                                    home_pieces.remove(piece)#remove piece from away_pieces
                                                    print_background()
                                                    print_pieces(home_pieces,away_pieces)
                                                    b=1
                                                    break
                                            break
                                if b==1:
                                    turn = "home"
                                    pygame.display.update() 
                                    break
                        pygame.display.update() #basically for random unselection. 
                            
                        
                                
                                
                      
                                                                                        
        
                    

main()

    




    

