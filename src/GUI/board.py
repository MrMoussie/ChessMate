import pygame, pygame_gui, GUI_config as cf

# import time # TO BE REMOVED

bg = cf.bg
ww = bg.get_width()     # get image width
wh = bg.get_height()    # get image height
pieces = []
for piece in cf.pieces:
    pieces.append(pygame.image.load("" + cf.image_dir + "Black_" + piece + ".png"))
    pieces.append(pygame.image.load("" + cf.image_dir + "White_" + piece + ".png"))

def draw_board(FEN, window):
    window.blit(bg, (0, 0))
    i = 0           # the rows of the chessboard
    index = 0       # keep track of where in the FEN-string you are
    while i < 8:
        j = 0       # the columns of the chessboard
        while j < 8:
            x = FEN[index]
            index += 1
            if x == '/':
                continue
            elif x.isdigit():
                j+=int(x)
                continue
            else:
                draw_piece(x, ([j, i]), window)
            j+=1
        i += 1
    # time.sleep(5)


def draw_piece(char, location, window):
    color = "Black_"
    type = 0                # type is used to find the correct piece in the pieces[] array
    if char in "RNBQKP":
        type += 1           # white pieces are on uneven numbers, black on even
        char = char.lower()
    if char == "k":
        type += 2
    elif char == "n":       # knight is officially referred to as 'n' in FEN since king is already 'k'
        type += 4
    elif char == "p":
        type += 6
    elif char == "q":
        type += 8
    elif char == "r":
        type += 10
    # print(char)
    # print(piece_name + " " + str(location[0]) + "," + str(location[1]))
    # piece_name = cf.image_dir + color + type + ".png"
    # piece = pygame.image.load(piece_name)
    piece = pieces[type]
    window.blit(piece, (location[0] / 8 * ww, location[1] / 8 * wh))
