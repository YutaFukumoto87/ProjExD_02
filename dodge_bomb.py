import random
import sys

import pygame as pg

delta = {
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
        }

move_images = {
    (0, -1): pg.transform.rotozoom(pg.image.load("ex01/fig/kk_up.png"), 0, 2.0),
    (0, 1): pg.transform.rotozoom(pg.image.load("ex01/fig/kk_down.png"), 0, 2.0),
    (-1, 0): pg.transform.rotozoom(pg.image.load("ex01/fig/kk_left.png"), 0, 2.0),
    (1, 0): pg.transform.rotozoom(pg.image.load("ex01/fig/kk_right.png"), 0, 2.0),
}


def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]:
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_rct = pg.Rect(900, 400, 0, 0)
    move_keys = []
    kk_img = move_images[(0, -1)]

    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img, (255,0,0), (10,10), 10)
    bb_img.set_colorkey((0,0,0))
    x, y = random.randint(0, 1600), random.randint(0, 900)
    bb_rct = bb_img.get_rect()
    bb_rct.center = (x, y)
    vx, vy = +1, +1

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()
        move_keys = [(key, delta[key]) for key in delta if key_lst[key]]
        move = tuple(sum(move) for _, move in move_keys)

        if move != (0, 0):
            kk_img = move_images[move]
            kk_rct.move_ip(move)
        if check_bound(screen.get_rect(), kk_rct) != (True, True):
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0], -mv[1])


        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko:  
            vx *= -1
        if not tate:  
            vy *= -1
        bb_rct.move_ip(vx, vy)
        screen.blit(bb_img, bb_rct)
        if kk_rct.colliderect(bb_rct):  
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()