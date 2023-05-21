import pygame

from player import Player
from level import Level


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.player = Player()
        self.level = Level()
        self.background = pygame.surface.Surface([800, 600])
        self.background.fill((0, 0, 255))

        self.is_work = True
        self.gravity = 4

    def load_level(self):
        pass

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.level.draw(self.screen)
        self.player.draw(self.screen)

        pygame.display.update()
        pygame.time.delay(16)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_work = False

    def physic_process(self):
        self.player.physic_process(self.gravity)
        self.level.move(4)

        self.player.is_droping = True
        for row in self.level.get_visible_map():
            for col in row:
                res = col.collide(self.player)
                if True in res and col.color.a > 0:
                    self.player.is_droping = False
                    self.player.compensate_dropping(col)
                    res = col.collide(self.player)
                    is_dead = col.collide_dead(res)
                    if is_dead:
                        print("I am dead, man...")
                        exit(1)

    def run(self):
        while self.is_work:
            self.physic_process()
            self.check_events()
            self.draw()
