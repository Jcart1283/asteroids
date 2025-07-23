import sys
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

AsteroidField.containers = (updatable)
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)

asteroid_field = AsteroidField()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #for obj in updatable:
        #    obj.update(dt)
        updatable.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.collides(player):
                print("game over")
                sys.exit()
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
