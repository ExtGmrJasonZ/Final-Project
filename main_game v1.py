# SPEEDING! - Motorcycle racing game
# Game made by Jason Sianandar - L1AC

import pygame, sys, time, random                                # importing important modules
from Colors_list import *                                       # importing multiple colors to be used later
# Initialize pygame
pygame.init()
# Settings for the display of the game, caption, fps, and the fonts used in the game
display_width = 1366
display_height = 768
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Speeding!")
clock = pygame.time.Clock()
font_name = pygame.font.match_font("cambria")

# Making sprite groups for all sprites, obstacles group, and the finish line in the map
all_sprites = pygame.sprite.Group()
obstacles_sprites = pygame.sprite.Group()
finishline_sprites = pygame.sprite.Group()
border_sprites = pygame.sprite.Group()

# Class for the start button in the start menu
class Start_button():
    def __init__(self):
        self.start_button = pygame.image.load('reference/graphics/start1.png')
        self.start_button = pygame.transform.scale(self.start_button, (200, 200))
        self.start_button_rect = self.start_button.get_rect()
        self.start_button.set_colorkey(Color.White)
# Class for the quit button in the start menu
class Quit_button():
    def __init__(self):
        self.quit_button = pygame.image.load('reference/graphics/quit.png')
        self.quit_button = pygame.transform.scale(self.quit_button, (200, 200))
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button.set_colorkey(Color.White)
# Class for arrows manual after the start menu
class Arrows_manual():
    def __init__(self):
        self.arrow_manual = pygame.image.load('reference/graphics/arrowsmanual.png')
        self.arrow_manual = pygame.transform.scale(self.arrow_manual, (300, 300))
        self.arrow_manual_rect = self.arrow_manual.get_rect()

# class for the Racer in the game
class Racer(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('reference/graphics/bike1-5.png')
        self.image = pygame.transform.scale(self.image,(40,30))
        self.rect = self.image.get_rect()
        self.rect.center =(x, y)
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.x = x
        self.y = y

    # Function for updating the animations as the motorcycle moves around
    def update(self):
        if self.up:
            self.image = pygame.image.load("reference\\graphics\\bike-up.png")
            self.image = pygame.transform.scale(self.image,(40,30))
            self.rect = self.image.get_rect()
        if self.down:
            self.image = pygame.image.load("reference\\graphics\\bike-down.png")
            self.image = pygame.transform.scale(self.image,(40,30))
            self.rect = self.image.get_rect()
        if self.right:
            self.image = pygame.image.load("reference\\graphics\\bike1-5.png")
            self.image = pygame.transform.scale(self.image,(40,30))
            self.rect = self.image.get_rect()
        if self.left:
            self.image = pygame.image.load("reference\\graphics\\bike-left.png")
            self.image = pygame.transform.scale(self.image,(40,30))
            self.rect = self.image.get_rect()
        if self.up and self.right:
            self.image = pygame.image.load("reference\\graphics\\bike-upright.png")
            self.image = pygame.transform.scale(self.image,(40,30))
            self.rect = self.image.get_rect()
        if self.up and self.left:
            self.image = pygame.image.load("reference\\graphics\\bike-upleft.png")
            self.image = pygame.transform.scale(self.image,(40,30))
            self.rect = self.image.get_rect()
        if self.down and self.right:
            self.image = pygame.image.load("reference\\graphics\\bike-downright.png")
            self.image = pygame.transform.scale(self.image,(40,30))
            self.rect = self.image.get_rect()
        if self.down and self.left:
            self.image = pygame.image.load("reference\\graphics\\bike-downleft.png")
            self.image = pygame.transform.scale(self.image,(40,30))
            self.rect = self.image.get_rect()

        self.rect.center = (self.x , self.y)

# Class for the first map
class Map1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, all_sprites)
        self.image = pygame.image.load('reference/graphics/map1.png')
        self.image= pygame.transform.scale(self.image,(1366, 768))
        self.rect = self.image.get_rect()
# class for the obstacles in the map later on
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, all_sprites, obstacles_sprites)
        self.image = pygame.image.load('reference/graphics/tree.png')
        self.image= pygame.transform.scale(self.image,(60, 40))
        self.rect = self.image.get_rect()
