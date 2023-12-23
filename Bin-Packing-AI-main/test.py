import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move Rectangle")

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the rectangle
rect_width, rect_height = 50, 50
rect_x, rect_y = 50, 50

# Function to move the rectangle to a target destination
def move_to_destination(target_x, target_y):
    global rect_x, rect_y
    rect_x, rect_y = target_x, target_y

# Set the target destination for the rectangle
target_destination = (300, 300)

# Draw the initial rectangle


# Add a delay before moving to the destination
pygame.time.delay(2000)  # Delay in milliseconds (2 seconds)

# Move the rectangle to the target destination
move_to_destination(*target_destination)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw the rectangle at its final destination
    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
