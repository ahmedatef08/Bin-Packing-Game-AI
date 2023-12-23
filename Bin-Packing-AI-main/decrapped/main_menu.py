import pygame
import sys
from menu_btn_moudule import MenuBtn

pygame.init()

SCREEN_WIDTH = 1530
SCREEN_HEIGHT = 785
MID_SCREEN_WIDTH = SCREEN_WIDTH / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bin Packing AI')
clock = pygame.time.Clock()

background_img = pygame.image.load('./assets/background.jpg')
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
solve_genetic_img = pygame.image.load('./assets/solve_genetic_btn.png').convert_alpha()
solve_backtrack_img = pygame.image.load('./assets/solve_backtrack_btn.png').convert_alpha()
exit_img = pygame.image.load('./assets/exit_btn.png').convert_alpha()
menu_btn_img = pygame.image.load('./assets/menu_btns.png').convert_alpha()


def test():
    print("hamada")


def genetic_solve():
    screen.fill((255, 0, 255))


def backtrack_solve():
    screen.fill((255, 255, 0))


def main_menu():
    run = True
    while run:
        screen.blit(background_img, (0, 0))
        solve_genetic_btn = MenuBtn(image=pygame.image.load(menu_btn_img), pos=(MID_SCREEN_WIDTH, 200),
                                    text_input="GENETIC SOLVE", base_color=(255, 255, 255), hover_color=(0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            solve_genetic_btn.handle_event(event)

        screen.blit(background_img, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


main_menu()
