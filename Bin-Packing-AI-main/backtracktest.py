import pygame
from bin_module import Bin
from items_module import Item
from button_module import Button

pygame.init()

screen = pygame.display.set_mode((800, 600))
num_of_bins = 2
speed = 6
reached_destination = False
run = True
clock = pygame.time.Clock()  # Correct initialization of clock

items = [Item(0, 50, 50, 4, 50), Item(1, 50, 100, 4, 100), Item(2, 50, 150, 4, 30), Item(3, 50, 200, 4, 20)]
bins = [Bin(400, 50, 22, 100, (0, 0, 0), 0), Bin(450, 50, 22, 100, (0, 0, 0), 1)]
original_positions = {item.index: (item.x, item.y, item.width, item.height) for item in items}
all_solutions = []  # Initialize all_solutions as a global variable


def move_item(item, target_x, target_y, bin_height):
    if not item.reached_destination:
        if item.x < target_x:
            item.x += speed
            if item.x > target_x:
                item.x = target_x
                print(f"{item.width}, \n {target_x}, \n {target_y}")
                if item.width == bin_height:
                    pass
                else:
                    item.y = target_y + item.size + 10
        elif item.x > target_x:
            item.x -= speed
            if item.x < target_x:
                item.x = target_x
                print(f"{item.width}, \n {target_x}, \n {target_y}")
                if item.width == bin_height:
                    pass
                else:
                    item.y = target_y + item.size + 10
        if item.y > target_y:
            item.y -= speed
            if item.y < target_y:
                item.y = target_y
            if item.y < target_y:
                item.y += speed
                if item.y > target_y:
                    item.y = target_y
            elif item.y > target_y:
                item.y -= speed
                if item.y < target_y:
                    item.y = target_y
        if item.x == target_x and not reached_destination:
            item.width, item.height = item.height, item.width
            item.reached_destination = True

    pygame.draw.rect(screen, item.color, (item.x, item.y, item.width, item.height))
    screen.blit(item.label_size, ((item.x + item.width // 2) - item.label_size.get_width() // 2,
                                  item.y + item.height // 2 - item.label_size.get_height() // 2))
    return item.reached_destination


def reset_item(item, original_position):
    item.x, item.y, item.width, item.height = original_position


def bin_packing_backtracking(items, bins):
    def backtracking_util(current_bin, remaining_items, bin_assignment, all_solutions):
        nonlocal best_solution, best_num_bins

        if not remaining_items:
            # All items have been packed
            if current_bin < best_num_bins:
                best_num_bins = current_bin
                best_solution = bin_assignment.copy()
            return

        for a_bin in bins:
            if a_bin.height >= remaining_items[0].width:  # Check item size instead of item value
                a_bin.height -= remaining_items[0].width
                bin_assignment[remaining_items[0].index] = (a_bin, remaining_items[0])
                all_solutions.append(bin_assignment.copy())  # Append a copy to avoid modifying the same dictionary
                backtracking_util(current_bin, remaining_items[1:], bin_assignment, all_solutions)

                # Backtrack
                a_bin.height += remaining_items[0].width
                bin_assignment.pop(remaining_items[0].index, None)  # Use pop to avoid KeyError

    # Initialization
    best_solution = {}
    best_num_bins = float('inf')
    bin_assignment = {}

    backtracking_util(0, items, bin_assignment, all_solutions)

    # Return the actual number of bins used, the items in each bin, and all solutions
    return best_solution, len(set(location for location, size in best_solution.values())), all_solutions


def backtrack_solve():
    global reached_destination
    reached_destination = False  # Reset global flag
    solution, num_used_bins, _ = bin_packing_backtracking(items, bins)
    print(all_solutions)
    print(type(all_solutions))
    # Print used bins and their items
    print("\nUsed Bins:")
    for bin_index in range(num_used_bins):
        bin_items = [item.text for item, (location, size) in solution.items() if location == bin_index]
        print(f"Bin {bin_index}: {bin_items}")

    # Print the number of used bins
    if num_used_bins <= 0:
        print("You can't fit it all!")
    else:
        print("\nNumber of Bins Used:", num_used_bins)

        # Move items to their respective bins
        for idx, sol in enumerate(all_solutions, start=1):
            print(f"\nSolution {idx}:")
            for bin, item in sol.values():
                print(f"Bin {bin.index}: {item.width}")
                og_pos = original_positions[item.index]

                # Move item to its destination
                print(f"bin pos{bin.x}: {bin.y}")
                while not move_item(item, bin.x, bin.y, bin.height):
                    screen.fill((255, 255, 255))
                    solve_backtrack_button.draw(screen)

                    for current_item in items:
                        pygame.draw.rect(screen, current_item.color, (current_item.x, current_item.y,
                                                                      current_item.width, current_item.height))
                        screen.blit(current_item.label_size,
                                    ((current_item.x + current_item.width // 2) -
                                     current_item.label_size.get_width() // 2,
                                     current_item.y + current_item.height // 2 -
                                     current_item.label_size.get_height() // 2))

                    for a_bin in bins:
                        a_bin.draw(screen)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        solve_backtrack_button.handle_event(event)

                    pygame.display.update()
                    clock.tick(60)
                # Pause for a short time before resetting
                item.reached_destination = False  # Reset the flag for the next iteration

                # Reset the item after reaching its destination
            if idx < len(all_solutions):
                for item_index, (original_x, original_y, original_width, original_height) in original_positions.items():
                    item = next(item for item in items if item.index == item_index)
                    reset_item(item, (original_x, original_y, original_width, original_height))
                reset_item(item, (original_x, original_y, original_width, original_height))


solve_img = pygame.image.load('assets/solve_btn.png')
solve_backtrack_button = Button(0, 400, solve_img, backtrack_solve, 0.8)
while run:
    screen.fill((255, 255, 255))

    solve_backtrack_button.draw(screen)

    for item in items:
        pygame.draw.rect(screen, item.color, (item.x, item.y, item.width, item.height))
        screen.blit(item.label_size,
                    ((item.x + item.width // 2) - item.label_size.get_width() // 2,
                     item.y + item.height // 2 - item.label_size.get_height() // 2))

    for a_bin in bins:
        a_bin.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        solve_backtrack_button.handle_event(event)

    pygame.display.update()

pygame.quit()
