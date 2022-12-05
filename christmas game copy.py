import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_SPACE, MOUSEBUTTONDOWN, KEYUP, K_RETURN
from pygame import mixer

import time

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

mixer.music.load('jinglecut.mp3')

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

# ---------------------------
# Initialize global variables
delay = 150

candy_x = delay

corrdinate = [1280, 1350, 1420, 1500, 1560, 1640, 1860, 1930, 2000, 2080, 2150, 2230, 2430, 2500, 2570, 2640, 2720, 2790, 3010, 3080, 3150, 3220, 3290, 3360, 3640, 3720, 3790, 3860, 3930, 4140, 4230, 4300, 4370, 4430, 4510, 4790, 4850, 4920, 4990, 5070, 5140, 5220, 5290, 5370, 5440, 5510, 5580, 5650, 5950, 6010, 6090, 6220, 6290, 6360, 6490, 6560, 6630, 6740, 6780, 7070, 7140, 7210, 7350, 7420, 7490, 7630, 7700, 7770, 7840, 7920, 8210, 8290, 8360, 8510, 8580, 8650, 8800, 8870, 8930, 9030, 9070, 9360, 9420, 9500, 9630, 9710, 9780, 9840, 9920, 9990, 10070, 10150, 10220, 10430, 10500, 10570, 10640, 10700, 10780, 11000, 11070, 11140, 11210, 11290, 11360, 11570, 11640, 11710, 11790, 11850, 11930, 12140, 12210, 12280, 12360, 12430, 12500, 12710, 12780, 12850, 12930, 13000, 13070, 13340, 13410, 13490, 13560, 13640, 13920, 13990, 14060, 14130, 14210, 14280, 14360, 14430, 14500, 14570, 14630, 14700, 14780, 15060, 15130, 15210, 15360, 15420, 15490, 15630, 15700, 15780, 15880, 15920, 16200, 16270, 16340, 16480, 16560, 16630, 16770, 16850, 16920, 16990, 17060, 17340, 17410, 17490, 17630, 17710, 17780, 17910, 17980, 18050, 18160, 18200, 18480, 18560, 18630, 18780, 18850, 18920, 18990, 19070, 19130, 19200, 19270, 19340, 21920, 21990, 22060, 22200, 22270, 22350, 22470, 22550, 22630, 22720, 22770, 23060, 23130, 23200, 23350, 23420, 23490, 23560, 23640, 23780, 23920, 24050, 24210]

playercorrdinate = []

game_start = False
game_state = [True, "menu"]
RUNNING = 0
SCREEN = 1

playerstat = [0, 0, 0, 0]
PREFECT = 0
GOOD = 1
BAD = 2
MISS = 3

score = 0

BLACK = (0, 0, 0)
RED = (255, 0, 0)

font1 = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 150)
font4 = pygame.font.SysFont(None, 40)
menutext = font1.render("Menu", True, BLACK)
instructiontext = font2.render("Press enter to start game", True, BLACK)
gametext = font2.render("press mouse to start music", True, BLACK)
gametext2 = font2.render("press space bar to hit each note", True, BLACK)
scoretext = font3.render("Your score:", True, BLACK)

# ---------------------------

def DIFINLENGTH(playercorrdinate, corrdinate, playerstat):

    difinlength = abs(len(corrdinate)-len(playercorrdinate))

    if len(playercorrdinate) > len(corrdinate):
        del playercorrdinate[-difinlength:]
    elif len(playercorrdinate) < len(corrdinate):
        del corrdinate[-difinlength:]
    
    playerstat[MISS] += difinlength

def MISSING(playercorrdinate, corrdinate, playerstat) :

    DIFINLENGTH(playercorrdinate, corrdinate, playerstat)
    
    for i, num in enumerate (playercorrdinate):
        difference = abs(num - corrdinate[i])
        if difference > 20:
            del corrdinate[i]
            del playercorrdinate[i]
            playerstat[MISS] += 1
            break

def SCORE(playerstat):

    for n, value in enumerate (playercorrdinate):
        if corrdinate[n] - 30 < value <  corrdinate[n] + 30:
            playerstat[PREFECT] += 1 
        elif corrdinate[n] - 40 < value <  corrdinate[n] + 40:
            playerstat[GOOD] += 1 
        else:
            playerstat[BAD] += 1

def SCORINGBOARD(game_state):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state[RUNNING] = False
        elif event.type == QUIT:
            game_state[RUNNING] = False

    screen.fill((0, 160, 215))

    MISSING(playercorrdinate, corrdinate, playerstat)
    SCORE(playerstat)

    game_state[SCREEN] = "over"

    return playerstat
 
def MENU(game_state):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state[RUNNING] = False

            elif event.key ==  K_RETURN:
                game_state[SCREEN] = "game"
        elif event.type == QUIT:
            game_state[RUNNING] = False
    
    screen.fill((0, 160, 215))
    screen.blit(menutext, (WIDTH/2 - 100, 100))
    screen.blit(instructiontext, (120, 200))

def GAME(game_state, game_start, candy_x, playercorrdinate) -> int :
    
    mark_x = 144
    mark_y = 100

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state[RUNNING] = False
            elif event.key ==  K_RETURN:
                game_state[SCREEN] = "menu"
            elif event.key == K_SPACE:
                playercorrdinate.append(abs(candy_x) + delay)

        elif event.type == QUIT:
            game_state[RUNNING] = False
        
        elif event.type == MOUSEBUTTONDOWN: #start game
            mixer.music.play()
            playercorrdinate = []
            candy_x = delay
            game_start = True 
            
        elif event.type == MUSIC_END:
            game_state[SCREEN] = "score" 
            game_start = False
            candy_x = delay
            

    screen.fill((255, 255, 255)) 

    screen.blit(gametext, (80, 300))
    screen.blit(gametext2, (50, 350))
    pygame.draw.circle(screen, RED, (mark_x, mark_y), 30)
    
    if game_start == True:
        for n in corrdinate:
            pygame.draw.circle(screen, RED, (candy_x + n, mark_y), 15)

    return [game_start, candy_x]

def GAMEOVER():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state[RUNNING] = False
        elif event.type == QUIT:
            game_state[RUNNING] = False

    screen.fill((0, 160, 215))

    screen.blit(scoretext, (50, 100))
    screen.blit(scoretext2, (50, 200))
      
# --------------------------- game
while game_state[RUNNING]:

    if game_state[SCREEN] == "menu":
        MENU(game_state)
        playercorrdinate = []
        candy_x = delay
    elif game_state[SCREEN] == "game":
        game_start, candy_x = GAME(game_state, game_start, candy_x, playercorrdinate)
        candy_x -= 10
    elif game_state[SCREEN] == "score":
        if score == 0:
            score = SCORINGBOARD(game_state)
    elif game_state[SCREEN] == "over":
        scoretext2 = font4.render(f"perfect : {playerstat[0]}, good : {playerstat[1]}, bad : {playerstat[2]}, miss : {playerstat[3]}", True, BLACK)
        GAMEOVER()

    # --------------------------- 
    pygame.display.flip()
    clock.tick(30)
    #---------------------------



pygame.quit()