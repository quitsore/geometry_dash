import pygame

import block


class Player:

    def __init__(self):
        self.sprite = pygame.surface.Surface([32, 32])
        self.sprite.fill(pygame.Color(255, 255, 255))
        self.pos = pygame.Vector2(128, 450)
        self.direction = pygame.Vector2(0, 0)
        self.rect = self.sprite.get_rect().move(self.pos)

        self.is_droping = True
        self.jumping = True
        self.jump_speed = 0
        self.initial_jump_speed = 0
        self.jump_dy = 0.5

    def jump(self, initial_speed):
        if not self.jumping:
            self.initial_jump_speed = initial_speed
            self.jumping = True
            self.jump_speed = initial_speed

    def jump_process(self, gravity):
        if self.jumping:
            self.direction.y -= self.jump_speed + gravity
            self.jump_speed -= self.jump_dy
            if self.jump_speed <= 0:
                self.jumping = False

    def check_keys(self):
        keys = pygame.key.get_pressed()
        mkeys = pygame.mouse.get_pressed()

        jump_keys = [
            keys[pygame.K_SPACE],
        ]
        jump_keys.extend(mkeys)

        if True in jump_keys and not self.is_droping:
            self.jump(10)

    def gravity_process(self, gravity):
        if self.is_droping:
            self.direction.y += gravity - self.jump_speed
            self.jump_speed -= self.jump_dy

    def physic_process(self, gravity):
        self.direction = pygame.Vector2(0, 0)
        self.check_keys()
        self.jump_process(gravity)
        self.gravity_process(gravity)
        self.pos += self.direction
        self.rect.x, self.rect.y = self.pos

    def draw(self, screen):
        screen.blit(self.sprite, self.pos)

    def compensate_dropping(self, blck: block.Block):
        check = blck.collide(self)
        if self.jumping and check[2]:
            if not blck.is_dead_side(2):
                # compensate overlapping
                self.pos.y = blck.pos.y + blck.rect.height - 1
                self.rect.y = self.pos.y
        if not self.jumping and check[0]:
            if not blck.is_dead_side(0):
                self.pos.y = blck.pos.y - self.rect.height + 1
                self.rect.y = self.pos.y
