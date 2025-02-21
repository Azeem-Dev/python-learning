import os
from typing import Tuple
import pygame
import random


def pygame_constants() -> Tuple[int,
                                int,
                                int,
                                pygame.Surface,
                                pygame.Font,
                                pygame.Surface,
                                pygame.Clock,
                                pygame.Surface,
                                pygame.Surface,
                                pygame.Surface,
                                pygame.Surface,
                                pygame.Surface,
                                pygame.Surface,
                                pygame.Surface,
                                pygame.Surface,
                                pygame.Font,
                                int]:

    (
        WINDOWS_WIDTH,
        WINDOWS_HEIGHT,
        FPS,
        WIN,
        GAME_FONT,
        BG,
        CLOCK
    ) = __get_windows_constants()

    (
        RED_SPACESHIP,
        GREEN_SPACESHIP,
        BLUE_SPACESHIP,
        RED_SPACESHIP_LASER,
        GREEN_SPACESHIP_LASER,
        BLUE_SPACESHIP_LASER,
    ) = __get_enemy_constants()

    (
        YELLOW_SPACESHIP,
        YELLOW_SPACESHIP_LASER,
        PLAYER_FONT,
        PLAYER_VEL
    ) = __get_player_constants()

    return (
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
    )


def __get_windows_constants() -> Tuple[int, int, int, pygame.Surface, pygame.Font, pygame.Surface, pygame.Clock]:

    WINDOWS_WIDTH, WINDOWS_HEIGHT, GAME_TITLE, GAME_FONT_NAME, GAME_FONT_SIZE = 1200, 800, "Space Shooter(v1)", "comicsans", 100
    FPS = 60

    WIN = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    GAME_FONT = pygame.font.SysFont(GAME_FONT_NAME, GAME_FONT_SIZE)

    # BACKGROUND
    BG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "Space Shooter(v1)",
                                                               "assets", "background-black.png")), (WINDOWS_WIDTH, WINDOWS_HEIGHT))

    CLOCK = pygame.time.Clock()
    return (
        WINDOWS_WIDTH,
        WINDOWS_HEIGHT,
        FPS,
        WIN,
        GAME_FONT,
        BG,
        CLOCK
    )


def __get_enemy_constants() -> Tuple[pygame.Surface, pygame.Surface, pygame.Surface, pygame.Surface, pygame.Surface, pygame.Surface]:
    ENEMY_SPACESHIP_WIDTH, ENEMY_SPACESHIP_HEIGHT = 60, 60
    LASER_WIDTH, LASER_HEIGHT = 50, 70

    RED_SPACESHIP_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_ship_red_small.png")
    GREEN_SPACESHIP_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_ship_green_small.png")
    BLUE_SPACESHIP_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_ship_blue_small.png")

    RED_LASER_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_laser_red.png")
    GREEN_LASER_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_laser_green.png")
    BLUE_LASER_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_laser_blue.png")

    # enemy spaceship
    RED_SPACESHIP = pygame.transform.scale(pygame.image.load(
        RED_SPACESHIP_PATH), (ENEMY_SPACESHIP_WIDTH, ENEMY_SPACESHIP_HEIGHT))
    GREEN_SPACESHIP = pygame.transform.scale(pygame.image.load(
        GREEN_SPACESHIP_PATH), (ENEMY_SPACESHIP_WIDTH, ENEMY_SPACESHIP_HEIGHT))
    BLUE_SPACESHIP = pygame.transform.scale(pygame.image.load(
        BLUE_SPACESHIP_PATH), (ENEMY_SPACESHIP_WIDTH, ENEMY_SPACESHIP_HEIGHT))

    # enemy spaceship laser
    RED_SPACESHIP_LASER = pygame.transform.scale(pygame.image.load(
        RED_LASER_PATH), (LASER_WIDTH, LASER_HEIGHT))
    GREEN_SPACESHIP_LASER = pygame.transform.scale(pygame.image.load(
        GREEN_LASER_PATH), (LASER_WIDTH, LASER_HEIGHT))
    BLUE_SPACESHIP_LASER = pygame.transform.scale(pygame.image.load(
        BLUE_LASER_PATH), (LASER_WIDTH, LASER_HEIGHT))
    return (
        RED_SPACESHIP,
        GREEN_SPACESHIP,
        BLUE_SPACESHIP,
        RED_SPACESHIP_LASER,
        GREEN_SPACESHIP_LASER,
        BLUE_SPACESHIP_LASER,
    )


def __get_player_constants() -> Tuple[pygame.Surface, pygame.Surface, pygame.Font, int]:
    PLAYER_SPACESHIP_WIDTH, PLAYER_SPACESHIP_HEIGHT, PLAYER_FONT_NAME, PLAYER_FONT_SIZE = 100, 100, "comicsans", 34
    LASER_WIDTH, LASER_HEIGHT = 70, 80

    YELLOW_SPACESHIP_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_ship_yellow.png")

    YELLOW_LASER_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_laser_yellow.png")

    YELLOW_SPACESHIP = pygame.transform.scale(pygame.image.load(
        YELLOW_SPACESHIP_PATH), (PLAYER_SPACESHIP_WIDTH, PLAYER_SPACESHIP_HEIGHT))

    YELLOW_SPACESHIP_LASER = pygame.transform.scale(pygame.image.load(
        YELLOW_LASER_PATH), (LASER_WIDTH, LASER_HEIGHT))
    PLAYER_FONT = pygame.font.SysFont(PLAYER_FONT_NAME, PLAYER_FONT_SIZE)

    PLAYER_VEL = 5

    return (
        YELLOW_SPACESHIP,
        YELLOW_SPACESHIP_LASER,
        PLAYER_FONT,
        PLAYER_VEL
    )


def get_randomsize_enemyships() -> Tuple:
    RED_SPACESHIP_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_ship_red_small.png")
    GREEN_SPACESHIP_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_ship_green_small.png")
    BLUE_SPACESHIP_PATH = os.path.join(
        os.getcwd(), "Space Shooter(v1)", "assets", "pixel_ship_blue_small.png")

    MIN = 40
    MAX = 60
    random_width_height = random.randint(MIN, MAX)

    RED_SPACESHIP = pygame.transform.scale(pygame.image.load(
        RED_SPACESHIP_PATH), (random_width_height, random_width_height))

    random_width_height = random.randint(MIN, MAX)

    GREEN_SPACESHIP = pygame.transform.scale(pygame.image.load(
        GREEN_SPACESHIP_PATH), (random_width_height, random_width_height))

    random_width_height = random.randint(MIN, MAX)

    BLUE_SPACESHIP = pygame.transform.scale(pygame.image.load(
        BLUE_SPACESHIP_PATH), (random_width_height, random_width_height))

    return (
        RED_SPACESHIP,
        GREEN_SPACESHIP,
        BLUE_SPACESHIP
    )
