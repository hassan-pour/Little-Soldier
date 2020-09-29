import pygame as pg
from settings import*
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player((WIDTH / 2, HEIGHT / 2))

    def new(self):
        self.all_sprites.add(self.player)
        p = Platform((0, HEIGHT - 50), (WIDTH, 50))
        self.all_sprites.add(p)
        self.platforms.add(p)
        p = Platform((50, 240), (100, 20))
        self.all_sprites.add(p)
        self.platforms.add(p)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                if self.playing:self.playing = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.player.standing = True
    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            if vec(self.player.rect.center).y < vec(hits[0].rect.center).y:
                self.player.vel.y = 0
                self.player.rect.bottom = hits[0].rect.top - 1
                self.player.pos = self.player.rect.center
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

g = Game()
while g.running:
    g.new()
pg.quit()
