import pygame
import os
import time
import random
pygame.font.init()

SCALE = 90
WIDTH, HEIGHT = SCALE*8 +60, SCALE*8 +60
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
        
    def posCheck(self, x, y):
        if self.x == x and self.y == y:
            return True
        else:
            return False
            
    def move(self, difx, dify):
        self.x += difx
        self.y += dify

    def options(self, difx, dify, direction):
        if self.kind == "castle":
            if difx == 0 or dify == 0:
                return True
        elif self.kind == "knight":
            if (abs(difx) == SCALE and abs(dify) == SCALE*2) or (abs(difx) == SCALE*2 and abs(dify) == SCALE):
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
            if abs(difx) <= SCALE and  abs(dify) <= SCALE:
                return True
        else:
            return False
            
    def pawn_attack(self, difx, dify, direction):
        if (difx == SCALE or difx == -SCALE) and dify == SCALE*direction:
            self.move(difx, dify)
            return True
        else:
            return False        

    def pawn_move(self, difx, dify, direction):
        if difx == 0 and dify == SCALE*direction:
            self.move(difx, dify)
            return True

    def friendly_collision(self, x1, y1, x2, x3):
        if x2 == x1 and y2 == y1:
            return True
        else:
            return False           
  

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
        piece = Pawn(i*SCALE, 6*SCALE, home_colour)
        home_pieces.append(piece)
    for i in range (0,8):
        piece = Pawn(i*SCALE, 1*SCALE, away_colour)
        away_pieces.append(piece)
#backrow
    #Castles
    piece = Castle(0*SCALE, 7*SCALE, home_colour)
    home_pieces.append(piece)
    piece = Castle(7*SCALE, 7*SCALE, home_colour)
    home_pieces.append(piece)
    piece = Castle(0*SCALE, 0*SCALE, away_colour)
    away_pieces.append(piece)
    piece = Castle(7*SCALE, 0*SCALE, away_colour)
    away_pieces.append(piece)
    #Knights
    piece = Knight(1*SCALE, 7*SCALE, home_colour)
    home_pieces.append(piece)
    piece = Knight(6*SCALE, 7*SCALE, home_colour)
    home_pieces.append(piece)
    piece = Knight(1*SCALE, 0*SCALE, away_colour)
    away_pieces.append(piece)
    piece = Knight(6*SCALE, 0*SCALE, away_colour)
    away_pieces.append(piece)
    #Bishops
    piece = Bishop(2*SCALE, 7*SCALE, home_colour)
    home_pieces.append(piece)
    piece = Bishop(5*SCALE, 7*SCALE, home_colour)
    home_pieces.append(piece)
    piece = Bishop(2*SCALE, 0*SCALE, away_colour)
    away_pieces.append(piece)
    piece = Bishop(5*SCALE, 0*SCALE, away_colour)
    away_pieces.append(piece)
    #Queens
    piece = Queen(3*SCALE, 7*SCALE, home_colour)
    home_pieces.append(piece)
    piece = Queen(3*SCALE, 0*SCALE, away_colour)
    away_pieces.append(piece)
    #Kings
    piece = King(4*SCALE, 7*SCALE, home_colour)
    home_pieces.append(piece)
    piece = King(4*SCALE, 0*SCALE, away_colour)
    away_pieces.append(piece)
    
    return [home_pieces, away_pieces], first_move
     
def main():
    def print_background(): #print over old piece positions
        #board
        for x in range(0,4):
            for y in range (0,4):
                WIN.blit(LIGHT_SQUARE,(2*x*SCALE,2*y*SCALE))
        for x in range(1,5):
            for y in range (1,5):
                WIN.blit(LIGHT_SQUARE,(((2*x)-1)*SCALE,((2*y)-1)*SCALE))
        for x in range(1,5):
            for y in range (0,4):
                WIN.blit(DARK_SQUARE,((2*x-1)*SCALE,2*y*SCALE))
        for x in range(0,4):
            for y in range (1,5):
                WIN.blit(DARK_SQUARE,(2*x*SCALE,(2*y-1)*SCALE))

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
            WIN.blit(font.render(NUMBER_MAP[n], 1, (255,255,255)), ((n-1)*SCALE + 30, HEIGHT-50))
        for n in range (1,9):
            WIN.blit(font.render(f"{n}", 1, (255,255,255)), (WIDTH-40, (n-1)*SCALE + 30))
    
    def print_pieces(home_pieces,away_pieces):
        #pieces    
        for piece in home_pieces:
            piece.draw(WIN)
        for piece in away_pieces:
            piece.draw(WIN)

              
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
    
    #MAIN LOOP STARTS
    while run: ####
        pygame.time.Clock().tick(FPS)
        b=0
        a=0
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
                    x1 = int(pos[0]/SCALE)*SCALE
                    y1 = int(pos[1]/SCALE)*SCALE
