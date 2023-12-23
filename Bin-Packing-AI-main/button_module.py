import pygame
import math


class Button:
    def __init__(self, x, y, image, callback, initial_scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * initial_scale), int(self.height * initial_scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.callback = callback
        self.target_scale = initial_scale
        self.current_scale = initial_scale

    def ease_in_out(self, t):
        return 0.5 * (1 - math.cos(math.pi * t))

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        hovered = self.rect.collidepoint(pos)

        if hovered:
            self.target_scale = 0.9
        else:
            self.target_scale = 0.8

        easing_speed = 0.5
        self.current_scale += (self.target_scale - self.current_scale) * easing_speed

        scaled_image = pygame.transform.scale(self.image,
                                              (int(self.width * self.current_scale),
                                               int(self.height * self.current_scale)))
        screen.blit(scaled_image, (self.rect.x, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()
