import pygame as pg
import pygame_gui as gui
from boid import Boid
from predator import Predator

# pygame initialization
pg.init()
window = pg.display.set_mode((800, 800))
pg.display.set_caption("Boids Simulation")

# window variables
width, height = 800, 600
# Set up the clock for a consistent frame rate
clock = pg.time.Clock()

# Set up the boids
num_boids = 50 # Number of boids
boids = ([Boid(width, height) for _ in range(num_boids)]) # initialize the boids

# Set up the predators
predator = Predator(width, height) # initialize the predator

# UI setup
manager = gui.UIManager((800, 800), "data/pygame_gui/themes/pygame_gui_theme.json")
# Create reset button
reset_button = gui.elements.UIButton(relative_rect=pg.Rect((20, 700), (100, 50)),
                                      text='Reset',
                                      manager=manager)
# set up sliders
cohesion_slider = gui.elements.UIHorizontalSlider(relative_rect=pg.Rect((140, 710), (200, 20)),
                                        start_value=1,
                                        value_range=(-2, 6),
                                        manager=manager,
                                        object_id="#cohesion_slider")
cohesion_label = gui.elements.UILabel(relative_rect=pg.Rect((140, 680), (200, 20)),
                                      text='Cohesion',
                                      manager=manager,
                                      object_id="#cohesion_label")

separation_slider = gui.elements.UIHorizontalSlider(relative_rect=pg.Rect((360, 710), (200, 20)),
                                           start_value=1,
                                           value_range=(-2,6 ),
                                           manager=manager,
                                           object_id="#separation_slider")
separation_label = gui.elements.UILabel(relative_rect=pg.Rect((360, 680), (200, 20)),
                                      text='Separation',
                                      manager=manager,
                                      object_id="#separation_label")

alignment_slider = gui.elements.UIHorizontalSlider(relative_rect=pg.Rect((580, 710), (200, 20)),
                                            start_value=1,
                                            value_range=(0, 3),
                                            manager=manager,
                                            object_id="#alignment_slider")
alignment_label = gui.elements.UILabel(relative_rect=pg.Rect((580, 680), (200, 20)),
                                      text='Alignment',
                                      manager=manager,
                                      object_id="#alignment_label")

# Main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == gui.UI_BUTTON_PRESSED:
            if event.ui_element == reset_button:
                print("Reset button pressed")
                # Reset sliders to default values
                cohesion_slider.set_current_value(1)
                separation_slider.set_current_value(1)
                alignment_slider.set_current_value(1)

                for boid in boids:
                    boid.adjust_cohesion(1)
                    boid.adjust_alignment(1)
                    boid.adjust_separation(1)

        if event.type == gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == cohesion_slider:
                for boid in boids:
                    boid.adjust_cohesion(event.value)
            elif event.ui_element == separation_slider:
                for boid in boids:
                    boid.adjust_separation(event.value)
            elif event.ui_element == alignment_slider:
                for boid in boids:
                    boid.adjust_alignment(event.value)
                
        manager.process_events(event)

    manager.update(clock.tick(24))  # Update the UI manager
    # Fill the window with black
    window.fill((0, 0, 0))

    # Update and draw boids
    for boid in boids:
        boid.update(boids,predator)
        boid.draw(window)
        #print(boid.position, boid.velocity)  # Print position and velocity for debugging
    
    predator.update(boids) # update the predator
    predator.draw(window) # draw the predator
    manager.draw_ui(window)  # Draw the UI elements

    # Update the display
    pg.display.flip()

    # Cap the frame rate to 24 FPS
    clock.tick(24)