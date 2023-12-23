import pygame


class Bin:
    def __init__(self, x, y, width, height, color, index):
        self.rect = pygame.Rect(x, y, width, height)
        self.height = height
        self.color = color
        self.index = index
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
