import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)

    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (updatable_group, drawable_group, asteroids_group)

    shots_group = pygame.sprite.Group()
    Shot.containers = (updatable_group, drawable_group, shots_group)

    AsteroidField.containers = (updatable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
       
        updatable_group.update(dt)

        for asteroid in asteroids_group:
            if player.collisions(asteroid):
                sys.exit("Game over!")

        for asteroid in asteroids_group:
            for shot in shots_group:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")
       
        for sprite in drawable_group:
            sprite.draw(screen)
        
        pygame.display.flip()
    


if __name__ == "__main__":
    main()