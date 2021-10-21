# https://pygame-gui.readthedocs.io/en/latest/quick_start.html#quick-start
# http://bluegalaxy.info/codewalk/2017/10/14/python-how-to-create-gui-pop-up-windows-with-tkinter/

import pygame, pygame_gui
import board, GUI_config as cf
from tkinter import *

pygame.init()

pygame.display.set_caption('ChessMate')
window_surface = pygame.display.set_mode((800, 600))

font_color=(0,150,250)
font_obj=pygame.font.Font("C:\Windows\Fonts\segoeprb.ttf",25)
text_obj=font_obj.render("ChessMate",True,font_color)

i = 0

manager = pygame_gui.UIManager((800, 600))
bob = pygame_gui.UIManager((800, 600))
petra = pygame_gui.UIManager((800, 600))
pol = pygame_gui.UIManager((800, 600))
daan = pygame_gui.UIManager((800, 600))

ButtonLayoutRectL = pygame.Rect(340, 350, 100, 30)
ButtonLayoutRectS = pygame.Rect(340, 400, 100, 30)
ButtonLayoutRectU = pygame.Rect(340, 450, 100, 30)
EntryLayoutRectU = pygame.Rect(250, 200, 300, 40)
EntryLayoutRectP = pygame.Rect(250, 300, 300, 40)
EntryLayoutRectR = pygame.Rect(250, 150, 300, 40)

Login = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectL, text='Login', manager=manager)
SignUp = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Sign up', manager=manager)
Username = pygame_gui.elements.UITextEntryLine(relative_rect=EntryLayoutRectU, manager=manager)
Password = pygame_gui.elements.UITextEntryLine(relative_rect=EntryLayoutRectP, manager=manager)

PlayGame = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectL, text='Play game', manager=bob)
ScoreBoard = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Score board', manager=bob)
Logout = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectU, text='Logout', manager=bob)

SignUpScreen = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Sign up', manager=petra)
FullName = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(250, 150, 300, 40), manager=petra)
EmailAddress = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(250, 200, 300, 40), manager=petra)
UsernameEntry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(250, 250, 300, 40), manager=petra)
PasswordEntry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(250, 300, 300, 40), manager=petra)
PasswordEntryRepeat = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(250, 350, 300, 40), manager=petra)

GoBack1 = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectU, text='Return', manager=petra)
GoBack2 = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectU, text='Return', manager=pol)
GoBack3 = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectU, text='Return', manager=daan)

clock = pygame.time.Clock()
is_running = True

def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()

while is_running:
    window_surface.fill((255, 255, 255))
    window_surface.blit(text_obj, (330, 100))
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == Login:
                    if Username.get_text() == "julia" and Password.get_text() == "1":
# In this if statement you can add the checking with the database part (for logging in)
                        i = 1
                    else:
                        alert_popup("Error", "Either your password or username is incorrect.", "Please try again.")
                if event.ui_element == SignUp:
# In this if statement you can add the part where the new user information is stored in the database (for signing up)
                    i = 2
                if event.ui_element == PlayGame:
                    board.draw_board(cf.START_FEN, window_surface)
# In this if statement you should call on the game (make the game a seperate class)
                    i = 3
                if event.ui_element == ScoreBoard:
# Here we should add the part of the scoreboard, not yet sure how to implement that
                    i = 4
                if event.ui_element == Logout:
                    i = 5
                if event.ui_element == GoBack1 or event.ui_element == GoBack2 or event.ui_element == GoBack3:
                    i = 6

        if(i == 0):
            manager.process_events(event)
        if(i == 1):
            bob.process_events(event)
        if(i == 2):
            petra.process_events(event)
        if(i == 3):
            pol.process_events(event)
        if(i == 4):
            daan.process_events(event)
        if(i == 5):
            manager.process_events(event)
        if(i == 6):
            manager.process_events(event)
    if(i == 0):
        manager.update(time_delta)
        manager.draw_ui(window_surface)
    if(i == 1):
        bob.update(time_delta)
        bob.draw_ui(window_surface)
    if(i == 2):
        petra.update(time_delta)
        petra.draw_ui(window_surface)
    if(i == 3):
        pol.update(time_delta)
        pol.draw_ui(window_surface)
    if(i == 4):
        daan.update(time_delta)
        daan.draw_ui(window_surface)
    if(i == 5):
        manager.update(time_delta)
        manager.draw_ui(window_surface)
    if (i == 6):
        manager.update(time_delta)
        manager.draw_ui(window_surface)

    #window_surface.blit(background, (0, 0))
    #manager.draw_ui(window_surface)
    #bob.draw_ui(window_surface)

    pygame.display.update()
