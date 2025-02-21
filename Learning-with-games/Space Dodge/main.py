import pygame
import time
import random


# general setup
pygame.font.init()

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE, BG_IMAGE_PATH = 1200, 800, "Space Dodge", "bg.jpg"

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption(GAME_TITLE)

BG = pygame.transform.scale(pygame.image.load(
    BG_IMAGE_PATH), (WINDOW_WIDTH, WINDOW_HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VELOCITY = 40, 60, 10

STAR_WIDTH, STAR_HEIGHT, STAR_VEL = 10, 20, 3

FPS = 60

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time, stars):

    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")

    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)
    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()


def main():

    run: bool = True

    player_x_position = random.randint(0, WINDOW_WIDTH - PLAYER_WIDTH)

    player_y_position = WINDOW_HEIGHT - PLAYER_HEIGHT

    player = pygame.Rect(player_x_position, player_y_position,
                         PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    start_time = time.time()

    elapsed_time = 0

    star_add_increment = 2000

    star_count = 0

    stars = []

    hit = False

    while (run):

        # slows the fps to given frames per second
        clock.tick(FPS)

        elapsed_time = time.time() - start_time

        star_count += clock.tick(60)

        if (star_count > star_add_increment):
            for _ in range(random.randint(3, 15)):

                star_x = random.randint(0, WINDOW_WIDTH - STAR_WIDTH)

                star_y = random.randint(-STAR_HEIGHT *
                                        random.randint(1, STAR_HEIGHT), -STAR_HEIGHT)

                star = pygame.Rect(star_x, star_y,
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(100, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False
                break

        # MOVING BASED ON KEYS

        # keys = pygame.key.get_pressed()

        # if (keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0):
        #     player.x -= PLAYER_VELOCITY

        # if (keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WINDOW_WIDTH):
        #     player.x += PLAYER_VELOCITY

        X, _ = pygame.mouse.get_pos()
        # player.x is the top left corner of the rect.

        if (X <= player.x):
            player.x = X

        if (X > player.x):
            player.x = X-PLAYER_WIDTH

        for star in stars[:]:
            star.y += STAR_VEL
            if (star.y > WINDOW_HEIGHT):
                stars.remove(star)
            elif (star.y + star.height >= player.y and star.colliderect(player)):
                stars.remove(star)
                hit = True
                break

        if (hit):
            lost_text = FONT.render("You lost!", 1, "white")
            WIN.blit(lost_text, (WINDOW_WIDTH / 2 - lost_text.get_width() /
                     2, WINDOW_HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
