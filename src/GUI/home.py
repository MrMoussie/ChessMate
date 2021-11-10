# https://pygame-gui.readthedocs.io/en/latest/quick_start.html#quick-start
# http://bluegalaxy.info/codewalk/2017/10/14/python-how-to-create-gui-pop-up-windows-with-tkinter/

import pygame, pygame_gui, board, config, sys
from tkinter import *
from threading import Thread

sys.path.append("../Chess")
import game, Missions, Leaderboard

sys.path.append("../SQL")
import Connect, Account
import atexit
import time

theme = "theme.json"

pygame.init()
pygame.display.set_caption('ChessMate')
window_surface = pygame.display.set_mode(config.home_size, pygame.RESIZABLE)

pygame.display.set_icon(config.programIcon)

font_color = (0, 150, 250)
font_obj = pygame.font.Font("fonts/segoeprb.ttf", 25)
font_obj_game = pygame.font.Font("fonts/segoeprb.ttf", 15)
font_obj_main = pygame.font.Font("fonts/segoeprb.ttf", 35)
text_obj = font_obj_main.render("ChessMate", True, font_color)

mission_text_obj = font_obj_main.render("Missions", True, font_color)  
mission_easy_text_obj = font_obj.render("Easy", True, font_color)  
mission_medium_text_obj = font_obj.render("Medium", True, font_color)  
mission_hard_text_obj = font_obj.render("Hard", True, font_color)  
mission_expert_text_obj = font_obj.render("Expert", True, font_color)

login_username = font_obj.render("Username", True, font_color) 
login_password = font_obj.render("Password", True, font_color)

register_username = font_obj.render("Username", True, font_color)  
register_email = font_obj.render("E-mail", True, font_color)  
register_password = font_obj.render("Password", True, font_color)  
register_confirm_password = font_obj.render("Confirm Password", True, font_color)  

i = 0

manager = pygame_gui.UIManager(config.home_size, theme)
bob = pygame_gui.UIManager(config.home_size, theme)
petra = pygame_gui.UIManager(config.home_size, theme)
pol = pygame_gui.UIManager(config.home_size, theme)
daan = pygame_gui.UIManager(config.home_size, theme)
players = pygame_gui.UIManager(config.home_size, theme)
MISSIONS = pygame_gui.UIManager(config.home_size, theme)
second = pygame_gui.UIManager(config.home_size, theme)

ButtonLayoutRectL = pygame.Rect(340, 350, 100, 30)
ButtonLayoutRectS = pygame.Rect(340, 400, 100, 30)
ButtonLayoutRectT = pygame.Rect(340, 450, 100, 30)
ButtonLayoutRectU = pygame.Rect(340, 450, 100, 30)
EntryLayoutRectU = pygame.Rect(250, 200, 300, 40)
EntryLayoutRectP = pygame.Rect(250, 300, 300, 40)
EntryLayoutRectR = pygame.Rect(250, 150, 300, 40)
ButtonLayoutRect2 = pygame.Rect(340, 390, 100, 30)

Login = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectL, text='Login', manager=manager)
SignUp = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Sign up', manager=manager)
Quit = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectT, text='Quit', manager=manager)
Username = pygame_gui.elements.UITextEntryLine(relative_rect=EntryLayoutRectU, manager=manager)
Password = pygame_gui.elements.UITextEntryLine(relative_rect=EntryLayoutRectP, manager=manager)
# Username.set_text("Username")
# Password.set_text("Password")

Login2 = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Login', manager=second)
Quit2 = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectT, text='Return', manager=second)
Username2 = pygame_gui.elements.UITextEntryLine(relative_rect=EntryLayoutRectU, manager=second)
Password2 = pygame_gui.elements.UITextEntryLine(relative_rect=EntryLayoutRectP, manager=second)

PlayGame = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectL, text='Play game', manager=bob)
ScoreBoard = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Leaderboard', manager=bob)
Logout = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectU, text='Logout', manager=bob)

# Setting players
Player = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectL, text='Friend', manager=players)
Naive = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='AI level 1', manager=players)
Smart = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectU, text='AI level 2', manager=players)
PlayerNum = 0

# Mission screen
ContinueGame = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectT, text='Continue', manager=MISSIONS)

