"""
DISPLAY SURFACE:

Is the main window on the screen on which we will draw other surfaces.
There can only be 1 surface.


SHOWING GRAPHICS HAS 2 WAYS

1- Show an image or text via a surface
2- Drawing the pixels


SURFACE:
in pygame is usually an image, a plane area or rendered text

How to create a SURFACE?

plain surface: pygame.Surface((width,height))
imported surface: pygame.image.load(path)
text surface: font.render(text, AntiAlias, Color)


"""

import pygame

# general setup
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE = 1200, 720, "Space Shooter"

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption(GAME_TITLE)  # sets the window title

running = True

# surface

surf = pygame.Surface((100, 200))

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game

    # fill the window with a red color
    display_surface.fill('darkgray')
    display_surface.blit(surf, (100, 150))
    # update()/flip() here flip rerenders part of the game while update updates the whole window causing a rerender
    pygame.display.update()


pygame.quit()
