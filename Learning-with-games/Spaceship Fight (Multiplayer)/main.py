import pygame
import random

# constant values
WINDOWS_WIDTH, WINDOWS_HEIGHT, GAME_TITLE, GAME_FONT = 1200, 800, "Spaceship Fight (Multiplayer)", "comicsans"
BG_IMAGE_PATH = "./Assets/space.png"
BULLET_SOUND_PATH = "./Assets/Gun+Silencer.mp3"
HIT_SOUND_PATH = "./Assets/Grenade+1.mp3"
BG_SOUND_PATH = "./Assets/vinland_saga.mp3"


SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 80, 80
SPACESHIP_YELLOW_IMAGE_PATH = "./Assets/spaceship_yellow.png"
SPACESHIP_RED_IMAGE_PATH = "./Assets/spaceship_red.png"
SPACESHIP_VELOCITY = 5

BULLET_WIDTH, BULLET_HEIGHT = 20, 7
BULLET_VELOCITY = 7
BULLET_COOLDOWN_TIME = 10

# general code
pygame.init()
pygame.font.init()
pygame.mixer.init()

FONT = pygame.font.SysFont(GAME_FONT, 30)

WIN = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
FPS = 60

pygame.display.set_caption(GAME_TITLE)

BG_IMAGE = pygame.image.load(BG_IMAGE_PATH)
BG = pygame.transform.scale(BG_IMAGE, (WINDOWS_WIDTH, WINDOWS_HEIGHT))

TRANSPARENT_LAYER = pygame.Surface(
    (WINDOWS_WIDTH, WINDOWS_HEIGHT), pygame.SRCALPHA)
TRANSPARENT_LAYER.fill((0, 0, 0, 128))

SPACESHIP_YELLOW_IMAGE = pygame.image.load(SPACESHIP_YELLOW_IMAGE_PATH)
SPACESHIP_YELLOW = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP_YELLOW_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

SPACESHIP_RED_IMAGE = pygame.image.load(SPACESHIP_RED_IMAGE_PATH)
SPACESHIP_RED = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP_RED_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

SPACESHIP_HEALTH = 5

SPACEHIP_RED_START_RANDOM_POSITION = random.randint(
    100, WINDOWS_HEIGHT - SPACESHIP_HEIGHT)
SPACEHIP_YELLOW_START_RANDOM_POSITION = random.randint(
    100, WINDOWS_HEIGHT - SPACESHIP_HEIGHT)

damage_to_spaceship_red = 0
damage_to_spaceship_yellow = 0

clock = pygame.time.Clock()


bulletsRed = []
bulletsYellow = []

BULLET_FIRE_SOUND = pygame.mixer.Sound(BULLET_SOUND_PATH)
BULLET_FIRE_SOUND.set_volume(0.1)
HIT_SOUND = pygame.mixer.Sound(HIT_SOUND_PATH)
HIT_SOUND.set_volume(0.1)
BG_SOUND = pygame.mixer.Sound(BG_SOUND_PATH)
BG_SOUND.set_volume(0.05)


def draw(bullets, spaceship_yellow_y_position, spaceship_yellow_x_position, spaceship_red_y_position, spaceship_red_x_position, yellowLife, redLife, divider) -> None:

    WIN.blit(BG, (0, 0))
    WIN.blit(TRANSPARENT_LAYER, (0, 0))

    yello_life_text = FONT.render(f"lives : {yellowLife}", 1, "white")
    red_life_text = FONT.render(f"lives: {redLife}", 1, "white")

    for bullet in bullets:
        pygame.draw.rect(WIN, "red", bullet, border_radius=7)

    WIN.blit(red_life_text, (10, 10))
    WIN.blit(yello_life_text, (WINDOWS_WIDTH - yello_life_text.width - 10, 10))

    WIN.blit(SPACESHIP_RED, (spaceship_red_x_position, spaceship_red_y_position))
    WIN.blit(SPACESHIP_YELLOW, (spaceship_yellow_x_position,
             spaceship_yellow_y_position))

    pygame.draw.rect(WIN, "white", divider)
    
    pygame.display.update()
    return


