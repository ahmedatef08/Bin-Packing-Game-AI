import pygame
import math


class MenuBtn:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, initial_scale, target_scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * initial_scale), int(self.height * initial_scale)))
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.initial_scale = initial_scale
        self.target_scale = target_scale
        self.current_scale = initial_scale

    def ease_in_out(self, t):
        return 0.5 * (1 - math.cos(math.pi * t))

    def update(self, screen):
        if self.image is not None:
            pos = pygame.mouse.get_pos()
            hovered = self.rect.collidepoint(pos)

            if hovered:
                self.target_scale = self.target_scale
            else:
                self.target_scale = self.initial_scale

            easing_speed = 0.5
            self.current_scale += (self.target_scale - self.current_scale) * easing_speed

            scaled_image = pygame.transform.scale(self.image,
                                                  (int(self.width * self.current_scale),
                                                   int(self.height * self.current_scale)))
            screen.blit(scaled_image, (self.rect.x, self.rect.y))
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
