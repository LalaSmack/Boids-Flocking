import pygame as pg
import pygame_gui as gui
from boid import Boid
from predator import Predator

# pygame initialization
pg.init()
window = pg.display.set_mode((800, 600))
pg.display.set_caption("Boids Simulation")

# window variables
width, height = window.get_size()
# Set up the clock for a consistent frame rate
clock = pg.time.Clock()

# Set up the boids
num_boids = 50 # Number of boids
boids = ([Boid(width, height) for _ in range(num_boids)]) # initialize the boids

# Set up the predators
predator = Predator(width, height) # initialize the predator

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
        boid.update(boids,predator)
        boid.draw(window)
        #print(boid.position, boid.velocity)  # Print position and velocity for debugging
    
    predator.update(boids) # update the predator
    predator.draw(window) # draw the predator
        

    # Update the display
    pg.display.flip()

    # Cap the frame rate to 24 FPS
    clock.tick(24)