# Class for the finish line in the map
class FinishLine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, all_sprites, finishline_sprites)
        self.image = pygame.image.load('reference/graphics/finishline.png')
        self.image = pygame.transform.scale(self.image,(10, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (340, 700)
class Border(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, all_sprites, border_sprites)
        self.image = pygame.image.load('reference/graphics/finishline.png')
        self.image = pygame.transform.scale(self.image,(0, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (350, 700)

# Function for the start menu
def start_menu():
    sb = Start_button()             # Object for the start button
    qb = Quit_button()              # Object for the quit button
    gamedisplays.fill(Color.Beige)
    text_in_game("Press Enter for start ---- Press q for quit", 20, Color.Black, 300, 600)
    text_in_game("SPEEDING!", 40, Color.Black, display_width/2, 100)
    sb.start_button_rect.centerx = display_width/2
    sb.start_button_rect.centery = 300
    qb.quit_button_rect.centerx = display_width/2
    qb.quit_button_rect.centery = 550
    gamedisplays.blit(sb.start_button, sb.start_button_rect)
    gamedisplays.blit(qb.quit_button, qb.quit_button_rect)
    pygame.display.flip()
    wait_for_menu()             # Calling for the function so that we can select options later in the start menu screen

def start_sound():
    start = pygame.mixer.Sound("reference/sound/bikestart.wav")
    start.play()

def hit_sound():
    ouch = pygame.mixer.Sound("reference/sound/slide2.wav")
    ouch.play()

def speeding_sound():
    ngebut = pygame.mixer.Sound("reference/sound/rev4.wav")
    ngebut.play()

# Function for the text in game
def text_in_game(text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gamedisplays.blit(text_surface, text_rect)
# Function for the manual in game
def manual_for_game():
    am = Arrows_manual()
    gamedisplays.fill(Color.Black)
    text_in_game("Press either of these arrows to move the racer", 20, Color.White, 683, 500)
    text_in_game("Finish the track with the time given", 20, Color.White, 683, 550)
    text_in_game("Finish the track with the time given", 20, Color.White, 683, 600)
    am.arrow_manual_rect.centerx = display_width/2
    am.arrow_manual_rect.centery = 400
    gamedisplays.blit(am.arrow_manual, am.arrow_manual_rect)
    pygame.display.flip()
    draw()
    game_loop()

    
'''
def gameover_screen:
'''
# Function so that we can select options in the menu screen
def wait_for_menu():
    waiting = True
    while waiting:
        clock.tick(120)         # FPS rate
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    manual_for_game()
                    if event.key == pygame.K_RETURN:
                        waiting = False
                        start_sound()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


r = Racer(display_height/2, display_width/2)            # Object for Racer
m = Map1()                                              # Object for Map
f = FinishLine()                                        # Object for Finish Line
all_sprites.add(r, f)                                   # adding the racer and finish tree sprite in the map
# Function for displaying everything in the screen
def draw():
    gamedisplays.fill(Color.Blood)
    all_sprites.draw(gamedisplays)
    text_in_game("Time left: {}".format(timer), 20, Color.White, 683, 384)


create_tree = False
bumped = False
play = False
timer_miliseconds = 0
timer = 20           # Timer in the game
# Function for game loop
def game_loop():

    global bumped, create_tree, play, timer, timer_miliseconds
    while not bumped:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True

        hits = pygame.sprite.spritecollide(r, obstacles_sprites, False, pygame.sprite.collide_mask)          # Collision with the obstacles
        finished = pygame.sprite.spritecollide(r, finishline_sprites, False)                                # Collision with the finish line
        border = pygame.sprite.spritecollide(r, finishline_sprites, False)
        if hits:
            if r.left:                                                                           # if collision with the obstacles, you will for stop 0.5 seconds
                r.rect.x = hits[0].rect.right + 200
                hit_sound()
            elif r.right:
                r.rect.x = hits[0].rect.left + 200
                hit_sound()
            elif r.up:
                r.rect.x = hits[0].rect.down + 200
                hit_sound()
            elif r.down:
                r.rect.x = hits[0].rect.up + 200
                hit_sound()
        if finished:                                                                                        # If touch the finish line, it means you have completed the track.
            bumped = True
            play = False
                                                                                                # So you cannot just go backwards to the finish line
     #This is for all the controls for the racer.
        if keys[pygame.K_DOWN and pygame.K_RIGHT]:
            r.x += 1
            r.y += 2
            r.down = True
            r.right = True
            r.left = False
            r.up = False
            speeding_sound()

        if keys[pygame.K_DOWN and pygame.K_LEFT]:
            r.x -= 1
            r.y += 2
            r.down = True
            r.left = True
            r.right = False
            r.up = False
            speeding_sound()

        if keys[pygame.K_UP and pygame.K_RIGHT]:
            r.x += 1
            r.y -= 2
            r.up = True
            r.right = True
            r.left = False
            r.down = False
            speeding_sound()

        if keys[pygame.K_UP and pygame.K_LEFT]:
            r.x -= 1
            r.y -= 2
            r.up = True
            r.left = True
            r.right = False
            r.down = False
            speeding_sound()

        if keys[pygame.K_LEFT]:
            r.x -= 5
            r.left = True
            r.right = False
            r.down = False
            r.up = False
            speeding_sound()

        if keys[pygame.K_RIGHT]:
            r.x += 5
            r.right = True
            r.left = False
            r.down = False
            r.up = False
            speeding_sound()

        if keys[pygame.K_UP]:
            r.y -= 5
            r.up = True
            r.down = False
            r.right = False
            r.left = False
            speeding_sound()

        if keys[pygame.K_DOWN]:
            r.y += 5
            r.down = True
            r.up = False
            r.right = False
            r.left = False
            speeding_sound()


        #
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #         r.rect.x += 0
        #         r.rect.y += 0
        #     if event.key == pygame.K_DOWN and event.key == pygame.K_RIGHT:
        #         r.rect.y += 0
        #         r.rect.x += 0
        #
        #     if event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
        #         r.rect.y += 0
        #         r.rect.x += 0
        #
        #     if event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
        #         r.rect.y += 0
        #         r.rect.x += 0
        #
        #     if event.key == pygame.K_UP and event.key == pygame.K_LEFT:
        #         r.rect.y += 0
        #         r.rect.x += 0

        # For spawning the obstacles randomly on the map
        if not create_tree:
            for i in range(100):
                tree = Obstacle()
                tree.rect.x = random.randint(0, 1366)
                tree.rect.y = random.randint(0, 768)

        create_tree = True
        timer_miliseconds += 1.5
        if timer_miliseconds > 49:
            timer_miliseconds = 0
            timer -= 1





        # Calling the functions to update the sprites, draw, fps rate of 500
        all_sprites.update()
        draw()

        pygame.display.update()
        clock.tick(500)
run = True
# While loop for running
while run:
    start_menu()
    play = True
    if play:
        game_loop()
# Quit
pygame.quit()
quit()

# Reference from Muhammad Erizky Suryaputra, Fernanda Dzaky, GRIP
