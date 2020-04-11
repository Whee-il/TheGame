import random, pygame, time, sys
pygame.init()
#Global Variablefs

WIN_W = 1000
WIN_H = 750
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (119,157,255)
RED = (255,64,34)
PURPLE = (184,120,255)
YELLOW = (255,243,17)
ORANGE = (255,166,33)
GREEN = (65,255,85)
BROWN = (99,73,5)
LIGHT_GREY = (55,54,56)
def main():

    #Setting up pycharm screen
    screen = pygame.display.set_mode((WIN_W,WIN_H), pygame.SRCALPHA)

    #Local variable
    game = True

    #Game Loop
    clock = pygame.time.Clock()

    fps = 90
    while game:
        #Take In Input
        mousepos = pygame.mous.get_pos()


        #Process Input


        #Gameplay


        #Update
        screen.FILL(WHITE)

        clock.tick(fps)

        pygame.display.flip()
