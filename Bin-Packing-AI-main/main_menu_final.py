import pygame
import sys
from menu_button_module import MenuBtn

pygame.init()

SCREEN_WIDTH = 1530
SCREEN_HEIGHT = 785
MID_WIDTH = SCREEN_WIDTH / 2
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

background_img = pygame.image.load("assets/background.jpg")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
genetic_solve_img = pygame.image.load("assets/genetic_solve_menu_btn.png")
backtrack_solve_img = pygame.image.load("assets/backtrack_solve_menu_btn.png")
quit_image = pygame.image.load("assets/quit_menu_btn.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/ka1.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(MID_WIDTH, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = MenuBtn(image=quit_image, pos=(MID_WIDTH, 460),
                            text_input=None, font=get_font(75), base_color="White", hovering_color="Green", initial_scale=1, target_scale=1)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMenuBtnDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = MenuBtn(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMenuBtnDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(background_img, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(750, 100))

        genetic_solve_btn = MenuBtn(backtrack_solve_img, pos=(750, 300),
                            text_input=None, font=get_font(75), base_color="#d7fcd4", hovering_color="White",initial_scale=0.8, target_scale= 0.9)
        backtrack_solve_btn = MenuBtn(image=pygame.image.load("assets/backtrack_solve_menu_btn.png"), pos=(750, 500),
                            text_input=None, font=get_font(75), base_color="#d7fcd4", hovering_color="White", initial_scale=0.8, target_scale= 0.9)
        exit_btn = MenuBtn(image=pygame.image.load("assets/exit_btn.png"), pos=(750, 670),
                            text_input=None, font=get_font(75), base_color="#d7fcd4", hovering_color="White", initial_scale=0.85, target_scale= 0.95)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for MenuBtn in [genetic_solve_btn, backtrack_solve_btn, exit_btn]:
            MenuBtn.changeColor(MENU_MOUSE_POS)
            MenuBtn.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMenuBtnDOWN:
                if genetic_solve_btn.checkForInput(MENU_MOUSE_POS):
                    play()
                if backtrack_solve_btn.checkForInput(MENU_MOUSE_POS):
                    options()
                if exit_btn.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()