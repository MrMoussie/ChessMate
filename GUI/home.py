# https://pygame-gui.readthedocs.io/en/latest/quick_start.html#quick-start
import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('ChessMate')
window_surface = pygame.display.set_mode((800, 600))

font_color=(0,150,250)
font_obj=pygame.font.Font("C:\Windows\Fonts\segoeprb.ttf",25)
# Render the objects
text_obj=font_obj.render("ChessMate",True,font_color)

i = 0

#background = pygame.Surface((800, 600))
#background.fill(pygame.Color('#FFFFFF'))

manager = pygame_gui.UIManager((800, 600))
bob = pygame_gui.UIManager((800, 600))
# def Test():
#     ButtonLayoutRectL = pygame.Rect(340, 350, 100, 30)
#     Login = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectL, text='Login', manager=manager)

ButtonLayoutRectL = pygame.Rect(340, 350, 100, 30)
ButtonLayoutRectS = pygame.Rect(340, 400, 100, 30)
EntryLayoutRectU = pygame.Rect(250, 200, 300, 40)
EntryLayoutRectP = pygame.Rect(250, 300, 300, 40)

Login = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectL, text='Login', manager=manager)
SignUp = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Sign up', manager=manager)
Username = pygame_gui.elements.UITextEntryLine(relative_rect=EntryLayoutRectU, manager=manager)
Password = pygame_gui.elements.UITextEntryLine(relative_rect=EntryLayoutRectP, manager=manager)

PlayGame = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectL, text='Play game', manager=bob)
ScoreBoard = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Score board', manager=bob)
Logout = pygame_gui.elements.UIButton(relative_rect=ButtonLayoutRectS, text='Logout', manager=bob)


clock = pygame.time.Clock()
is_running = True

while is_running:
    window_surface.fill((255, 255, 255))
    window_surface.blit(text_obj, (330, 100))

    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                print(i)
                if event.ui_element == Login:
                    i = 1
                    print(i)
                   # LoginPage()
                    print('Hello World!') #when the button is pressed hello world in printed in the command line
                    #check if the entryboxes contain correct information
                    #if not give error message

        #manager.process_events(event)
        if(i == 0):
            manager.process_events(event)
        if(i == 1):
            bob.process_events(event)
    if(i == 0):
        manager.update(time_delta)
        manager.draw_ui(window_surface)
    if(i == 1):
        bob.update(time_delta)
        bob.draw_ui(window_surface)

    #window_surface.blit(background, (0, 0))
    #manager.draw_ui(window_surface)
    #bob.draw_ui(window_surface)

    pygame.display.update()