# hi 

import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 25
height = 25
vel = 0
acc = 0
gravity = 1
block_color = (255, 0, 0)
bg_color = (0, 0, 0)

run = True
while run:
    pygame.time.delay(100)

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