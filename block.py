import pygame


class Block:

    def __init__(self, color, pos, hitbox: pygame.Rect, picture=None):
        if picture:
            self.sprite = pygame.image.load(picture).convert_alpha()
        else:
            self.sprite = pygame.surface.Surface((32, 32)).convert_alpha()
            self.sprite.fill(color)
        self.pos = pos
        self.color = color
        self.rect = self.sprite.get_rect().move(pos)
        self.hitbox = hitbox

    def move(self, game_speed):
        self.pos.x -= game_speed
        self.rect.x -= game_speed

    def physic_process(self, game_speed):
        self.move(game_speed)

    def draw(self, screen):
        screen.blit(self.sprite, self.pos)

    def collide_dead(self, sides):
        for index, side in enumerate(sides):
            if side and self.hitbox[index]:
                return True
        return False

    def is_dead_side(self, side):
        return self.hitbox[side]

    def get_sides(self):
        rect = self.rect
        # x, y, width, height
        t = pygame.Rect(
            (rect.x, rect.y),
            (rect.width, 4)
        )
        r = pygame.rect.Rect(
            (rect.x + rect.width - 4, rect.y + 4),
            (4, rect.height - 8)
        )
        b = pygame.rect.Rect(
            (rect.x, rect.y + rect.height - 4),
            (rect.width, 4)
        )
        l = pygame.rect.Rect(
            (rect.x + 4, rect.y + 4),
            (4, rect.height - 8)
        )
        return t, r, b, l

    def collide(self, obj):
        t, r, b, l = self.get_sides()
        return (
            obj.rect.colliderect(t),
            obj.rect.colliderect(r),
            obj.rect.colliderect(b),
            obj.rect.colliderect(l),
        )
