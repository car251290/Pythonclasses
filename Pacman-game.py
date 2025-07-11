import pygame
import numpy as np


def load_image(file):
    filename = file + '.png'
    try:
        image = pygame.image.load(filename).convert()
    except pygame.error:
        error_message = 'Could not load the image {0}.\n{1}'.\
            format(filename, pygame.get_error())
        pygame.quit()
        raise SystemExit(error_message)

    return image


def verify_8x8_image(image):
    # Calculate the size of the image
    width, height = image.get_rect().size
    NFIL, NCOL = height / 8, width / 8  # rows, columns

    if NFIL != int(NFIL) or NCOL != int(NCOL):
        raise('The size of the image is not divisible by 8')

    return int(NFIL), int(NCOL)


# Initialize PYGAME mode
pygame.init()

# Initialize the game window
window = pygame.display.set_mode((1280, 800))  # , FULLSCREEN)

# Load images from disk and store them in a dictionary
maze = load_image('laberinto')
NFIL, NCOL = verify_8x8_image(maze)

small_pepa = load_image('pepa_peq')
large_pepa = load_image('pepa_gra')
fan_wall = load_image('muro_fan')
empty = load_image('vacio')

surfarray_small_pepa = pygame.surfarray.array2d(small_pepa)
surfarray_large_pepa = pygame.surfarray.array2d(large_pepa)
surfarray_fan_wall = pygame.surfarray.array2d(fan_wall)
surfarray_empty = pygame.surfarray.array2d(empty)

map_grid = [['#' for c in range(NCOL)] for f in range(NFIL)]

scale = 3
width, height = 8, 8
for f in range(NFIL):
    for c in range(NCOL):
        # Extract the 8x8 image from the larger image
        block_8x8 = pygame.Surface((width, height)).convert()
        block_8x8.blit(maze, (0, 0), (width * c, height * f, width, height))

        surfarray_block_8x8 = pygame.surfarray.array2d(block_8x8)

        if np.array_equal(surfarray_small_pepa, surfarray_block_8x8):
            map_grid[f][c] = '.'
        elif np.array_equal(surfarray_large_pepa, surfarray_block_8x8):
            map_grid[f][c] = 'o'
        elif np.array_equal(surfarray_fan_wall, surfarray_block_8x8):
            map_grid[f][c] = 'M'
        elif np.array_equal(surfarray_empty, surfarray_block_8x8):
            map_grid[f][c] = ' '

        print(surfarray_block_8x8)
        print('')

        scaled_block_8x8 = pygame.transform.scale(block_8x8, (scale * width, scale * height))

        # Display the image
        window.blit(scaled_block_8x8, (c * 3 * 8, f * 3 * 8))
        pygame.display.update()

print('NFIL =', NFIL, '   NCOL =', NCOL)
for i in range(NFIL):
    print('"' + ''.join(map_grid[i]) + '",')

pygame.quit()  # Exit PYGAME mode