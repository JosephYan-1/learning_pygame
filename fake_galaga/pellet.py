import pygame
class Pellet:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.radius = 3
        self.speed = 5

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius)

    def hit(self, enemy):
        pellet_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        return pellet_rect.colliderect(enemy.get_rect())