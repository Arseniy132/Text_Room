import os
import shutil
from pygame import *

init()
font.init()

dos = font.Font("fnt/ModernDOS9x16.ttf", 45)
dos_small = font.Font("fnt/ModernDOS9x16.ttf", 20)
dos_smaller = font.Font("fnt/ModernDOS9x16.ttf", 10)

screen = display.set_mode((1200, 1000))

tile_size = 100

room = [
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
room1 = [
    ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"]]
room2 = [
    ["/", "/", "/", "/", "/", 2, 1, "/", "/", "/", "/", "/"],
    ["/", "§", 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"]]
room3 = [
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
room_count = 0
level = 0


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
        global room_count, world
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

        darklog = image.load('img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    dooor = Door(col_count * 100, row_count * 100, "left")
                    door_group.add(dooor)
                if tile == 2:
                    dooor = Door(col_count * 100, row_count * 100, "right")
                    door_group.add(dooor)
                if tile == "/":
                    img = transform.scale(darklog, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == "§":
                    locker = Locker(col_count * 100, row_count * 100)
                    locker_group.add(locker)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Door(sprite.Sprite):
    def __init__(self, x, y, direction):
        sprite.Sprite.__init__(self)
        if direction == "left":
            img = image.load("img/Doorright.png")
            self.image = transform.scale(img, (100, 100))
        if direction == "right":
            img = image.load("img/Doorleft.png")
            self.image = transform.scale(img, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Locker(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        img = image.load("img/Doorright.png")
        self.image = transform.scale(img, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




door_group = sprite.Group()
locker_group = sprite.Group()

world = World(room)
player = Player(580, 800)

run = True
while True:
    screen.fill((0, 0, 0))
    world.draw()
    player.update()
    door_group.draw(screen)
    locker_group.draw(screen)

    draw_grid()

    for e in event.get():
        if e.type == QUIT:
            exit()

    if sprite.spritecollide(player, locker_group, False):
        Enter_Locker = dos.render("Press space to enter the locker.", True, (175, 175, 175))
        screen.blit(Enter_Locker, (125, 800))

    if sprite.spritecollide(player, door_group, False):
        level += 1
        door_group.empty()
        locker_group.empty()
        player.rect.x = 580
        player.rect.y = 800
        if level == 1:
            world = World(room1)
        elif level == 2:
            world = World(room2)
        elif level == 3:
            world = World(room3)

    print(mouse.get_pos())

    display.update()
