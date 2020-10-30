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

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("pics", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("pics", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("pics", "pixel_ship_blue_small.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("pics", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("pics", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("pics", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("pics", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("pics", "pixel_laser_yellow.png"))


def redraw_window(): #function inside a function so only avaliable in this fucntion but won't need to pass varaibles through..
        WIN.blit(BACKGROUND, (0,0))
        lives_label = main_font.render(f"lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"level: {level}", 1, (255,255,255))
        
        WIN.blit(lives_label, (15,15))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 15,15))


def main_menu():
    redraw_window()


main_menu
