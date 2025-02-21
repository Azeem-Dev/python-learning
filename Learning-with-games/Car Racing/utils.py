import pygame


def scale_image(img: pygame.Surface, factor: float):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win: pygame.Surface, image: pygame.Surface, top_left: tuple[float, float], angle: float):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win: pygame.Surface, font: pygame.Font, text: str):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width() / 2 - render.get_width() /
             2, win.get_height() / 2 - render.get_height() / 2))
