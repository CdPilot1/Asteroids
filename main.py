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
    from asteroid import *
    from asteroidfield import *
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    updatebles = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = updatebles, drawables
    Asteroid.containers = updatebles, drawables, asteroids
    AsteroidField.containers = updatebles
    Shot.containers = updatebles, drawables, shots
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill("black")
        updatebles.update(dt)
        for sprite in drawables:
            sprite.draw(screen)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                pygame.quit()
                exit()
        pygame.display.flip()
        dt = Clock.tick(60) / 1000
