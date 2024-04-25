import pygame as pg
import random
pg.mixer.init()
pg.init()

sound = pg.mixer.Sound("../maze game/final_.mp3")

W = 800
H = 800

color = (200, 250, 200)
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Кликер")
screen.fill((200, 250, 200))
rect = pg.draw.rect(screen, color, (0, 200, 600, 600))  # A
button = pg.image.load("not_pressed.png")
like = pg.image.load("like.png")
button = pg.transform.scale(button, (200, 200))
like = pg.transform.scale(like, (100, 100))
button_rect = button.get_rect(center=(400, 400))
like_rect = like.get_rect(center=(600, 600))
clock = pg.time.Clock()

run = True

while run:
    pg.time.delay(100)
    clock.tick(60)
    button = pg.transform.scale(pg.image.load("not_pressed.png").convert(), (200, 200))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                print("clicc")
                sound.play()
                like = pg.transform.scale(pg.image.load("like.png").convert(), (400, 400))
                button = pg.transform.scale(pg.image.load("pressed.png").convert(), (200, 200))
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.blit(button, button_rect)
    pg.display.update()