import pygame


class InputBox:
    def __init__(self, x, y, width, height, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('gray15')
        self.color = self.color_passive
        self.active = False
        self.text = ""
        self.font = font

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    pass
                elif event.key == pygame.K_ESCAPE:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def update(self):
        width = max(self.font.size(self.text)[0] + 10, 100)
        self.rect.w = width
        self.color = self.color_active if self.active else self.color_passive

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