#####################For initial select
                    if toggle == False: #nothing selected - highlighting piece
                        #home p
                        if turn == "home":
                            #is CHECK?
                            
                            for piece in home_pieces:
                                #Find king
                                if isinstance(piece, King): 
                                    #check diag
                                    DIAG = {
                                        1 : (1,1),
                                        2 : (1,-1),
                                        3 : (-1,-1),
                                        4 : (-1,1)
                                        }
                                    for direction in range (1,5):
                                        for diag in range (1,8):
                                            xdir, ydir = DIAG[direction]
                                            xhelp= piece.x + SCALE*diag*xdir
                                            yhelp= piece.y + SCALE*diag*ydir
                                            if xhelp < 0 or xhelp >= 720 or yhelp < 0 or yhelp >= 720:
                                                break
                                            WIN.blit(HIGHLIGHTED_SQUARE, (xhelp,yhelp))
                                    #check lines
                                    LINE = {
                                        1 : (0,1), #ffs forgotten what was standard in radians
                                        2 : (-1,0),
                                        3 : (0,-1),
                                        4 : (1,0)
                                        }
                                            
                                    for direction in range (1,5):
                                        for line in range (1,8):
                                            xdir, ydir = LINE[direction]
                                            xhelp= piece.x + SCALE*line*xdir
                                            yhelp= piece.y + SCALE*line*ydir
                                            if xhelp < 0 or xhelp >= 720 or yhelp < 0 or yhelp >= 720:
                                                break
                                            WIN.blit(HIGHLIGHTED_SQUARE, (xhelp,yhelp))

                                    #check knight        
                                    KNT = {
                                        1 : (1,2),
                                        2 : (2,1),
                                        3 : (2,-1),
                                        4 : (1,-2),
                                        5 : (-1,-2),
                                        6 : (-2,-1),
                                        7 : (-2,1),
                                        8 : (-1,2)
                                        }
                                            
                                    for direction in range (1,9):
                                        xdir, ydir = KNT[direction]
                                        xhelp= piece.x + SCALE*xdir
                                        yhelp= piece.y + SCALE*ydir
                                        if xhelp < 0 or xhelp >= 720 or yhelp < 0 or yhelp >= 720:
                                            continue
                                        WIN.blit(HIGHLIGHTED_SQUARE, (xhelp,yhelp))
                                            
                                            
                                            
                                        
                            
                            


                            
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
                                kill_confirmed = False
                                for piece in home_pieces:
                                    if piece.posCheck(cur_sel_x,cur_sel_y) == True: #gets selected peice to be manipulated
                                        #avoid moving through (need to copy for away)
                                        if not isinstance(piece, Knight):
                                            if difx > 0:
                                                dx = 1
                                            else:
                                                dx = -1
                                            if dify > 0:
                                                dy = -1
                                            else:
                                                dy = 1
                                            if abs(difx) >= abs(dify):
                                                spaces = int(abs(difx)/SCALE)-1
                                            else:
                                                spaces = int(abs(dify)/SCALE)-1
                                            for bit in range (1,spaces+1):
                                                if abs(difx) > abs(dify):
                                                    x2=cur_sel_x + SCALE*bit*dx
                                                    y2=cur_sel_y
                                                elif abs(difx) < abs(dify):
                                                    x2=cur_sel_x
                                                    y2=cur_sel_y - SCALE*bit*dy
                                                else:
                                                    x2=cur_sel_x + SCALE*bit*dx
                                                    y2=cur_sel_y - SCALE*bit*dy
                                                for piecehome in home_pieces:
                                                    if piecehome.posCheck(x2,y2) == True:
                                                        a = 1
                                                        break
                                                for pieceaway in away_pieces:
                                                    if pieceaway.posCheck(x2,y2) == True:
                                                        a = 1
                                                        break
                                            if a == 1:
                                                break
                                         
                                        #avoid self-collision
                                        for piecehome in home_pieces: # for all home piece to collide with piece(home)
                                            if piecehome.posCheck(x1,y1) == True: # checks if home piece collides with home piece
                                                is_col = True #not good 1
                                                break
                                            else:
                                                is_col = False
                                        #Pawns        
                                        if isinstance(piece, Pawn): #use this to sort pawns and then let rest be handled differently
                                            for pieceaway in away_pieces:#check if anything infront
                                                if pieceaway.posCheck(x1,y1) == True:
                                                    is_som = True #not good 2
                                                    break
                                                else:
                                                    is_som = False
                                            if is_som == False:
                                                if piece.pawn_move(difx, dify, -1) == True:
                                                    b=1
                                                    break
                                            for pieceaway in away_pieces:
                                                if pieceaway.posCheck(x1,y1) == True: #if enemy piece there
                                                    if piece.pawn_attack(difx, dify, -1) == True: #if allowed
                                                        kill_confirmed = True
                                                        b=1
                                                        break
                                        #Non-Pawns       
                                        if piece.options(difx,dify,-1) == True and is_col == False:
                                            piece.move(difx, dify)
                                            kill_confirmed = True
                                            b=1
                                            break
                                            
                                #For Both    
                                if kill_confirmed == True:
                                    for pieceaway in away_pieces: # for ever away piece
                                        if pieceaway.posCheck(x1,y1) == True: # check if at moved to location
                                            away_pieces.remove(pieceaway)#if so remove piece from away_pieces
                                            b=1
                                            break

                                if b==1:
                                    turn = "away"
                                    print_background()
                                    print_pieces(home_pieces,away_pieces)
                                    pygame.display.update() 
                                    break
                            #away
                            if turn == "away":
                                kill_confirmed = False
                                for piece in away_pieces:
                                    if piece.posCheck(cur_sel_x,cur_sel_y) == True: #gets selected peice to be manipulated
                                         #avoid moving through (need to copy for away)
                                        if not isinstance(piece, Knight):
                                            if difx > 0:
                                                dx = 1
                                            else:
                                                dx = -1
                                            if dify > 0:
                                                dy = -1
                                            else:
                                                dy = 1
                                            if abs(difx) >= abs(dify):
                                                spaces = int(abs(difx)/SCALE)-1
                                            else:
                                                spaces = int(abs(dify)/SCALE)-1
                                            for bit in range (1,spaces+1):
                                                if abs(difx) > abs(dify):
                                                    x2=cur_sel_x + SCALE*bit*dx
                                                    y2=cur_sel_y
                                                elif abs(difx) < abs(dify):
                                                    x2=cur_sel_x
                                                    y2=cur_sel_y - SCALE*bit*dy
                                                else:
                                                    x2=cur_sel_x + SCALE*bit*dx
                                                    y2=cur_sel_y - SCALE*bit*dy
                                                for piecehome in home_pieces:
                                                    if piecehome.posCheck(x2,y2) == True:
                                                        a = 1
                                                        break
                                                for pieceaway in away_pieces:
                                                    if pieceaway.posCheck(x2,y2) == True:
                                                        a = 1
                                                        break
                                            if a == 1:
                                                break

                                        #avoid self-collision
                                        for pieceaway in away_pieces: # for all home piece to collide with piece(home)
                                            if pieceaway.posCheck(x1,y1) == True: # checks if home piece collides with home piece
                                                is_col = True
                                                break
                                            else:
                                                is_col = False
                                        #Pawns        
                                        if isinstance(piece, Pawn): #use this to sort pawns and then let rest be handled differently
                                            for piecehome in home_pieces:#check if anything infront
                                                if piecehome.posCheck(x1,y1) == True:
                                                    is_som = True #not good 2
                                                    break
                                                else:
                                                    is_som = False
                                            if is_som == False:
                                                if piece.pawn_move(difx, dify, 1) == True:
                                                    b=1
                                                    break
                                            for piecehome in home_pieces:
                                                if piecehome.posCheck(x1,y1) == True: #if enemy piece there
                                                    if piece.pawn_attack(difx, dify, 1) == True: #if allowed
                                                        kill_confirmed = True
                                                        b=1
                                                        break
                                        #Non-Pawns       
                                        if piece.options(difx,dify,1) == True and is_col == False:
                                            piece.move(difx, dify)
                                            kill_confirmed = True
                                            b=1
                                            break
                                            
                                #For Both    
                                if kill_confirmed == True:
                                    for piecehome in home_pieces: # for ever away piece
                                        if piecehome.posCheck(x1,y1) == True: # check if at moved to location
                                            home_pieces.remove(piecehome)#if so remove piece from away_pieces
                                            b=1
                                            break

                                if b==1: #could use one for both home and away
                                    turn = "home"
                                    print_background()
                                    print_pieces(home_pieces,away_pieces)
                                    pygame.display.update() 
                                    break
                        pygame.display.update() #basically for random unselection. 
                            
                        
                                
                                
                      
                                                                                        
        
                    

main()

    




    

