# hi 

import pygame

pygame.init()

display_width = 500
display_height = 500

win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("FlappyBird")

x = 50
y = 50
width = 25
height = 25
vel = 0
acc = 0
gravity = 1
block_color = (255, 0, 0)
bg_color = (0, 0, 0)

bird = pygame.image.load("")

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        acc = 0
        vel = 0
        y -= 100
    else:
        acc += gravity
        vel += acc
        y += vel

    
    win.fill(bg_color)

    pygame.draw.rect(win, block_color, (x, y, width, height))
    pygame.display.update()


pygame.quit()