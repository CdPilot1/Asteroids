import pygame
import constants
def main():
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

if __name__ == "__main__":
    main()
    pygame.init()
    from constants import *
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill("black")
        pygame.display.flip()
