import pygame
from pygame.locals import *
import os
from pygame import mixer

# Initializarea jocului
pygame.init()

# Centrarea jocului
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Rezolutia jocului
screen_width=720
screen_height=720
screen=pygame.display.set_mode((screen_width, screen_height))

# Redarea textului
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Culori
white=(255, 255, 255)
black=(19, 201, 194)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(13, 233, 226)
blue=(108, 15, 102)
yellow=(255, 255, 0)
purple=(186,25,211)


# Fontul
font = "Graphics/Mabook.otf"


# Cadre pe secunda
clock = pygame.time.Clock()
FPS=60

# Tastele si contitia existentei
def main_menu():

    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        import snake_game
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Interfata meniului
        screen.fill(purple)
        title = text_format("SNAKE GAME", font, 90, green)
        if selected == "start":
            text_start = text_format("START", font, 75, white)
          
        else:
            text_start = text_format("START", font, 75, black)
        if selected == "quit":
          
            text_quit = text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 390))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Snake Game")


#Initializarea jocului
main_menu()
pygame.quit()
quit()
