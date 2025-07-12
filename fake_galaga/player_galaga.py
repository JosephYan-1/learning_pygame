import pygame
from pellet import Pellet 
class Player:
    def __init__(self):
        self.leftpoint_x, self.leftpoint_y = 180,890
        self.rightpoint_x, self.rightpoint_y = 220,890
        self.centerpoint_x, self.centerpoint_y = 200,850
        self.player_movement = 5

    def move(self, key):
        if key[pygame.K_d]:
            if self.rightpoint_x + self.player_movement  <= 400:
                self.rightpoint_x += self.player_movement
                self.centerpoint_x += self.player_movement
                self.leftpoint_x += self.player_movement

        if key[pygame.K_a]:
            if self.leftpoint_x - self.player_movement >= 0:
                self.rightpoint_x -= self.player_movement
                self.centerpoint_x -= self.player_movement
                self.leftpoint_x -= self.player_movement

    def shoot(self):
        return Pellet(self.centerpoint_x + 1, self.centerpoint_y + 1)





    def draw(self, screen):
        self.playership_points = [(self.leftpoint_x, self.leftpoint_y), (self.rightpoint_x, self.rightpoint_y), (self.centerpoint_x, self.centerpoint_y)]
        pygame.draw.polygon(screen, "white", self.playership_points)