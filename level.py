from block import Block

import pygame
import csv


class Level:

    def __init__(self):
        self.symb_map = self.load_symb_map()
        self.map = self.load_map()
        self.map_details = None
        self.image = self.map_details

    def load_symb_map(self):
        level = list()
        with open("level_1.csv", newline='') as csvfile:
            rows = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in rows:
                level.append(row)
        return level

    def load_map(self):
        level = list()
        pos = pygame.Vector2(0, 32)
        for row in self.symb_map:
            row_list = list()
            pos.x = 0
            for col in row:
                if col == "-1":
                    row_list.append(
                        Block(
                            pygame.Color(0, 0, 0, 0), pos.copy(),
                            (False, False, False, False)  # top, right, bottom, left
                        )
                    )
                if col == "0":
                    row_list.append(
                        Block(
                            pygame.Color(100, 200, 100), pos.copy(),
                            (False, True, True, True), picture="block.png"
                        )
                    )  # , picture="block.png"))
                if col == "Spike":
                    row_list.append(
                        Block(
                            pygame.Color(200, 100, 200), pos.copy(),
                            (True, True, True, True), picture="spike.png"
                        )
                    )
                if col == "Orb":
                    row_list.append(
                        Block(
                            pygame.Color(115, 235, 0), pos.copy(),
                            (False, False, False, False)
                        )
                    )
                if col == "T":
                    row_list.append(
                        Block(
                            pygame.Color(0, 235, 0), pos.copy(),
                            (False, False, False, False)
                        )
                    )
                if col == "Coin":
                    row_list.append(
                        Block(
                            pygame.Color(23, 0, 123), pos.copy(),
                            (False, False, False, False)
                        )
                    )  # , picture="coin.png"))
                if col == "End":
                    row_list.append(
                        Block(
                            pygame.Color(255, 255, 255), pos.copy(),
                            (False, False, False, False)
                        )
                    )
                self.map_details = col
                pos.x += 32
            level.append(row_list)
            pos.y += 32
        return level

    def get_visible_map(self):
        visible_map = list()
        for row in self.map:
            visible_row = list()
            for col in row:
                if col.pos.x > -32 and col.pos.x < 832:
                    visible_row.append(col)
            visible_map.append(visible_row)
        return visible_map

    def move(self, game_speed):
        for row in self.map:
            for col in row:
                col.move(game_speed)

    def draw(self, screen):
        for row in self.get_visible_map():
            for col in row:
                if col.color.a != 0:
                    col.draw(screen)
