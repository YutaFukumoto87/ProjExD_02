import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    
    bomb_radius = 10
    bomb_color = (255, 0, 0)
    bomb_img = pg.Surface((bomb_radius * 2, bomb_radius * 2))
    bomb_img.fill((0, 0, 0))
    pg.draw.circle(bomb_img, bomb_color, (bomb_radius, bomb_radius), bomb_radius)
    bomb_img.set_colorkey((0, 0, 0))
    bomb_rect = bomb_img.get_rect()
    bomb_rect.center = (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))
    screen.blit(bomb_img, bomb_rect)

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])

        screen.blit(bomb_img, bomb_rect)


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()