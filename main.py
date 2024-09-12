import os
import shutil
from pygame import *

init()
screen = display.set_mode((1200, 1000))

tile_size = 100


def draw_grid():
    for line in range(0, 12):
        draw.line(screen, (255, 255, 255), (0, line * tile_size), (1200, line * tile_size))
        draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, 1000))


class Player:
    def __init__(self, x, y):
        self.image = transform.scale(image.load("img/Doorright.png"), (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        dx = 0
        dy = 0

        keys = key.get_pressed()
        if keys[K_a]:
            dx -= 0.51
        if keys[K_d]:
            dx += 0.51
        if keys[K_w]:
            dy -= 0.51
        if keys[K_s]:
            dy += 0.51
        if not keys[K_a] and not keys[K_d]:
            dx = 0
        if not keys[K_w] and not keys[K_s]:
            dy = 0

        for tile in world.tile_list:

            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0

        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.image, self.rect)
        draw.rect(screen, (255, 255, 255), self.rect, 2)


class World:
    def __init__(self, data):
        self.tile_list = []

        door = image.load('img/Doorright.png')
        doorl = image.load('img/Doorleft.png')
        darklog = image.load('img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = transform.scale(door, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = transform.scale(doorl, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == "/":
                    img = transform.scale(darklog, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


room_start = [
    ["/", "/", "/", "/", "/", 2, 1, "/", "/", "/", "/", "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"]]

world = World(room_start)
player = Player(580, 800)

run = True
while True:
    screen.fill((0, 0, 0))
    world.draw()
    player.update()

    draw_grid()

    for e in event.get():
        if e.type == QUIT:
            exit()

    print(mouse.get_pos())

    display.update()
