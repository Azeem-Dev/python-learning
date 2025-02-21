import pygame
import os
import time
import random
from game_constants import pygame_constants, get_randomsize_enemyships
from typing import List, Literal

# general code
pygame.init()
pygame.font.init()
pygame.mixer.init()

(
    WINDOWS_WIDTH,
    WINDOWS_HEIGHT,
    FPS,
    WIN,
    GAME_FONT,
    RED_SPACESHIP,
    CLOCK,
    GREEN_SPACESHIP,
    BLUE_SPACESHIP,
    YELLOW_SPACESHIP,
    RED_SPACESHIP_LASER,
    GREEN_SPACESHIP_LASER,
    BLUE_SPACESHIP_LASER,
    YELLOW_SPACESHIP_LASER,
    BG,
    PLAYER_FONT,
    PLAYER_VEL
) = pygame_constants()


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window: pygame.Surface):
        window.blit(self.img, (self.x, self.y))

    def move(self, velocity):
        self.y += velocity

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Ship:

    COOLDOWN = 30

    def __init__(self, x: int, y: int, velocity: int, health: int = 100):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.health = health
        self.ship_img: pygame.Surface = None
        self.laser_img: pygame.Surface = None
        self.mask: pygame.Mask = None
        self.lasers: List[Laser] = []
        self.cool_down_counter = 0
        self.shoot_offset: int = 0

    def draw(self, window: pygame.Surface):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move(vel)
            if laser.off_screen(WINDOWS_HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def get_width(self) -> int:
        return self.ship_img.get_width()

    def get_height(self) -> int:
        return self.ship_img.get_height()

    def shoot(self):
        if (self.cool_down_counter == 0):
            laser = Laser(self.x + self.shoot_offset, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def cooldown(self):
        if (self.cool_down_counter >= self.COOLDOWN):
            self.cool_down_counter = 0
        elif (self.cool_down_counter > 0):
            self.cool_down_counter += 1


class PlayerShip(Ship):
    def __init__(self, x: int, y: int, velocity: int, health: int = 100):
        super().__init__(x, y, velocity, health)
        self.ship_img = YELLOW_SPACESHIP
        self.laser_img = YELLOW_SPACESHIP_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health: int = health

    def recalculate_movement_and_shooting(self, pygame: pygame):
        keys = pygame.key.get_pressed()

        if ((keys[pygame.K_UP] or keys[pygame.K_w]) and self.y - self.velocity >= 0):
            self.y -= self.velocity
        if ((keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y + self.velocity + self.get_height() + 20 <= WINDOWS_HEIGHT):
            self.y += self.velocity
        if ((keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x - self.velocity >= 0):
            self.x -= self.velocity
        if ((keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x + self.velocity + self.get_height() <= WINDOWS_WIDTH):
            self.x += self.velocity
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move(vel)
            if laser.off_screen(WINDOWS_HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs[:]:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window: pygame.Surface):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window: pygame.Surface):
        health_progress_damage = pygame.Rect(
            self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10)
        health_progress_remaining = pygame.Rect(
            self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10)

        pygame.draw.rect(window, (255, 0, 0), health_progress_damage)
        pygame.draw.rect(window, (0, 255, 0), health_progress_remaining)


class EnemyShip(Ship):

    COLOR_MAP = {
        "red": (RED_SPACESHIP, RED_SPACESHIP_LASER),
        "green": (GREEN_SPACESHIP, GREEN_SPACESHIP_LASER),
        "blue": (BLUE_SPACESHIP, BLUE_SPACESHIP_LASER)
    }

    def __init__(self, x: int, y: int, velocity: int, color: Literal["red", "green", "blue"], health: int = 100):
        super().__init__(x, y, velocity, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color.lower()]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self):
        self.y += self.velocity

    def should_remove_enemy(self) -> bool:
        return self.y + self.get_height() >= WINDOWS_HEIGHT


def collide(obj1: Laser | Ship, obj2: Laser | Ship):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():

    running = True
    level = 0
    lives = 5

    enemies: list[EnemyShip] = []
    wave_length = 5
    enemy_val = 1
    lost: bool = False
    lost_count = 0

    player_ship = PlayerShip(300, 650, PLAYER_VEL)
    player_ship.shoot_offset = 15

    def redraw_life_and_level_text():
        player_level_text = PLAYER_FONT.render(f"level : {level}", 1, "white")
        player_lives_text = PLAYER_FONT.render(f"lives : {lives}", 1, "white")

        WIN.blit(player_level_text, (10, 10))

        pygame.draw.line(WIN, "red", (10, 55), (130, 55), 2)

        WIN.blit(player_lives_text, (WINDOWS_WIDTH -
                 player_lives_text.width - 10, 10))

        pygame.draw.line(WIN, "red", (WINDOWS_WIDTH - 10, 55),
                         (WINDOWS_WIDTH - player_lives_text.width - 10, 55), 2)

    def redraw_window():

        WIN.blit(BG, (0, 0))

        redraw_life_and_level_text()

        for enemy in enemies:
            enemy.draw(WIN)

        player_ship.recalculate_movement_and_shooting(pygame)
        player_ship.draw(WIN)

        if (lost):
            lost_text = GAME_FONT.render(f"YOU LOST :D", 1, "white")
            WIN.blit(lost_text, (WINDOWS_WIDTH // 2 -
                     lost_text.width // 2, WINDOWS_HEIGHT // 2))

        pygame.display.update()

    while running:
        CLOCK.tick(FPS)

        redraw_window()

        if (lives <= 0 or player_ship.health <= 0):
            lost = True
            lost_count += 1

        if (lost):
            if lost_count > FPS * 3:
                running = False
            else:
                continue

        if (len(enemies) == 0):
            level += 1
            for _ in range(wave_length):
                enemy = EnemyShip(random.randrange(100, WINDOWS_WIDTH - 100), random.randrange(
                    -WINDOWS_HEIGHT, - 50), level * 2, random.choice(["red", "blue", "green"]), 100)
                enemy.shoot_offset = 5
                enemies.append(enemy)
            wave_length += 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        for enemy in enemies[:]:
            enemy.move()
            enemy.move_lasers(10, player_ship)

            if (random.randrange(0, 2//level*60)) == 1:
                enemy.shoot()

            if (collide(player_ship, enemy)):
                player_ship.health -= 10
                enemies.remove(enemy)

            elif (enemy.should_remove_enemy()):
                enemies.remove(enemy)
                lives -= 1

        player_ship.move_lasers(-(10), enemies)

    


def main_menu():
    running = True
    title_font = GAME_FONT.render("Press mousekey to start", 1, "white")

    while running:
      
        WIN.blit(BG, (0, 0))

        WIN.blit(title_font, (WINDOWS_WIDTH//2 -
                 title_font.get_width() // 2, WINDOWS_HEIGHT//2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()


if (__name__ == "__main__"):
    main_menu()
