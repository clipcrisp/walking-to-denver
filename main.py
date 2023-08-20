import pygame as pg

def input_controller():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
    return True

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

while running:
    running = input_controller()

    screen.fill("black")

    notofont = pg.Font("./assets/NotoSans-Regular.ttf", 18)

    img = notofont.render("That boy ain't right.", False, "white")
    screen.blit(img, (20,20))

    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()

