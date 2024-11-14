import pygame, random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_pos_x = 0
        mole_pos_y = 0
        while running:
            # Events
            for event in pygame.event.get():
                # Quit Program
                if event.type == pygame.QUIT:
                    running = False
                # Clicked Button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Get row and col of mouse
                    mouse_row = mouse_x // 32
                    mouse_col = mouse_y // 32
                    # print(mouse_row, mouse_col # Testing
                    # Get row and col of mole
                    mole_row = mole_pos_x // 32
                    mole_col = mole_pos_y // 32
                    # Determine if the mole's sector was clicked
                    if (mole_row == mouse_row) and (mole_col == mouse_col):
                        mole_pos_x = random.randrange(0, 20) * 32
                        mole_pos_y = random.randrange(0, 16) * 32
                        # print(mole_pos_x // 32, mole_pos_y // 32) # Test -> Print new mole position

            # Fill Screen
            screen.fill("light green")

            # Draw Grid
            # Rows
            for i in range(1, 16):
                pygame.draw.line(screen, "dark green", (0, (i * 32)), (640, (i * 32)))
            # Columns
            for i in range(1, 20):
                pygame.draw.line(screen, "dark green", ((i * 32), 0), ((i * 32), 512))

            # Draw Mole
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pos_x, mole_pos_y)))

            # Update Screen
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
