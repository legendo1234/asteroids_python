# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the loop and close the game

        screen.fill("black")  # Fill the screen with a solid color

        # Call update for all updatable objects
        updatable.update(dt)

        # Loop over all drawable objects and call their draw method
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()  # Refresh the display

        # Frame rate control
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000

    




if __name__ == "__main__":
    main()