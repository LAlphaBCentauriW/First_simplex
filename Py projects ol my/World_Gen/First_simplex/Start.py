import opensimplex
import numpy as np
import pygame


pygame.init()

window = pygame.display.set_mode((1000, 1000))

# Cell parameters
width, height = 10, 10  # Defines width and height of each cell in the grid

scale = 0.1 # Defines the scale of the noise function, affecting the frequency of the noise pattern



opensimplex.random_seed() # Generates a random seed for the noise function

xs = np.arange(0, 100) # Creates an array of x-coordinates for the grid cells
ys = np.arange(0, 100) # Creates an array of y-coordinates for the grid cells

print("before scaling: ", xs, ys)

xs = xs * scale # Scales the x-coordinates by the defined scale factor
ys = ys * scale # Scales the y-coordinates by the defined scale factor

print("after scaling: ", xs, ys)
print("xs.shape:", xs.shape, "xs length", len(xs))
print("ys.shape:", ys.shape, "ys length", len(ys))


grid= opensimplex.noise2array(xs, ys) # Generates a 2D array of noise values for the grid cells using the OpenSimplex noise function

print ("grid length: ", len(grid))
print ("grid: ", grid)
print("grid min: ", grid.min())
print("grid max: ", grid.max())

COLORS = {
    "OCEAN": (54, 141, 197),
    "blue": (0, 0, 255),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255),
    "Shallow water": (51, 153, 204),
    "Sand": (237, 201, 175),
    "Grassland / plains": (144, 238, 144),
    "Forest": (34, 139, 34)
}

def color(value): # need new bands brown - 
    # Maps the noise value to a color
    # if value < -0.5:
    #     return COLORS["OCEAN"] # Dark blue for low values
    # elif value < 0:
    #     return COLORS["blue"] # Blue for medium-low values
    # elif value < 0.5:
    #     return COLORS["Sand"] # Cyan for medium-high values
    # else:
    #     return COLORS["white"] # White for high values

    low = -1.0
    low_end = -0.5
    medium_low = -0.25
    mid = 0.0
    high_medium = 0.25
    high_end = 0.5
    high = 1.0

    if value < low_end:
            return COLORS["OCEAN"] # Dark blue for low values
    elif value < medium_low:
            return COLORS["Shallow water"] # Blue for medium-low values
    elif value < high_medium:
            return COLORS["Sand"] # Cyan for medium-high values
    elif value < high_end:
            return COLORS["Grassland / plains"] # Cyan for medium-high values
    else:
            return COLORS["Forest"] # White for high values
    


def draw_grid(): # Draws the grid of cells on the Pygame window
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





