import pygame #import the package
pygame.init() #add init statment

#constant vars
HEIGHT, WIDTH = 800, 1600
SQUARE_SIZE = WIDTH // 16
WHITE = (255, 255, 255)
BLACK = (255, 200, 100)
HIGHLIGHT = (0, 255, 0, 100)  # green overlay
#setup screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess Game")


selected_square = None


#load in pawn images
pawn_img = pygame.image.load('images/white_pawn.png')
pawn_img = pygame.transform.scale(pawn_img, (SQUARE_SIZE, SQUARE_SIZE))
#add black pawns
pawn_img_black = pygame.image.load('images/black_pawn.png')
pawn_img_black = pygame.transform.scale(pawn_img_black, (SQUARE_SIZE, SQUARE_SIZE))


pieces = {}
for i in range(16):
    pieces[(i, 6)] = 'white_pawn'
    pieces[(i, 1)] = 'black_pawn'




#draw the board
def draw_board():
    for i in range(16): #rows
        for j in range(8): #cols 8x8
            if (i + j) % 2 == 0: #if even col then white
                color = WHITE
            else: #if odd then black
                color = BLACK
            pygame.draw.rect( #for each one indent 
            screen,
            color,
            (i * SQUARE_SIZE,j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) # i -> 8 j -> 8 

def add_pieces(): #add pawns
        for (x, y), piece in pieces.items():
            if piece == 'white_pawn':
                screen.blit(pawn_img, (x*SQUARE_SIZE, y*SQUARE_SIZE))
            elif piece == 'black_pawn':
                screen.blit(pawn_img_black, (x*SQUARE_SIZE, y*SQUARE_SIZE))



def highlight_square(x, y):
    highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
    highlight_surface.fill(HIGHLIGHT)
    screen.blit(highlight_surface, (x * SQUARE_SIZE, y * SQUARE_SIZE))

def get_square_cords(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return col, row






running = True #setup game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            col, row = get_square_cords(mouse_pos)


            if selected_square is None:
                selected_square = (col, row)
                if selected_square:
                    piece = pieces[selected_square]
                    pieces[(col, row)] = piece
                    del pieces[selected_square]
                    selected_square = None
            else:
                selected_square = None

    draw_board() #draw baord
    add_pieces() #draw pieces

    if selected_square:
        highlight_square(*selected_square)
    pygame.display.flip() #refresh screen
pygame.quit()