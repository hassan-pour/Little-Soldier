import pygame as pg
from settings import *
vec = pg.math.Vector2
class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((40, 60))
        self.image.fill(BLUE)
        self.vel = vec(0, 0)
        self.pos = vec(pos)
        self.acc = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.standing = True
    def update(self):
        self.acc = 0.5
        self.vel = vec(0, self.vel.y)
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.vel.x = PLAYER_SPEED

        if keys[pg.K_LEFT]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_UP]:
            if self.standing:
                self.vel.y  = -PLAYER_JUMP
                self.standing = False
        self.vel.y += self.acc
        self.pos += self.vel
        self.rect.center = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, pos, size):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(size)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.topleft = self.pos
