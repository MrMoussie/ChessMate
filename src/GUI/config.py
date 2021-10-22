import pygame

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
image_dir = "images/"
pieces = ["Bishop", "King", "Knight", "Pawn", "Queen", "Rook"]
home_size = (800, 600)
bg = pygame.image.load("images/chessboard.png")
# bg = pygame.image.load("images/numchessboard.jpg")
bg_offset = 32
use_offset = False
