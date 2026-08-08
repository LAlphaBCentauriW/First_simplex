import opensimplex
import numpy as np
import pygame


pygame.init()

window = pygame.display.set_mode((1000, 1000))

# Cell parameters
width, height = 10, 10 # Defines width and height of each cell in the grid

scale = 0.5 # Defines the scale of the noise function, affecting the frequency of the noise pattern



opensimplex.random_seed() # Generates a random seed for the noise function

xs = np.arange(0, 1000, width*scale) # Creates an array of x-coordinates for the grid cells
ys = np.arange(0, 1000, height*scale) # Creates an array of y-coordinates for the grid cells

print(xs)


grid= opensimplex.noise2array(xs, ys) # Generates a 2D array of noise values for the grid cells using the OpenSimplex noise function


def color(value):
    # Maps the noise value to a color
    if value < -0.5:
        return (0, 0, 128) # Dark blue for low values
    elif value < 0:
        return (0, 0, 255) # Blue for medium-low values
    elif value < 0.5:
        return (0, 255, 255) # Cyan for medium-high values
    else:
        return (255, 255, 255) # White for high values


def draw_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(window, color(grid[i][j]), (j * width, i * height, width, height))
            
    pygame.display.update() # Updates the display after drawing each row of cells




draw_grid()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()





