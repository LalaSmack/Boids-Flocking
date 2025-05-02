import pygame as pg
import random
import numpy as np
from boid import Boid

# pygame initialization
pg.init()
window = pg.display.set_mode((800, 600))
pg.display.set_caption("Boids Simulation")

# window variables
width, height = window.get_size()
# Set up the clock for a consistent frame rate
clock = pg.time.Clock()

# Set up the boids
num_boids = 50
boids = ([Boid(width, height) for _ in range(num_boids)])

# Main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the window with black
    window.fill((0, 0, 0))

    # Update and draw boids
    for boid in boids:
        boid.update(boids, window)
        boid.draw(window)

    # Update the display
    pg.display.flip()

    # Cap the frame rate to 24 FPS
    clock.tick(24)