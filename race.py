import tkinter
import pygame
import random
import math
import time
from pygame import mixer
pygame.init()
size = [800, 600]
black = [0, 0, 0]



# for displaying screen
screen = pygame.display.set_mode(size)

# for displaying caption
pygame.display.set_caption("CAR CHAMPS")

# displaying the icon of the game
game_icon = pygame.image.load(r'C:\Users\DELL\Downloads\spaceship.png')
pygame.display.set_icon(game_icon)

# for displaying back image


# for background music
mixer.music.load(r'C:\Users\DELL\Downloads\back.mp3')
mixer.music.play(-1)
# car details
carimage = pygame.image.load(r'C:\Users\DELL\Downloads\car.png')
carX = 400
carY = 500
carX_change = 0.3

def car(x, y):
    screen.blit(carimage, (x, y))                 # prints the image on the screen

# barrier details
obstacleimg = pygame.image.load(r'C:\Users\DELL\Downloads\barrier.png')
barrierX = random.randint(200, 600)               # randomly selects the coordinates of x axis
barrierY = 0                                      # from where the barrier starts
barrierY_change = 1.5                              # speed with which the barrier decsends

def barrier(x, y):
    screen.blit(obstacleimg, (x, y))              # prints the image on the screen


def game_over(x, y):
    font = pygame.font.Font('freesansbold.ttf', 100)
    over = font.render("GAME OVER:", True, [255, 0, 0])
    screen.blit(over, (x, y))

    expsound.play()
    time.sleep(1.5)
# score details
scoreX=10
scoreY=10
score1=pygame.font.Font('freesansbold.ttf', 55)

# function for displaying of score
def disp_score(x,y):
    s=score1.render("SCORE:"+str(score),True,[0,0,255])
    screen.blit(s,(x,y))

# function for collision with barrier
def collission(barrX, barrY, cX, cY):
    distance = math.sqrt((math.pow(cX - barrX, 2)) + (math.pow(cY - barrY, 2)))
    if 10<distance<30:
        game_over(100, 200)

score=0                                                  # initailize score to 0
running = True
while (running):
    screen.fill((5,255,255))
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                 carX_change = -3
             if event.key == pygame.K_RIGHT:
                 carX_change = 3
         if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 carX_change = 0
    carX = carX + carX_change
    # for the barrier movement
    if barrierY <= 600:
        barrierY = barrierY + barrierY_change
     # boundries of the car
    if carX > 600:
         carX = 600
    elif carX < 200:
        carX = 200
    # for the repetation of the barriers
    if barrierY > 600:
        barrierY = 0
        barrierX = random.randint(200, 600)
        score=score+1         # increase the score every time when barrier moves above 600




    disp_score(scoreX,scoreY)                             # function call to disp_score
    car(carX, carY)                                       # function call to car
    collission(barrierX, barrierY, carX, carY)
    barrier(barrierX, barrierY)                           # function call to barrier
    pygame.display.update()
    # it updates the changes done in the code
