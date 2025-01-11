# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *

def main():
    print("Starting game...")  # Add this
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen dimensions: {SCREEN_WIDTH} x {SCREEN_HEIGHT}")  # Add this
    dt = 0
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Player created")  # Add this




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for thing in updateable:
            thing.update(dt)
        #player_one.update(dt)
        for thing in drawable:
            thing.draw(screen)
        #player_one.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

