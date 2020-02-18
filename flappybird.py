# hi 

import pygame

pygame.init()

display_width = 500
display_height = 500

win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("FlappyBird")

x = 50
y = 50
vel = 0
acc = 0
gravity = 0.01
block_color = (255, 0, 0)
bg_color = (0, 0, 0)
bgImg = pygame.image.load('bg.png').convert()
birdImg = pygame.image.load('bird.png')
cooldown = 100


def bird(x,y):
    win.blit(birdImg, (x,y))

def bg():
    win.blit(bgImg, (0,0))

run = True
while run:
    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        acc = 0
        vel = 0
        if y < 100:
            y = 0
        else:
            y -= 50
    else:
        acc += gravity
        vel += acc
        if y >= display_height - 100:
            y = display_height - 100
        else:
            y += vel

    pygame.event.clear()

    bg()
    bird(x, y)
    pygame.display.update()


pygame.quit()