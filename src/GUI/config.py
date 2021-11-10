import pygame

import os
dir = os.path.dirname(os.path.abspath(__file__))

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
image_dir = dir + "/images/"
pieces = ["Bishop", "King", "Knight", "Pawn", "Queen", "Rook"]
home_size = (800, 600)
bg = pygame.image.load(dir + "/images/numchessboard.jpg")
bg = pygame.transform.scale(bg, (512, 512))
programIcon = pygame.image.load(dir + '/images/icon.png')
bg_offset = 39
use_offset = True