SignUpScreen = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Sign up', manager=petra)
UsernameEntry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(250, 200, 300, 40), manager=petra)
EmailAddressEntry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(250, 250, 300, 40), manager=petra)
PasswordEntry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(250, 300, 300, 40), manager=petra)
PasswordEntryRepeat = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(250, 350, 300, 40), manager=petra)
# EmailAddressEntry.set_text("Email address")
# UsernameEntry.set_text("Username")
# PasswordEntry.set_text("Password")
# PasswordEntryRepeat.set_text("Repeat password")

GoBack1 = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectU, text='Return', manager=petra)
GoBack2 = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectU, text='Return', manager=pol)
GoBack3 = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectU, text='Return', manager=daan)

clock = pygame.time.Clock()
is_running = True

# Initialize connection to database and set it up
Connect.connect()
Connect.setupDB()


def alert_popup(title, message, path, destroy=False):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400  # popup window width
    h = 200  # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    if destroy:
        root.after(2000, lambda: root.destroy())
        root.mainloop()
        return
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()

## Can be used as an alternative thread checking for exit events while game is running.
# def checkForExit():
#     try:
#         while is_running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     is_running = False
#         pygame.quit()
#     except SystemExit:
#         is_running = False
#         pygame.quit()

#Check if connection is valid to the database
if (not Connect.connectExists()):
    alert_popup("Error", "Program can not connect to SQL with given credentials!", "Please refer to the README file to setup a database.")
    is_running = False

if (not Connect.connectExists):
    alert_popup("Error", "Program can not connect to SQL with given credentials!",
                "Please refer to the README in the SQL folder.")
    time.sleep(5)
    is_running = False

#################################################
## Get missions from missions file and display ##
#################################################
easy_mission = Missions.get_easy_mission()
medium_mission = Missions.get_medium_mission()
hard_mission = Missions.get_hard_mission()
expert_mission = Missions.get_expert_mission()

easy_mission = "" if easy_mission == None else easy_mission.decode('utf-8')
medium_mission = "" if medium_mission == None else medium_mission.decode('utf-8')
hard_mission = "" if hard_mission == None else hard_mission.decode('utf-8')
expert_mission = "" if expert_mission == None else expert_mission.decode('utf-8')

font_obj = pygame.font.Font("fonts/segoeprb.ttf", 25)
mission_color = (0, 0, 0)
mission_color_game = (255, 255, 255)
mission_easy_text = font_obj.render(easy_mission, True, mission_color)  
mission_medium_text = font_obj.render(medium_mission, True, mission_color)  
mission_hard_text = font_obj.render(hard_mission, True, mission_color)  
mission_expert_text = font_obj.render(expert_mission, True, mission_color) 

mission_easy_text_game = font_obj_game.render(easy_mission, True, mission_color_game)  
mission_medium_text_game = font_obj_game.render(medium_mission, True, mission_color_game) 
mission_hard_text_game = font_obj_game.render(hard_mission, True, mission_color_game)  
mission_expert_text_game = font_obj_game.render(expert_mission, True, mission_color_game) 


leaderboard_obj = font_obj_main.render("Leaderboard", True, font_color)  
leaderboard_name = font_obj.render("Name", True, font_color)
leaderboard_elo = font_obj.render("Elo", True, font_color)
leaderboard_points = font_obj.render("Points", True, font_color)
leaderboard_wins = font_obj.render("Wins", True, font_color)
leaderboard_loss = font_obj.render("Loss", True, font_color)
leaderboard_winrate = font_obj.render("Winrate", True, font_color)

name = elo = points = wins = loss = winrate = font_obj.render("", True, mission_color)
click = True

MISSIONS_GAME = [easy_mission, medium_mission, hard_mission, expert_mission]

started_thread = False

