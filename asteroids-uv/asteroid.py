import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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
        angle = random.uniform(20, 50)
        rotated_v1 = self.velocity.rotate(angle) * 1.2
        rotated_v2 = self.velocity.rotate(-angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_aster1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_aster2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_aster1.velocity = rotated_v1
        new_aster2.velocity = rotated_v2
        