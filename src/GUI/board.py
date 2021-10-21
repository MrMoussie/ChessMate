import pygame, config

bg = config.bg
ww = bg.get_width()     # get image width
wh = bg.get_height()    # get image height
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
    index = 0               # type is used to find the correct piece in the pieces array
    if char in "RNBQKP":
        index += 1          # white pieces are on uneven numbers, black on even
        char = char.lower()
    if char == "k":
        index += 2
    elif char == "n":       # knight is officially referred to as 'n' in FEN since king is already 'k'
        index += 4
    elif char == "p":
        index += 6
    elif char == "q":
        index += 8
    elif char == "r":
        index += 10
    chess_piece = pieces[index]
    window.blit(chess_piece, (location[0] / 8 * ww, location[1] / 8 * wh))  # scale with window size
