import os, shutil, pygame
from random import randint

pygame.init()
pygame.font.init()
pygame.init()

walk = pygame.mixer.Sound("snd/walk_entity.flac")
start_snd = pygame.mixer.Sound("snd/start.flac")
fnt = "fnt/ModernDOS9x16.ttf"
door = "img/Doorright.png"

locker = pygame.image.load("img/locker.png")

dos = pygame.font.Font(fnt, 45)
dos_small = pygame.font.Font(fnt, 20)
dos_smaller = pygame.font.Font(fnt, 10)

screen = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption(" ")

clock = pygame.time.Clock()

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
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
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
room4 = [
    ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"]]
room5 = [
    ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"]]
room6 = [
    ["/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "/"],
    ["/", "/", "/", "/", "/", 2, 1, "/", "/", "/", "/", "/"]]
room7 = [
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
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (1200, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, 1000))


class Player:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load(door), (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        global room_count, world
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            dx -= 5
        if keys[pygame.K_d]:
            dx += 5
        if keys[pygame.K_w]:
            dy -= 5
        if keys[pygame.K_s]:
            dy += 5
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            dx = 0
        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            dy = 0

        for tile in world.tile_list:

            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0

        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


class World:
    def __init__(self, data):
        self.tile_list = []

        darklog = pygame.image.load('img/grass.png')

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
                if tile == 3:
                    dooor = Door(col_count * 100, row_count * 100, "left")
                    door_left_group.add(dooor)
                if tile == "/":
                    img = pygame.transform.scale(darklog, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == "§":
                    locke = Locker(col_count * 100, row_count * 100)
                    locker_group.add(locke)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        if direction == "left":
            img = pygame.image.load(door)
            self.image = pygame.transform.scale(img, (100, 100))
        if direction == "right":
            img = pygame.image.load("img/Doorleft.png")
            self.image = pygame.transform.scale(img, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Locker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("img/lockr.png")
        self.image = pygame.transform.scale(img, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class start:
    def __init__(self):
        self.a = False

    def Start(self, rang):
        if not self.a:
            pos_x = 1920 / 2 - 540 / 2
            pos_y = 1080 - 540
            os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)
            os.environ['SDL_VIDEO_CENTERED'] = '0'
            screen = pygame.display.set_mode((540, 540))
            start_snd.play()

            for frame in range(rang):
                screen.fill((0, 0, 0))
                a = pygame.image.load(f"frames/start/ezgif-frame-0{frame}.jpg")
                pygame.transform.scale(a, (1200, 1000))
                screen.blit(a, (0, 0))
                pygame.display.flip()
                pygame.time.delay(40)

            self.a = True


class termux:
    def __init__(self):
        self.a = False

    def Terminal(self, rang):
        if not self.a:
            pos_x = 1920 / 2 - 1200 / 2
            pos_y = 1080 - 1000
            os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)
            os.environ['SDL_VIDEO_CENTERED'] = '0'
            screen = pygame.display.set_mode((1200, 1000))

            for frame in range(rang):
                screen.fill((0, 0, 0))
                a = pygame.image.load(f"frames/termux/ezgif-frame-0{frame}.jpg")
                screen.blit(a, (0, 0))
                pygame.display.flip()
                pygame.time.delay(40)

            self.a = True


door_group = pygame.sprite.Group()
door_left_group = pygame.sprite.Group()
locker_group = pygame.sprite.Group()

world = World(room)
player = Player(580, 800)

st = start()
tmx = termux()

guard = False

stage = "termux"
i = 0
run = True
while True:
    if guard:
        if i == 0:
            walk.set_volume(0)
            walk.play()
        i += 1
        walk.set_volume(walk.get_volume() + 0.0079)
        print(walk.get_volume())
        if i == 180:
            if stage != "locker":
                stage = "found"
                guard = False
            else:
                guard = False
                i = 0

    if not guard:
        walk.set_volume(0)

    if stage == "termux":
        tmx.Terminal(100)
        stage = "start"

    if stage == "start":
        st.Start(46)
        pos_x = 1920 / 2 - 540 / 2
        pos_y = 1080 - 540
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)
        os.environ['SDL_VIDEO_CENTERED'] = '0'
        screen = pygame.display.set_mode((1200, 1000))
        stage = "room"

    if stage == "room":
        screen.fill((0, 0, 0))
        world.draw()
        player.update()
        door_group.draw(screen)
        door_left_group.draw(screen)
        locker_group.draw(screen)

        draw_grid()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and pygame.sprite.spritecollide(player, locker_group, False):
                print("Lock")
                stage = "locker"
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_g:
                guard = True

        if pygame.sprite.spritecollide(player, locker_group, False):
            Enter_Locker = dos.render("Press space to enter the locker.", True, (175, 175, 175))
            screen.blit(Enter_Locker, (125, 800))

        if pygame.sprite.spritecollide(player, door_group, False):
            if level != 0 and level != 1:
                guard_go = randint(1, 6)
                if guard_go == 1:
                    print("hide")
                    guard = True
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
            elif level == 4:
                world = World(room4)
            elif level == 5:
                world = World(room5)
            elif level == 6:
                world = World(room6)
            elif level == 7:
                world = World(room7)

            print(level)
        elif pygame.sprite.spritecollide(player, door_left_group, False):
            level += 1
            door_group.empty()
            door_left_group.empty()
            locker_group.empty()
            player.rect.x = 1100 - player.rect.width
            player.rect.y = 800
            if level == 1:
                world = World(room1)
            elif level == 2:
                world = World(room2)
            elif level == 3:
                world = World(room3)
            elif level == 4:
                world = World(room4)
            elif level == 5:
                world = World(room5)
            elif level == 6:
                world = World(room6)
            elif level == 7:
                world = World(room7)

    elif stage == "locker":
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                stage = "room"

        screen.blit(locker, (0, 0))

    clock.tick(60)
    pygame.display.update()
