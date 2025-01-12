# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots_group)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    print("Player created")  # Add this




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for thing in updateable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player_one):
                #print("Game over!")
                exit("Game over!")

            for shot in shots_group:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

