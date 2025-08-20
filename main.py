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
    from player import *
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatebles = pygame.sprite.Group()
    updatebles.add(player)
    drawables = pygame.sprite.Group()
    drawables.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill("black")
        updatebles.update(dt)
        drawables.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000
