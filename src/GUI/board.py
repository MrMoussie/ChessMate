import pygame, pygame_gui, GUI_config as cf

# import time # TO BE REMOVED

bg = pygame.image.load(cf.image_dir + "chessboard.png")

def draw_board(FEN, window):
    testiterator = 0 # TO BE REMOVED
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
            else:
                draw_piece(x, ([i, j]), window, testiterator)
                testiterator += 1 # TO BE REMOVED
            j+=1
        i += 1
    # time.sleep(5)


def draw_piece(char, location, window, *it):
    color = "Black_"
    type = "Pawn"
    if char in "ABCDEFGH":
        color = "White_"
        char.lower()
    if char == "r":
        type = "Rook"
    elif char == "n":
        type = "Knight"
    elif char == "b":
        type = "Bishop"
    elif char == "q":
        type = "Queen"
    elif char == "k":
        type = "King"
    piece_name = cf.image_dir + color + type + ".png"
    # print(char)
    print("" + str(it[0]) + ". " + piece_name + " " + str(location[0]) + "," + str(location[1]))
    piece = pygame.image.load(piece_name)
    window.blit(piece, (location[0], location[1]))