while is_running:        
    window_surface.fill((255, 255, 255))
    window_surface.blit(text_obj, (300, 100))
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            Connect.close()
            pygame.quit()
            sys.exit()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == Login:
                    if (Account.login(Username.get_text(), Password.get_text())):
                        i = 1
                    else:
                        alert_popup("Error", "Either your password or username is incorrect.", "Please try again.")
                elif event.ui_element == SignUp:
                    i = 2
                elif event.ui_element == PlayGame:
                    # In this if statement you should call on the game (make the game a separate class)
                    i = 11
                elif event.ui_element == ScoreBoard:
                    # Here we should add the part of the scoreboard, not yet sure how to implement that
                    i = 4
                elif event.ui_element == Logout or event.ui_element == GoBack1:
                    i = 0
                elif event.ui_element == GoBack2:
                    i = 6
                elif event.ui_element == GoBack3:
                    click = True
                    i = 1
                elif event.ui_element == SignUpScreen:
                    i = 7
                ############################################################################
                #############################CHOOSING PLAYERS###############################
                ############################################################################
                elif event.ui_element == Player:
                    i = 12
                    # Username.set_text("username")
                    # Password.set_text("password")
                elif event.ui_element == Login2:
                    i = 12
                    # i = 8
                    if (Username2.get_text() == Username.get_text()):
                        alert_popup("Error", "You can not log in on the same account twice!", "Please try again.")
                    elif (Account.login(Username2.get_text(), Password2.get_text())):
                        #print("hoi")
                        i = 8
                        PlayerNum = 0
                    else:
                        alert_popup("Error", "Either your password or username is incorrect.", "Please try again.")
                #  else:
                #      alert_popup("Error", "1", "2")
                elif event.ui_element == Naive:
                    window_surface = pygame.display.set_mode((config.bg.get_width(), config.bg.get_height()),
                                                             pygame.RESIZABLE)
                    i = 9
                    PlayerNum = 1
                elif event.ui_element == Smart:
                    window_surface = pygame.display.set_mode((config.bg.get_width(), config.bg.get_height()),
                                                             pygame.RESIZABLE)
                    i = 10
                    PlayerNum = 2
                elif event.ui_element == ContinueGame:
                    i = 3
                elif event.ui_element == Quit:
                    is_running = False
                elif event.ui_element == Quit2:
                    i = 3

        if i == 0:
            manager.process_events(event)
        elif i == 1:
            bob.process_events(event)
        elif i == 2:
            petra.process_events(event)
        elif i == 3:
            players.process_events(event)
        elif i == 4:
            daan.process_events(event)
        elif i == 5:
            manager.process_events(event)
        elif i == 6:
            manager.process_events(event)
        elif i == 7:
            bob.process_events(event)
        elif i == 8 or i == 9 or i == 10:
            pol.process_events(event)
        elif i == 11:
            MISSIONS.process_events(event)
        elif i == 12:
            second.process_events(event)
    if i == 0:
        window_surface.blit(login_username, (100, 188))
        window_surface.blit(login_password, (100, 290))

        manager.update(time_delta)
        manager.draw_ui(window_surface)
    elif i == 1:
        bob.update(time_delta)
        bob.draw_ui(window_surface)
    elif i == 2:
        window_surface.blit(register_username, (100, 188))
        window_surface.blit(register_email, (125, 242))
        window_surface.blit(register_password, (100, 290))
        window_surface.blit(register_confirm_password, (10, 342))
        
        petra.update(time_delta)
        petra.draw_ui(window_surface)
    elif i == 3:
        players.update(time_delta)
        players.draw_ui(window_surface)
        # PLAY GAME HERE

        # pol.draw_ui(window_surface)
    elif i == 4:
        result = None if not click else Leaderboard.getLeaderboard()
        click = False
        
        window_surface.fill((255, 255, 255))
        window_surface.blit(leaderboard_obj, (280, 50))

        window_surface.blit(leaderboard_name, (50, 100))
        window_surface.blit(leaderboard_elo, (180, 100))
        window_surface.blit(leaderboard_points, (280, 100))
        window_surface.blit(leaderboard_wins, (420, 100))
        window_surface.blit(leaderboard_loss, (550, 100))
        window_surface.blit(leaderboard_winrate, (650, 100))

        height = 150

        if (result != None):
            for row in result:
                name = name if row[0] == None else font_obj.render(row[0].decode('utf-8'), True, mission_color)  
                elo = elo if row[1] == None else font_obj.render(str(row[1]), True, mission_color)  
                points = points if row[2] == None else font_obj.render(str(row[2]), True, mission_color)  
                wins = wins if row[3] == None else font_obj.render(str(row[3]), True, mission_color)  
                loss = loss if row[4] == None else font_obj.render(str(row[4]), True, mission_color)  
                winrate = winrate if row[5] == None else font_obj.render(str(row[5]), True, mission_color)  
        
        window_surface.blit(name, (50, height))
        window_surface.blit(elo, (180, height))
        window_surface.blit(points, (280, height))
        window_surface.blit(wins, (420, height))
        window_surface.blit(loss, (550, height))
        window_surface.blit(winrate, (650, height))    
        
        height += 40
            
        daan.update(time_delta)
        daan.draw_ui(window_surface)
    elif i == 5:
        manager.update(time_delta)
        manager.draw_ui(window_surface)
    elif i == 6:
        manager.update(time_delta)
        manager.draw_ui(window_surface)
    elif i == 7:
        bob.update(time_delta)
        bob.draw_ui(window_surface)

        if (PasswordEntry.get_text() == "" or PasswordEntryRepeat.get_text() == "" or UsernameEntry.get_text() == "" or EmailAddressEntry.get_text() == ""):
            alert_popup("Error", "Fill in all the fields!", "Please try again.")
        elif (not PasswordEntry.get_text() == PasswordEntryRepeat.get_text()):
            alert_popup("Error", "The two passwords do not match each other!", "Please try again.")
        elif (Account.accountExists(UsernameEntry.get_text())):
            alert_popup("Error", "This user already exists!", "Please try again.")
        elif (Account.emailExists(EmailAddressEntry.get_text())):
            alert_popup("Error", "This email is already taken!", "Please try again.")
        elif (Account.register(UsernameEntry.get_text(), EmailAddressEntry.get_text(), PasswordEntry.get_text())):
            i = 1
            continue
        else:
            alert_popup("Error", "Fill in the fields correctly.", "Please try again.")
        
        i = 2
    elif i == 8 or i == 9 or i == 10:
        start_thread = True
        if start_thread and not started_thread:
            game_thread = Thread(target=game.start, args=(Username2.get_text(), PlayerNum, Username.get_text(), MISSIONS_GAME, alert_popup))
            game_thread.daemon = True
            game_thread.start()
            started_thread = True
            start_thread = False
        window_surface = pygame.display.set_mode((config.bg.get_width() + 375, config.bg.get_height()), pygame.RESIZABLE)
        board.draw_board(game.get_new_fen(), window_surface)
        player_turn = font_obj.render(("Turn: " + game.get_turn()), True, font_color)
        window_surface.blit(mission_text_obj, (575, 140))
        completed = game.get_flags()
        green = (0, 250, 0)
        if completed[0] == 1:
            mission_easy_text_game = font_obj_game.render(easy_mission, True, green)
        if completed[1] == 1:
            mission_medium_text_game = font_obj_game.render(medium_mission, True, green)
        if completed[2] == 1:
            mission_hard_text_game = font_obj_game.render(hard_mission, True, green)
        if completed[3] == 1:
            mission_expert_text_game = font_obj_game.render(expert_mission, True, green)
        window_surface.blit(mission_easy_text_game, (550, 200))
        window_surface.blit(mission_medium_text_game, (550, 250))
        window_surface.blit(mission_hard_text_game, (550, 300))
        window_surface.blit(mission_expert_text_game, (550, 350))
        window_surface.blit(player_turn, (config.bg.get_width() + 50, 50))
        pygame.display.update()
        pol.update(time_delta)
    elif i == 11:
        window_surface.fill((255, 255, 255))
        window_surface.blit(mission_text_obj, (330, 100))
        window_surface.blit(mission_easy_text_obj, (75, 175))
        window_surface.blit(mission_medium_text_obj, (75, 225))
        window_surface.blit(mission_hard_text_obj, (75, 275))
        window_surface.blit(mission_expert_text_obj, (75, 325))
        
        window_surface.blit(mission_easy_text, (200, 175))
        window_surface.blit(mission_medium_text, (200, 225))
        window_surface.blit(mission_hard_text, (200, 275))
        window_surface.blit(mission_expert_text, (200, 325))

        MISSIONS.update(time_delta)
        MISSIONS.draw_ui(window_surface)
    elif i == 12:
        window_surface.blit(login_username, (100, 188))
        window_surface.blit(login_password, (100, 290))
        
        second.update(time_delta)
        second.draw_ui(window_surface)

    # window_surface.blit(background, (0, 0))
    # manager.draw_ui(window_surface)
    # bob.draw_ui(window_surface)

    pygame.display.update()

atexit.register(Connect.close)