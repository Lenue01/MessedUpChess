import pygame
import sys


pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Variations Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 40)

# Menu options
menu_options = ["Classic Chess", "Vanish Chess", "Exit"]
selected_option = 0

def draw_menu():
    screen.fill(WHITE)

    title_text = font.render("F'D Up Chess", True, BLACK)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 80))

    for i, option in enumerate(menu_options):
        color = BLACK if i == selected_option else GRAY
        option_text = small_font.render(option, True, color)
        screen.blit(option_text, (WIDTH//2 - option_text.get_width()//2, 200 + i*60))

    pygame.display.flip()

def menu_loop():
    global selected_option

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == "Exit":
                        pygame.quit()
                        sys.exit()
                    else:
                        return menu_options[selected_option]

        draw_menu()

# Run the menu
choice = menu_loop()
print(f"You chose: {choice}")

# Example: route to different games
if choice == "Classic Chess":
    import main
    main.main()
if choice == "Vanish Chess":
    import vanish_game
    vanish_game.main()



