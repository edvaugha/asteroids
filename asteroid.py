import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            pos_x = self.position.x
            pos_y = self.position.y
            new_vector_one = self.velocity.rotate(random_angle)
            new_vector_two = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_one = Asteroid(pos_x, pos_y, new_radius)
            new_asteroid_two = Asteroid(pos_x, pos_y, new_radius)
            new_asteroid_one.velocity = new_vector_one * 1.2
            new_asteroid_two.velocity = new_vector_two