def main() -> None:

    BG_SOUND.play(-1)

    running: bool = True

    spaceship_yellow_y_position = SPACEHIP_YELLOW_START_RANDOM_POSITION
    spaceship_yellow_x_position = WINDOWS_WIDTH - SPACESHIP_WIDTH

    spaceship_red_y_position = SPACEHIP_RED_START_RANDOM_POSITION
    spaceship_red_x_position = 0

    yellow_bullet_cooldown = 0
    red_bullet_cooldown = 0

    yellow_life = SPACESHIP_HEALTH
    red_life = SPACESHIP_HEALTH

    divider = pygame.Rect(WINDOWS_WIDTH // 2 - 5, 200, 10, WINDOWS_HEIGHT //2)

    while running:

        clock.tick(FPS)

        if (yellow_bullet_cooldown > 0):
            yellow_bullet_cooldown -= 1
        if (red_bullet_cooldown > 0):
            red_bullet_cooldown -= 1

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
                break

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] and spaceship_yellow_y_position - SPACESHIP_VELOCITY >= 0):
            spaceship_yellow_y_position -= SPACESHIP_VELOCITY

        if (keys[pygame.K_DOWN] and spaceship_yellow_y_position + SPACESHIP_HEIGHT + SPACESHIP_VELOCITY <= WINDOWS_HEIGHT):
            spaceship_yellow_y_position += SPACESHIP_VELOCITY

        if (keys[pygame.K_LEFT] and spaceship_yellow_x_position - SPACESHIP_VELOCITY >= (WINDOWS_WIDTH / 2)):
            spaceship_yellow_x_position -= SPACESHIP_VELOCITY

        if (keys[pygame.K_RIGHT] and spaceship_yellow_x_position + SPACESHIP_HEIGHT + SPACESHIP_VELOCITY <= WINDOWS_WIDTH):
            spaceship_yellow_x_position += SPACESHIP_VELOCITY

        if (keys[pygame.K_w] and spaceship_red_y_position - SPACESHIP_VELOCITY >= 0):
            spaceship_red_y_position -= SPACESHIP_VELOCITY

        if (keys[pygame.K_s] and spaceship_red_y_position + SPACESHIP_HEIGHT + SPACESHIP_VELOCITY <= WINDOWS_HEIGHT):
            spaceship_red_y_position += SPACESHIP_VELOCITY

        if (keys[pygame.K_a] and spaceship_red_x_position - SPACESHIP_VELOCITY >= 0):
            spaceship_red_x_position -= SPACESHIP_VELOCITY

        if (keys[pygame.K_d] and spaceship_red_x_position + SPACESHIP_HEIGHT + SPACESHIP_VELOCITY <= WINDOWS_WIDTH/2):
            spaceship_red_x_position += SPACESHIP_VELOCITY

        if (keys[pygame.K_LCTRL]):
            if (red_bullet_cooldown == 0):
                bullet = pygame.Rect(spaceship_red_x_position + SPACESHIP_WIDTH, spaceship_red_y_position +
                                     (SPACESHIP_HEIGHT - 5) / 2, BULLET_WIDTH, BULLET_HEIGHT)
                bulletsRed.append(bullet)
                red_bullet_cooldown += BULLET_COOLDOWN_TIME
                BULLET_FIRE_SOUND.play()

        if (keys[pygame.K_RCTRL]):
            if (yellow_bullet_cooldown == 0):
                bullet = pygame.Rect(spaceship_yellow_x_position - 20,
                                     spaceship_yellow_y_position + (SPACESHIP_HEIGHT - 5) / 2, BULLET_WIDTH, BULLET_HEIGHT)
                bulletsYellow.append(bullet)
                yellow_bullet_cooldown += BULLET_COOLDOWN_TIME
                BULLET_FIRE_SOUND.play()

        if (len(bulletsRed) > 0):
            for bullet in bulletsRed[:]:
                if (bullet.x + bullet.width + BULLET_VELOCITY >= WINDOWS_WIDTH):
                    bulletsRed.remove(bullet)
                    continue
                yellow_rect = pygame.Rect(
                    spaceship_yellow_x_position, spaceship_yellow_y_position, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
                if (bullet.colliderect(yellow_rect)):
                    yellow_life -= 1
                    bulletsRed.remove(bullet)
                    HIT_SOUND.play()
                    if (yellow_life <= 0):
                        winning_text_render = FONT.render(
                            "Red Wins", 1, "white")
                        WIN.blit(winning_text_render,
                                 (WINDOWS_WIDTH/2 - winning_text_render.width / 2, WINDOWS_HEIGHT/2 - winning_text_render.height/2))
                        pygame.display.update()
                        pygame.time.delay(4000)
                        running = False
                bullet.x += BULLET_VELOCITY

        if (len(bulletsYellow) > 0):
            for bullet in bulletsYellow[:]:
                if (bullet.x + bullet.width - BULLET_VELOCITY <= 0):
                    bulletsYellow.remove(bullet)
                    continue
                red_rect = pygame.Rect(
                    spaceship_red_x_position, spaceship_red_y_position, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
                if (bullet.colliderect(red_rect)):
                    red_life -= 1
                    bulletsYellow.remove(bullet)
                    HIT_SOUND.play()
                    if (red_life <= 0):
                        winning_text_render = FONT.render(
                            "Yellow Wins", 1, "white")
                        WIN.blit(winning_text_render,
                                 (WINDOWS_WIDTH/2 - winning_text_render.width/2, WINDOWS_HEIGHT/2 - winning_text_render.height/2))
                        pygame.display.update()
                        pygame.time.delay(4000)
                        running = False
                bullet.x -= BULLET_VELOCITY
        bullets = [*bulletsRed, *bulletsYellow]

        draw(bullets, spaceship_yellow_y_position, spaceship_yellow_x_position,
             spaceship_red_y_position, spaceship_red_x_position, yellow_life, red_life, divider)

    pygame.quit()

    return


if (__name__ == "__main__"):
    main()
