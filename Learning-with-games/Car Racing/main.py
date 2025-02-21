import pygame
import time
import math
import os
from utils import scale_image, blit_rotate_center, blit_text_center


GAME_TITLE, GAME_FONT_NAME, GAME_FONT_SIZE = "Car Racing", "comicsans", 100
FPS = 60

GAME_ASSETS_DIR_PATH = os.path.join(os.getcwd(), GAME_TITLE, "imgs")

TRACK = scale_image(pygame.image.load(
    os.path.join(GAME_ASSETS_DIR_PATH, "track.png")), 0.9)

GAME_WIDTH, GAME_HEIGHT = TRACK.get_width(), TRACK.get_height()

TRACK_BORDER = scale_image(pygame.image.load(os.path.join(
    GAME_ASSETS_DIR_PATH, "track-border.png")), 0.9)

TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

FINISH = pygame.image.load(os.path.join(GAME_ASSETS_DIR_PATH, "finish.png"))
FINISH_MASK = pygame.mask.from_surface(FINISH)

FINISH_POSITION = (130, 250)

RED_CAR = scale_image(pygame.image.load(
    os.path.join(GAME_ASSETS_DIR_PATH, "red-car.png")), 0.55)
GREEN_CAR = scale_image(pygame.image.load(os.path.join(
    GAME_ASSETS_DIR_PATH, "green-car.png")), 0.55)
GRASS = scale_image(pygame.image.load(os.path.join(
    GAME_ASSETS_DIR_PATH, "grass.jpg")), 2)


WIN = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

FPS = 60

ENEMY_PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
              (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]


class Stage:

    LEVELS = 10

    def __init__(self, stage_images: list[(pygame.Surface), (int, int)], level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0
        self.stage_images = stage_images

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return 0
        else:
            return round(time.time() - self.level_start_time, 0)

    def draw(self, win: pygame.Surface):
        for stage_img, pos in self.stage_images:
            win.blit(stage_img, pos)


class Car:
    START_POS = (180, 200)

    def __init__(self, x, y, max_velocity, rotation_velocity, velocity=0, angle=0, img: pygame.Surface = None):
        self.x, self.y, self.max_velocity, self.rotation_velocity, self.velocity, self.angle, self.img, self.acceleration = x, y, max_velocity, rotation_velocity, velocity, angle, img, 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_velocity
        elif right:
            self.angle -= self.rotation_velocity

    def draw(self, win: pygame.Surface):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.velocity = min(
            self.velocity + self.acceleration, self.max_velocity)
        self.move()

    def move_backward(self):
        self.velocity = max(
            self.velocity - self.acceleration, - self.max_velocity / 2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.velocity
        horizontal = math.sin(radians) * self.velocity
        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask: pygame.Mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        # point of intersection
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.velocity = 0


class PlayerCar(Car):
    def __init__(self, x, y, max_velocity, rotation_velocity, velocity=0, angle=0, img=None):
        super().__init__(x, y, max_velocity, rotation_velocity, velocity, angle, img)

    def reduce_speed(self):
        self.velocity = max(self.velocity - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.velocity = -self.velocity
        self.move()


class EnemyCar(Car):

    START_POS = (150, 200)

    def __init__(self, x, y, max_velocity, rotation_velocity, velocity=0, angle=0, img=None, path=[]):
        super().__init__(x, y, max_velocity, rotation_velocity, velocity, angle, img)
        self.path = path
        self.current_point = 0
        self.velocity = max_velocity

    def draw_points(self, win: pygame.Surface):
        for point in self.path:
            pygame.draw.circle(win, (255, 0, 0), point, 5)

    def draw(self, win: pygame.Surface):
        super().draw(win)
        # self.draw_points(win)

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff/y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)

        if (difference_in_angle >= 180):
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_velocity, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_velocity, abs(difference_in_angle))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(
            self.x, self.y, self.img.get_width(), self.img.get_height())
        target_rect = pygame.Rect(*target, 10, 10)
        if rect.colliderect(target_rect):
            self.current_point += 1

    def move(self):
        if self.current_point >= len(self.path):
            return

        self.calculate_angle()
        self.update_path_point()

        super().move()

    def reset(self):
        super().reset()
        self.current_point = 0

    def next_level(self, level):
        self.reset()
        self.velocity = self.max_velocity + (level - 1) * 0.2


def draw(win: pygame.Surface, stage: Stage, player_car: PlayerCar, enemy_car: EnemyCar):

    stage.draw(win)

    level_text = GAME_FONT.render(f"Level {stage.level}", 1, "white")

    win.blit(level_text, (10, GAME_HEIGHT - level_text.get_height() - 70))

    time_text = GAME_FONT.render(
        f"Time: {stage.get_level_time()}s", 1, "white")

    win.blit(time_text, (10, GAME_HEIGHT - time_text.get_height() - 40))

    player_text = GAME_FONT.render(
        f"Vel: {round(player_car.velocity, 1)}px/s", 1, "white")

    win.blit(player_text, (10, GAME_HEIGHT - player_text.get_height() - 10))

    player_car.draw(win)
    enemy_car.draw(win)

    move_player(player_car)
    enemy_car.move()

    handle_collision(player_car, enemy_car, stage)

    if stage.game_finished():
        blit_text_center(win, GAME_FONT, f'You won! :)')
        pygame.display.update()
        pygame.time.wait(5000)
        stage.reset()
        player_car.reset()
        enemy_car.reset()

    pygame.display.update()


def move_player(player_car: PlayerCar):
    keys = pygame.key.get_pressed()
    moved = False

    if (keys[pygame.K_UP] or keys[pygame.K_w]):
        moved = True
        player_car.move_forward()
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
        moved = True
        player_car.move_backward()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        player_car.rotate(left=True)
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        player_car.rotate(right=True)

    if not moved:
        player_car.reduce_speed()


def handle_collision(player_car: PlayerCar, enemy_car: EnemyCar, stage: Stage):
    if player_car.collide(TRACK_BORDER_MASK) != None:
        player_car.bounce()

    enemy_finish_poi_collide = enemy_car.collide(FINISH_MASK, *FINISH_POSITION)

    if enemy_finish_poi_collide != None:
        blit_text_center(WIN, GAME_FONT, f'You lost!')
        pygame.time.wait(5000)
        stage.reset()
        player_car.reset()
        enemy_car.reset()

    player_finish_poi_collide = player_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            stage.next_level()
            player_car.reset()
            enemy_car.next_level(stage.level)


pygame.init()
pygame.font.init()
pygame.mixer.init()

CLOCK = pygame.time.Clock()

GAME_FONT = pygame.font.SysFont("comicsans", 36)


def game_level_start_draw(win: pygame.Surface, stage: Stage, player_car: PlayerCar, enemy_car: EnemyCar):

    stage.draw(win)

    player_car.draw(win)
    enemy_car.draw(win)

    while not stage.started:
        blit_text_center(
            WIN, GAME_FONT, f'Press any key to start level {stage.level}!')

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                stage.start_level()


def main():

    running = True
    stage = Stage([(GRASS, (0, 0)), (TRACK, (0, 0)),
                  (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))])

    player_car = PlayerCar(180, 200, 4, 4, 0, img=RED_CAR)
    enemy_car = EnemyCar(150, 200, 2, 4, 0, img=GREEN_CAR, path=ENEMY_PATH)

    game_level_start_draw(WIN, stage, player_car, enemy_car)

    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pos = pygame.mouse.get_pos()
            #     enemy_car.path.append(pos)
        draw(WIN, stage, player_car, enemy_car)

    pygame.quit()


if (__name__ == "__main__"):
    main()
