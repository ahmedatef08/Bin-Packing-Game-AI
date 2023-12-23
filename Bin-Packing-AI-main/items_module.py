import pygame
import random

pygame.font.init()


class Item:
    item_font_size = 20
    item_font = pygame.font.Font(None, item_font_size)

    @staticmethod
    def generate_constant_colors(num_colors):
        return [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(num_colors)
        ]

    def __init__(self, index, item_x_pos, item_y_pos, num_items, size):
        self.index = index
        self.text = f"Item {index + 1}"
        self.label = Item.item_font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.label.get_rect(center=(item_x_pos / 2, item_y_pos + 10))
        self.text_size = f"{size}"
        self.label_size = Item.item_font.render(self.text_size, True, (0, 0, 0))
        self.text_rect_size = self.label_size.get_rect(center=((item_x_pos + size / 2) - self.label_size.get_width() / 2, item_y_pos + 5))
        self.rect = pygame.Rect(item_x_pos, item_y_pos, size, 20)
        self.color = Item.CONSTANT_COLORS[index % num_items]
        self.x = item_x_pos
        self.y = item_y_pos
        self.height = 20
        self.width = size
        self.size = size
        self.item_color = self.color
        self.reached_destination = False
        self.reset_requested = False


Item.CONSTANT_COLORS = Item.generate_constant_colors(9999)
