import pygame
import config

bg = config.bg
ww = bg.get_width()     # get image width
wh = bg.get_height()    # get image height
offset = 0
if config.use_offset:
    ww = ww - config.bg_offset * 2
    wh = wh - config.bg_offset * 2
    offset = config.bg_offset
pieces = []
for piece in config.pieces:
    pieces.append(pygame.image.load("" + config.image_dir + "Black_" + piece + ".png"))
    pieces.append(pygame.image.load("" + config.image_dir + "White_" + piece + ".png"))


def draw_board(FEN, window):
    window.blit(bg, (0, 0))
    i = 0           # i tracks the rows of the chessboard
    index = 0       # index points to a location in the FEN-string
    while i < 8:
        j = 0       # j tracks the columns of the chessboard
        while j < 8:
            x = FEN[index]      # select the current character from the FEN-string
            index += 1
            if x == '/':        # end of the row on the board, continue
                continue
            elif x.isdigit():   # if x is a number, skip x columns and continue
                j += int(x)
                continue
            else:
                draw_piece(x, ([j, i]), window)  # reverse order of i and j since y = j = row, and x = i = column
            j += 1
        i += 1


def draw_piece(char, location, window):
    index = 0               # index is used to find the correct piece in the pieces array
    if char in "RNBQKP":    # white pieces are represented as uppercase letters
        index += 1          # here white pieces are on uneven numbers, black on even
        char = char.lower()
    if char == "k":
        index += 2
    elif char == "n":       # the knight is officially referred to as 'n' in FEN since king is already 'k'
        index += 4
    elif char == "p":
        index += 6
    elif char == "q":
        index += 8
    elif char == "r":
        index += 10
    place_piece(index, location, window)


def place_piece(index, location, window):
    # The game expects square pieces and a square board
    # It takes into account offset from numbering/letters on the side of the board, as well as the size of the board
    # It then scales everything accordingly
    # This should also allow for selecting different backgrounds or chess piece sprites on the fly
    chess_piece = pieces[index]
    scale_size = (ww / 8, ww / 8)   # scale according to the size of the board
    chess_piece = pygame.transform.scale(chess_piece, scale_size)
    place = (location[0] / 8 * ww + offset, location[1] / 8 * wh + offset)
    window.blit(chess_piece, place)  # scale with window size

