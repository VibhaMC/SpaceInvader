import pygame
import random

# initialise pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background image
background = pygame.image.load('Space_background.png')

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('spaceship2.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load('space_alien.png')
enemyX = random.randint(0, 800 - 64)
enemyY = random.randint(50, 150)
enemyX_change = 1.5
enemyY_change = 40

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
# ready - we cant see the bullet , Fire - bullet is moving
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # To make bullet appear at the centre of the space ship do x+16 and y+10


# Game loop
running = True
while running:

    # Set background color
    screen.fill((10, 10, 60))
    # backgrong image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if key stroke is pressed, check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            playerX_change = 0
    playerX += playerX_change

    # set boundary for spaceship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 800 - 64:
        playerX = 800 - 64
    enemyX += enemyX_change
    # boundary for enemy
    if enemyX <= 0:
        enemyX = 0
        enemyX_change = 1.5
        enemyY += enemyY_change
    elif enemyX >= 800 - 64:
        enemyX = 800 - 64
        enemyX_change = -1.5
        enemyY += enemyY_change

    # call function to display the player
    player(playerX, playerY)

    # call function to display the enemy
    enemy(enemyX, enemyY)

    # bullet movement
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    # to update the screen (score,position...)
    pygame.display.update()


