import pygame, pygame_gui, GUI_config as cf

# import time # TO BE REMOVED

bg = pygame.image.load(cf.image_dir + "chessboard.png")
ww = bg.get_width()     # get image width
wh = bg.get_height()    # get image height

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
    type = "Pawn"
    if char in "RNBQKP":
        color = "White_"
        char.lower()
    if char == "r" or char == "R":
        type = "Rook"
    elif char == "n" or char == "N":
        type = "Knight"
    elif char == "b" or char == "B":
        type = "Bishop"
    elif char == "q" or char == "Q":
        type = "Queen"
    elif char == "k" or char == "K":
        type = "King"
    piece_name = cf.image_dir + color + type + ".png"
    print(char)
    print(piece_name + " " + str(location[0]) + "," + str(location[1]))
    piece = pygame.image.load(piece_name)
    window.blit(piece, (location[0] / 8 * ww, location[1] / 8 * wh))
