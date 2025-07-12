import pygame
import random
from pellet import Pellet

class Enemy:
    def __init__(self):
        # leftpoint = random.randint(0,370)
        self.width = 30
        self.leftpoint = random.randint(0,370)
        self.rightpoint = self.leftpoint + self.width
        self.centerpoint = (self.leftpoint + (self.width // 2))
        self.y_location = 30
        colors = ['red', 'blue', 'green']
        self.color = random.choice(colors)

        self.speed = random.randint(3,5)

    def move(self, speed):
        self.y_location += speed

    def draw(self, screen):
        enemy_points = [(self.leftpoint, self.y_location), (self.centerpoint, self.y_location +30), (self.rightpoint, self.y_location)]
        pygame.draw.polygon(screen, self.color, enemy_points)

    def get_rect(self):
        # Return a bounding box that fully encloses the triangle
        return pygame.Rect(self.leftpoint, self.y_location, self.width, 30)