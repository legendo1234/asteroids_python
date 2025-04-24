import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable


    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects except player
        for obj in updatable:
            if obj != player:  # Skip player since we update it separately
                obj.update(dt)
        
        # Update player with shots group
        player.update(dt, shots)
        
        # Update shots
        shots.update(dt)
        
        # Collision detection
        for asteroid in asteroids:
            if player.Collision(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.Collision(asteroid):
                    shot.kill()  # Remove the bullet
                    asteroid.split()  # Split the asteroid
        
        # Clear the screen
        screen.fill("black")
        
        # Draw all objects
        for obj in drawable:
            obj.draw(screen)
            
        # Draw shots
        for shot in shots:
            shot.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
